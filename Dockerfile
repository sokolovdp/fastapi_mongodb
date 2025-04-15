FROM python:3.13-bookworm

# Set environment variables in a single layer
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

# Set working directory to avoid relative paths
WORKDIR /fastapi

# Copy only requirements files first for caching
COPY requirements.txt requirements_prod.txt ./

# Upgrade pip and install dependencies in one layer
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements_prod.txt

# Copy application code and entrypoints
COPY app/ /fastapi

# Use non-root user for security
RUN useradd -m appuser && chown -R appuser:appuser /fastapi
USER appuser

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
