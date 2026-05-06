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
API Key Rotation - Round-robin key rotation with automatic fallback on quota errors.

Supports multiple API keys separated by semicolons or newlines.
When a key hits quota/rate-limit, automatically rotates to the next key.
"""

import threading
from typing import List, Optional

from loguru import logger


# HTTP status codes that indicate quota/rate-limit exhaustion
QUOTA_ERROR_CODES = {429, 402, 503}

# Error message substrings that indicate quota exhaustion
QUOTA_ERROR_MESSAGES = [
    "quota",
    "rate limit",
    "rate_limit",
    "too many requests",
    "insufficient_quota",
    "billing",
    "exceeded",
    "resource_exhausted",
]


class APIKeyRotator:
    """
    Manages a pool of API keys with round-robin rotation.

    Usage:
        rotator = APIKeyRotator("key1;key2;key3")
        key = rotator.get_key()
        # On quota error:
        rotator.mark_exhausted(key)
        next_key = rotator.get_key()
    """

    def __init__(self, keys_str: str):
        self._keys = parse_api_keys(keys_str)
        self._index = 0
        self._lock = threading.Lock()
        self._exhausted: set = set()

    @property
    def total_keys(self) -> int:
        return len(self._keys)

    def get_key(self) -> str:
        """Get the current active API key."""
        with self._lock:
            if not self._keys:
                return ""
            # Find a non-exhausted key starting from current index
            for _ in range(len(self._keys)):
                key = self._keys[self._index % len(self._keys)]
                if key not in self._exhausted:
                    return key
                self._index = (self._index + 1) % len(self._keys)
            # All keys exhausted, reset and return current
            self._exhausted.clear()
            logger.warning("All API keys exhausted, resetting rotation")
            return self._keys[self._index % len(self._keys)]

    def mark_exhausted(self, key: str):
        """Mark a key as exhausted and rotate to next."""
        with self._lock:
            self._exhausted.add(key)
            self._index = (self._index + 1) % len(self._keys)
            remaining = len(self._keys) - len(self._exhausted)
            logger.info(f"API key rotated. Remaining keys: {remaining}/{len(self._keys)}")

    def reset(self):
        """Reset all keys to available state."""
        with self._lock:
            self._exhausted.clear()
            self._index = 0


def parse_api_keys(keys_str: str) -> List[str]:
    """
    Parse multiple API keys from a string.

    Supports separators: semicolon (;), newline, comma.
    Strips whitespace and filters empty strings.

    Args:
        keys_str: Raw string containing one or more API keys

    Returns:
        List of cleaned API key strings
    """
    if not keys_str:
        return []
    # Replace common separators with semicolon, then split
    normalized = keys_str.replace("\n", ";").replace(",", ";")
    keys = [k.strip() for k in normalized.split(";")]
    return [k for k in keys if k]


def is_quota_error(error: Exception) -> bool:
    """
    Check if an exception indicates API quota/rate-limit exhaustion.

    Args:
        error: The exception to check

    Returns:
        True if the error is a quota/rate-limit error
    """
    error_str = str(error).lower()

    # Check error message substrings
    for msg in QUOTA_ERROR_MESSAGES:
        if msg in error_str:
            return True

    # Check HTTP status code if available
    status_code = getattr(error, "status_code", None)
    if status_code and status_code in QUOTA_ERROR_CODES:
        return True

    # Check nested response status
    response = getattr(error, "response", None)
    if response is not None:
        resp_status = getattr(response, "status_code", None)
        if resp_status and resp_status in QUOTA_ERROR_CODES:
            return True

    return False
