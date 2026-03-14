"""Playwright browser singleton managed via FastAPI lifespan."""

from __future__ import annotations

import logging

from playwright.async_api import Browser, async_playwright

from app.config import settings

logger = logging.getLogger(__name__)

_playwright_instance = None
_browser: Browser | None = None


async def get_browser() -> Browser:
    """Return the shared browser instance, launching it if needed."""
    global _playwright_instance, _browser
    if _browser is None:
        _playwright_instance = await async_playwright().start()
        _browser = await _playwright_instance.chromium.launch(
            headless=settings.browser_headless,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
            ],
        )
        logger.info("Playwright browser launched (headless=%s)", settings.browser_headless)
    return _browser


async def shutdown_browser() -> None:
    """Close the shared browser and Playwright instance."""
    global _playwright_instance, _browser
    if _browser is not None:
        await _browser.close()
        _browser = None
        logger.info("Playwright browser closed.")
    if _playwright_instance is not None:
        await _playwright_instance.stop()
        _playwright_instance = None
        logger.info("Playwright instance stopped.")
