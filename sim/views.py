from django.shortcuts import render

# Create your views here.
import asyncio
import random
import time

from django.http import StreamingHttpResponse
from django.shortcuts import render

def sse_stream(request):
    """
    Sends server-sent events to the client.
    """
    def event_stream():
        emojis = ["🚀", "🐎", "🌅", "🦾", "🍇"]
        i = 0
        while True:
            yield f'data: {random.choice(emojis)} {i}\n\n'
            i += 1
            time.sleep(1)

    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')

def index(request):
    return render(request, 'sse.html')