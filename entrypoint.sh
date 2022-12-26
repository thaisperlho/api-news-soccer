gunicorn \
    -b 0.0.0.0:8081 \
    -w 2 \
    -k "uvicorn.workers.UvicornWorker" \
    --timeout 600 \
    --max-requests 10000 \
    --keep-alive 5 \
    --graceful-timeout 40 \
    --log-level debug \
    "main:create_app()"