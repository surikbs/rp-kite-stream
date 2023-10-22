import aiohttp
import websockets
from aiohttp import web
from src.login import get_access_token
from src.stream import connect_to_kite_ws

async def main(request):
    access_token = await get_access_token()

    # Connect to Kite Connect's WebSocket API
    await connect_to_kite_ws(access_token)

    return web.Response(text="WebSocket client connected to Kite")

app = web.Application()
app.router.add_get('/', main)

web.run_app(app)
