FROM python:3.12-bookworm

WORKDIR /app

# Install Python dependencies first (layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright Chromium WITH all system deps (--with-deps handles apt packages)
# Use shared path so any user can access the browser
ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright
RUN playwright install --with-deps chromium

# Copy application code
COPY . .

# Create non-root user for security
# Grant read access to Playwright browser binaries
RUN useradd -m -u 1000 appuser \
    && chown -R appuser:appuser /app \
    && chmod -R o+rx /ms-playwright

USER appuser

# Railway injects PORT at runtime; default to 8000 for local Docker
ENV PORT=8000

EXPOSE ${PORT}

CMD ["python", "-m", "app.main"]
