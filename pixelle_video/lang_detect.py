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
Language detection for script text and voice auto-matching.

Detects script language based on Unicode character ranges and suggests
the most appropriate Edge TTS voice.
"""

import re
import unicodedata
from typing import Optional, Tuple


# Default voice for each detected language
LANG_DEFAULT_VOICES = {
    "vi": ("vi-VN-HoaiMyNeural", "vi-VN-NamMinhNeural"),
    "zh": ("zh-CN-XiaoxiaoNeural", "zh-CN-YunjianNeural"),
    "en": ("en-US-AriaNeural", "en-US-GuyNeural"),
    "ko": ("ko-KR-SunHiNeural", "ko-KR-InJoonNeural"),
    "fr": ("fr-FR-EloiseNeural", "fr-FR-HenriNeural"),
    "de": ("de-DE-AmalaNeural", "de-DE-ConradNeural"),
    "pt": ("pt-PT-RaquelNeural", "pt-PT-DuarteNeural"),
    "ru": ("ru-RU-SvetlanaNeural", "ru-RU-DmitryNeural"),
    "tr": ("tr-TR-EmelNeural", "tr-TR-AhmetNeural"),
    "es": ("es-ES-ElviraNeural", "es-ES-AlvaroNeural"),
    "ja": ("ja-JP-NanamiNeural", "ja-JP-KeitaNeural"),
}


# Vietnamese-specific diacritical marks (combining characters)
_VIETNAMESE_CHARS = set("àáảãạăắằẳẵặâấầẩẫậèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵđ"
                        "ÀÁẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬÈÉẺẼẸÊẾỀỂỄỆÌÍỈĨỊÒÓỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÙÚỦŨỤƯỨỪỬỮỰỲÝỶỸỴĐ")


def detect_language(text: str) -> str:
    """
    Detect the primary language of the given text.

    Uses Unicode character ranges to identify scripts:
    - Vietnamese: Latin chars with Vietnamese-specific diacritics
    - Chinese: CJK Unified Ideographs
    - Korean: Hangul syllables
    - Japanese: Hiragana/Katakana (+ CJK)
    - Others: Latin-based languages detected by character frequency

    Args:
        text: Input text to analyze

    Returns:
        ISO 639-1 language code (e.g., "vi", "zh", "en", "ko", "ja")
    """
    if not text or not text.strip():
        return "en"

    # Count character types
    vietnamese_count = 0
    chinese_count = 0
    korean_count = 0
    japanese_count = 0
    latin_count = 0
    cyrillic_count = 0
    total_alpha = 0

    for char in text:
        if not char.isalpha():
            continue
        total_alpha += 1

        # Vietnamese detection (specific diacritical marks)
        if char in _VIETNAMESE_CHARS:
            vietnamese_count += 1

        # CJK Unified Ideographs
        cp = ord(char)
        if 0x4E00 <= cp <= 0x9FFF or 0x3400 <= cp <= 0x4DBF:
            chinese_count += 1
        # Hangul
        elif 0xAC00 <= cp <= 0xD7AF or 0x1100 <= cp <= 0x11FF:
            korean_count += 1
        # Hiragana / Katakana
        elif 0x3040 <= cp <= 0x309F or 0x30A0 <= cp <= 0x30FF:
            japanese_count += 1
        # Cyrillic
        elif 0x0400 <= cp <= 0x04FF:
            cyrillic_count += 1
        # Latin
        elif char.isascii() or unicodedata.category(char).startswith('L'):
            latin_count += 1

    if total_alpha == 0:
        return "en"

    # Vietnamese has priority if we see Vietnamese-specific chars
    if vietnamese_count > 0 and vietnamese_count / total_alpha > 0.02:
        return "vi"

    # CJK-dominant text
    if chinese_count > 0 and chinese_count / total_alpha > 0.3:
        # Disambiguate Chinese vs Japanese
        if japanese_count > 0 and japanese_count / (chinese_count + japanese_count) > 0.15:
            return "ja"
        return "zh"

    if korean_count > 0 and korean_count / total_alpha > 0.3:
        return "ko"

    if japanese_count > 0 and japanese_count / total_alpha > 0.1:
        return "ja"

    if cyrillic_count > 0 and cyrillic_count / total_alpha > 0.3:
        return "ru"

    # Latin-based: try heuristics for specific languages
    lower_text = text.lower()

    # French markers
    if re.search(r"[àâéèêëïîôùûüÿçœæ]", lower_text):
        fr_words = ["le", "la", "les", "de", "des", "du", "un", "une", "est", "et", "en", "que", "qui"]
        if sum(1 for w in fr_words if f" {w} " in f" {lower_text} ") >= 2:
            return "fr"

    # German markers
    if re.search(r"[äöüß]", lower_text):
        de_words = ["der", "die", "das", "und", "ist", "ein", "eine", "nicht", "mit", "auf"]
        if sum(1 for w in de_words if f" {w} " in f" {lower_text} ") >= 2:
            return "de"

    # Spanish markers
    if re.search(r"[ñ¿¡]", lower_text):
        return "es"
    es_words = ["el", "la", "los", "las", "de", "del", "en", "que", "por", "con", "una"]
    if sum(1 for w in es_words if f" {w} " in f" {lower_text} ") >= 3:
        return "es"

    # Portuguese markers
    pt_words = ["o", "a", "os", "as", "de", "do", "da", "em", "que", "não", "com"]
    if sum(1 for w in pt_words if f" {w} " in f" {lower_text} ") >= 3:
        return "pt"

    # Turkish markers
    if re.search(r"[ığşçö]", lower_text):
        return "tr"

    # Default to English for Latin text
    return "en"


def suggest_voice(text: str, gender: str = "female") -> Optional[str]:
    """
    Suggest an appropriate TTS voice based on script text language.

    Args:
        text: Script text to analyze
        gender: Preferred gender ("female" or "male")

    Returns:
        Suggested Edge TTS voice ID, or None if no match
    """
    lang = detect_language(text)
    voices = LANG_DEFAULT_VOICES.get(lang)
    if not voices:
        voices = LANG_DEFAULT_VOICES["en"]

    idx = 0 if gender == "female" else 1
    return voices[idx]


def get_language_name(lang_code: str) -> str:
    """Get human-readable language name."""
    names = {
        "vi": "Tiếng Việt",
        "zh": "中文",
        "en": "English",
        "ko": "한국어",
        "ja": "日本語",
        "fr": "Français",
        "de": "Deutsch",
        "pt": "Português",
        "ru": "Русский",
        "tr": "Türkçe",
        "es": "Español",
    }
    return names.get(lang_code, lang_code)
