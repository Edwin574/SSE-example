import os
import asyncio
from django.core.asgi import get_asgi_application
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sse.settings')
django_app = get_asgi_application()

async def sse_stream(scope, receive, send):
    assert scope["type"] == "http"
    headers = [(b"content-type", b"text/event-stream")]
    await send({
        "type": "http.response.start",
        "status": 200,
        "headers": headers,
    })
    emojis = ["🚀", "🐎", "🌅", "🦾", "🍇"]
    i = 0
    try:
        while True:
            data = f"data: {random.choice(emojis)} {i}\n\n"
            await send({
                "type": "http.response.body",
                "body": data.encode("utf-8"),
                "more_body": True,
            })
            await asyncio.sleep(1)
            i += 1
    except asyncio.CancelledError:
        print("SSE client disconnected")

async def application(scope, receive, send):
    if scope["type"] == "http" and scope["path"] == "/stream-data/":
        await sse_stream(scope, receive, send)
    else:
        await django_app(scope, receive, send)
