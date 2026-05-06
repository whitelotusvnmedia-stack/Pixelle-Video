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
Multi-provider TTS utility.

Supports Edge TTS (free), OpenAI TTS, Google Cloud TTS, and ElevenLabs.
Each provider returns audio bytes and saves to output_path if given.
"""

import uuid
from pathlib import Path
from typing import Optional

import httpx
from loguru import logger


# ── Provider metadata ────────────────────────────────────────────────────────

TTS_PROVIDERS = [
    {
        "id": "edge_tts",
        "name": "Edge TTS (Free)",
        "needs_api_key": False,
    },
    {
        "id": "openai_tts",
        "name": "OpenAI TTS",
        "needs_api_key": True,
        "api_key_url": "https://platform.openai.com/api-keys",
        "voices": ["alloy", "ash", "ballad", "coral", "echo", "fable", "onyx", "nova", "sage", "shimmer"],
        "models": ["tts-1", "tts-1-hd", "gpt-4o-mini-tts"],
    },
    {
        "id": "google_tts",
        "name": "Google Cloud TTS",
        "needs_api_key": True,
        "api_key_url": "https://console.cloud.google.com/apis/credentials",
        "hint": "Requires a Google Cloud API key with Text-to-Speech API enabled",
    },
    {
        "id": "elevenlabs",
        "name": "ElevenLabs",
        "needs_api_key": True,
        "api_key_url": "https://elevenlabs.io/app/settings/api-keys",
        "voices": ["Rachel", "Domi", "Bella", "Antoni", "Elli", "Josh", "Arnold", "Adam", "Sam"],
    },
]


def get_provider_info(provider_id: str) -> Optional[dict]:
    """Get provider metadata by ID."""
    for p in TTS_PROVIDERS:
        if p["id"] == provider_id:
            return p
    return None


def get_provider_names() -> list:
    """Return list of (id, display_name) tuples."""
    return [(p["id"], p["name"]) for p in TTS_PROVIDERS]


# ── OpenAI TTS ───────────────────────────────────────────────────────────────

async def openai_tts(
    text: str,
    api_key: str,
    voice: str = "alloy",
    model: str = "tts-1",
    speed: float = 1.0,
    output_path: Optional[str] = None,
) -> str:
    """
    Generate speech using OpenAI TTS API.

    Args:
        text: Text to convert
        api_key: OpenAI API key
        voice: Voice name (alloy, echo, fable, onyx, nova, shimmer, etc.)
        model: TTS model (tts-1, tts-1-hd, gpt-4o-mini-tts)
        speed: Speed multiplier 0.25-4.0
        output_path: Output file path (auto-generated if None)

    Returns:
        Path to generated audio file
    """
    if not output_path:
        Path("output").mkdir(parents=True, exist_ok=True)
        output_path = f"output/{uuid.uuid4().hex}.mp3"

    logger.info(f"OpenAI TTS: voice={voice}, model={model}, speed={speed}")

    async with httpx.AsyncClient(timeout=60.0) as client:
        response = await client.post(
            "https://api.openai.com/v1/audio/speech",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": model,
                "input": text,
                "voice": voice,
                "speed": speed,
                "response_format": "mp3",
            },
        )
        response.raise_for_status()

        with open(output_path, "wb") as f:
            f.write(response.content)

    logger.info(f"OpenAI TTS generated: {output_path}")
    return output_path


# ── Google Cloud TTS ─────────────────────────────────────────────────────────

async def google_cloud_tts(
    text: str,
    api_key: str,
    voice: str = "en-US-Standard-A",
    language_code: str = "en-US",
    speed: float = 1.0,
    output_path: Optional[str] = None,
) -> str:
    """
    Generate speech using Google Cloud Text-to-Speech API.

    Args:
        text: Text to convert
        api_key: Google Cloud API key
        voice: Voice name (e.g. en-US-Standard-A, vi-VN-Standard-A)
        language_code: BCP-47 language code (e.g. en-US, vi-VN)
        speed: Speed multiplier 0.25-4.0
        output_path: Output file path

    Returns:
        Path to generated audio file
    """
    import base64

    if not output_path:
        Path("output").mkdir(parents=True, exist_ok=True)
        output_path = f"output/{uuid.uuid4().hex}.mp3"

    logger.info(f"Google TTS: voice={voice}, lang={language_code}, speed={speed}")

    async with httpx.AsyncClient(timeout=60.0) as client:
        response = await client.post(
            f"https://texttospeech.googleapis.com/v1/text:synthesize?key={api_key}",
            json={
                "input": {"text": text},
                "voice": {
                    "languageCode": language_code,
                    "name": voice,
                },
                "audioConfig": {
                    "audioEncoding": "MP3",
                    "speakingRate": speed,
                },
            },
        )
        response.raise_for_status()
        audio_content = base64.b64decode(response.json()["audioContent"])

        with open(output_path, "wb") as f:
            f.write(audio_content)

    logger.info(f"Google TTS generated: {output_path}")
    return output_path


# ── ElevenLabs ───────────────────────────────────────────────────────────────

async def elevenlabs_tts(
    text: str,
    api_key: str,
    voice_id: str = "21m00Tcm4TlvDq8ikWAM",
    model_id: str = "eleven_multilingual_v2",
    speed: float = 1.0,
    output_path: Optional[str] = None,
) -> str:
    """
    Generate speech using ElevenLabs API.

    Args:
        text: Text to convert
        api_key: ElevenLabs API key
        voice_id: ElevenLabs voice ID
        model_id: Model ID (eleven_multilingual_v2, eleven_turbo_v2_5, etc.)
        speed: Speed multiplier
        output_path: Output file path

    Returns:
        Path to generated audio file
    """
    if not output_path:
        Path("output").mkdir(parents=True, exist_ok=True)
        output_path = f"output/{uuid.uuid4().hex}.mp3"

    logger.info(f"ElevenLabs TTS: voice_id={voice_id}, model={model_id}")

    async with httpx.AsyncClient(timeout=60.0) as client:
        response = await client.post(
            f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
            headers={
                "xi-api-key": api_key,
                "Content-Type": "application/json",
                "Accept": "audio/mpeg",
            },
            json={
                "text": text,
                "model_id": model_id,
                "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.75,
                    "speed": speed,
                },
            },
        )
        response.raise_for_status()

        with open(output_path, "wb") as f:
            f.write(response.content)

    logger.info(f"ElevenLabs TTS generated: {output_path}")
    return output_path


async def elevenlabs_list_voices(api_key: str) -> list:
    """Fetch available voices from ElevenLabs API."""
    async with httpx.AsyncClient(timeout=15.0) as client:
        response = await client.get(
            "https://api.elevenlabs.io/v1/voices",
            headers={"xi-api-key": api_key},
        )
        response.raise_for_status()
        data = response.json()
        return [
            {"voice_id": v["voice_id"], "name": v["name"]}
            for v in data.get("voices", [])
        ]
