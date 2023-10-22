
import websockets


async def connect_to_kite_ws(access_token):
    async with websockets.connect('wss://websocket.kite.trade/') as websocket:
        # Authenticate with the Kite Connect WebSocket using the access token
        await websocket.send('{"a":"r", "v":1}')
        await websocket.send('{"a":"authenticate", "v": {"api_key": "your_api_key", "access_token": "' + access_token + '"}}')

        # Subscribe to market data or perform other actions
        await websocket.send('{"a":"subscribe", "v": ["NSE:RELIANCE"]}')

        # Handle incoming WebSocket messages
        async for message in websocket:
            print("Received:", message)
