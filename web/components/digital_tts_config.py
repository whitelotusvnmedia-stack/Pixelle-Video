# Copyright (C) 2025 AIDC-AI
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Style configuration components for web UI (middle column)
"""

import os
from pathlib import Path

import streamlit as st
from loguru import logger

from web.i18n import tr, get_language
from web.utils.async_helpers import run_async
from pixelle_video.config import config_manager


def render_style_config(pixelle_video):
    """Render style configuration section (middle column)"""
    # TTS Section (moved from left column)
    # ====================================================================
    with st.container(border=True):
        st.markdown(f"**{tr('section.tts')}**")
        
        with st.expander(tr("help.feature_description"), expanded=False):
            st.markdown(f"**{tr('help.what')}**")
            st.markdown(tr("tts.what"))
            st.markdown(f"**{tr('help.how')}**")
            st.markdown(tr("tts.how"))
        
        # Get TTS config
        comfyui_config = config_manager.get_comfyui_config()
        tts_config = comfyui_config["tts"]
        
        # Inference mode selection
        tts_mode = st.radio(
            tr("tts.inference_mode"),
            ["local", "comfyui"],
            horizontal=True,
            format_func=lambda x: tr(f"tts.mode.{x}"),
            index=0 if tts_config.get("inference_mode", "local") == "local" else 1,
            key="digital_tts_inference_mode"
        )
        
        # Show hint based on mode
        if tts_mode == "local":
            st.caption(tr("tts.mode.local_hint"))
        else:
            st.caption(tr("tts.mode.comfyui_hint"))
        
        # ================================================================
        # Local Mode UI
        # ================================================================
        if tts_mode == "local":
            # Import voice configuration
            from pixelle_video.tts_voices import EDGE_TTS_VOICES, get_voice_display_name
            from pixelle_video.utils.tts_providers import TTS_PROVIDERS, get_provider_info
            
            # Get saved config
            local_config = tts_config.get("local", {})
            saved_voice = local_config.get("voice", "vi-VN-HoaiMyNeural")
            saved_speed = local_config.get("speed", 1.2)
            saved_provider = local_config.get("provider", "edge_tts")
            
            # TTS Provider selection
            provider_ids = [p["id"] for p in TTS_PROVIDERS]
            provider_names = [p["name"] for p in TTS_PROVIDERS]
            provider_default = provider_ids.index(saved_provider) if saved_provider in provider_ids else 0
            
            selected_provider_name = st.selectbox(
                tr("tts.provider", fallback="TTS Provider"),
                provider_names,
                index=provider_default,
                key="digital_tts_provider_select"
            )
            selected_provider = provider_ids[provider_names.index(selected_provider_name)]
            
            # Voice and speed for Edge TTS
            if selected_provider == "edge_tts":
                voice_options = []
                voice_ids = []
                default_voice_index = 0
                custom_voice_label = tr("tts.voice.custom", fallback="Custom Voice ID...")
                
                for idx, voice_config in enumerate(EDGE_TTS_VOICES):
                    voice_id = voice_config["id"]
                    display_name = get_voice_display_name(voice_id, tr, get_language())
                    voice_options.append(display_name)
                    voice_ids.append(voice_id)
                    if voice_id == saved_voice:
                        default_voice_index = idx
                
                voice_options.append(custom_voice_label)
                voice_ids.append("__custom__")
                if saved_voice not in [v["id"] for v in EDGE_TTS_VOICES]:
                    default_voice_index = len(voice_options) - 1
                
                voice_col, speed_col = st.columns([1, 1])
                with voice_col:
                    selected_voice_display = st.selectbox(
                        tr("tts.voice_selector"), voice_options,
                        index=default_voice_index, key="digital_tts_local_voice"
                    )
                    selected_voice_index = voice_options.index(selected_voice_display)
                    selected_voice = voice_ids[selected_voice_index]
                    if selected_voice == "__custom__":
                        custom_voice_id = st.text_input(
                            tr("tts.voice.custom_input", fallback="Edge TTS Voice ID"),
                            value=saved_voice if saved_voice not in [v["id"] for v in EDGE_TTS_VOICES] else "",
                            placeholder="vi-VN-HoaiMyNeural",
                            key="digital_tts_custom_voice_id"
                        )
                        if custom_voice_id:
                            selected_voice = custom_voice_id
                with speed_col:
                    tts_speed = st.slider(
                        tr("tts.speed"), min_value=0.5, max_value=2.0,
                        value=saved_speed, step=0.1, format="%.1fx",
                        key="digital_tts_local_speed"
                    )
            else:
                voice_col, speed_col = st.columns([1, 1])
                with voice_col:
                    selected_voice = st.text_input(
                        tr("tts.voice_selector"), value=saved_voice,
                        key="digital_tts_local_voice"
                    )
                with speed_col:
                    tts_speed = st.slider(
                        tr("tts.speed"), min_value=0.5, max_value=2.0,
                        value=saved_speed, step=0.1, format="%.1fx",
                        key="digital_tts_local_speed"
                    )
            
            # Variables for video generation
            tts_workflow_key = None
            ref_audio_path = None
        
        # ================================================================
        # ComfyUI Mode UI
        # ================================================================
        else:  # comfyui mode
            tts_workflow_key = "runninghub/tts_index2.json"  # fallback
            
            # Reference audio upload (optional, for voice cloning)
            ref_audio_file = st.file_uploader(
                tr("tts.ref_audio"),
                type=["mp3", "wav", "flac", "m4a", "aac", "ogg"],
                help=tr("tts.ref_audio_help"),
                key="digital_ref_audio_upload"
            )
            
            # Save uploaded ref_audio to temp file if provided
            ref_audio_path = None
            if ref_audio_file is not None:
                # Audio preview player (directly play uploaded file)
                st.audio(ref_audio_file)
                
                # Save to temp directory
                temp_dir = Path("temp")
                temp_dir.mkdir(exist_ok=True)
                ref_audio_path = temp_dir / f"ref_audio_{ref_audio_file.name}"
                with open(ref_audio_path, "wb") as f:
                    f.write(ref_audio_file.getbuffer())
            
            # Variables for video generation
            selected_voice = None
            tts_speed = None
        
        # ================================================================
        # TTS Preview (works for both modes)
        # ================================================================
        with st.expander(tr("tts.preview_title"), expanded=False):
            # Preview text input
            preview_text = st.text_input(
                tr("tts.preview_text"),
                value="大家好，这是一段测试语音。",
                placeholder=tr("tts.preview_text_placeholder"),
                key="digital_tts_preview_text"
            )
            
            # Preview button
            if st.button(tr("tts.preview_button"), key="gidital_preview_tts", use_container_width=True):
                with st.spinner(tr("tts.previewing")):
                    try:
                        # Build TTS params based on mode
                        tts_params = {
                            "text": preview_text,
                            "inference_mode": tts_mode
                        }
                        
                        if tts_mode == "local":
                            tts_params["voice"] = selected_voice
                            tts_params["speed"] = tts_speed
                        else:  # comfyui
                            tts_params["workflow"] = tts_workflow_key
                            if ref_audio_path:
                                tts_params["ref_audio"] = str(ref_audio_path)
                        
                        audio_path = run_async(pixelle_video.tts(**tts_params))
                        
                        # Play the audio
                        if audio_path:
                            st.success(tr("tts.preview_success"))
                            if os.path.exists(audio_path):
                                st.audio(audio_path, format="audio/mp3")
                            elif audio_path.startswith('http'):
                                st.audio(audio_path)
                            else:
                                st.error("Failed to generate preview audio")
                            
                            # Show file path
                            st.caption(f"📁 {audio_path}")
                        else:
                            st.error("Failed to generate preview audio")
                    except Exception as e:
                        st.error(tr("tts.preview_failed", error=str(e)))
                        logger.exception(e)
    
    # Return all style configuration parameters (Simplified version only local TTS)
    return {
        "tts_inference_mode": tts_mode,
        "tts_voice": selected_voice if tts_mode == "local" else None,
        "tts_speed": tts_speed if tts_mode == "local" else None,
        "tts_workflow": tts_workflow_key if tts_mode == "comfyui" else None,
        "ref_audio": str(ref_audio_path) if ref_audio_path else None,
    }