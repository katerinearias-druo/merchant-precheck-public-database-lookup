"""Random browser fingerprint generator for anti-detection."""

from __future__ import annotations

import random

# Chrome versions on Windows, Mac, Linux
_USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
]

_VIEWPORTS = [
    {"width": 1920, "height": 1080},
    {"width": 1366, "height": 768},
    {"width": 1536, "height": 864},
    {"width": 1440, "height": 900},
    {"width": 1280, "height": 720},
    {"width": 1600, "height": 900},
    {"width": 1280, "height": 800},
    {"width": 1680, "height": 1050},
]

# Colombian cities and nearby timezones/locales
_LOCALES_AND_TIMEZONES = [
    {"locale": "es-CO", "timezone": "America/Bogota"},
    {"locale": "es-CO", "timezone": "America/Bogota"},
    {"locale": "es-MX", "timezone": "America/Mexico_City"},
    {"locale": "es-ES", "timezone": "Europe/Madrid"},
    {"locale": "es-AR", "timezone": "America/Argentina/Buenos_Aires"},
    {"locale": "en-US", "timezone": "America/New_York"},
    {"locale": "en-US", "timezone": "America/Chicago"},
    {"locale": "pt-BR", "timezone": "America/Sao_Paulo"},
]


def random_fingerprint() -> dict:
    """Generate a random browser context config for Playwright.

    Returns a dict ready to pass to browser.new_context(**fingerprint).
    """
    lt = random.choice(_LOCALES_AND_TIMEZONES)
    return {
        "user_agent": random.choice(_USER_AGENTS),
        "viewport": random.choice(_VIEWPORTS),
        "locale": lt["locale"],
        "timezone_id": lt["timezone"],
    }
