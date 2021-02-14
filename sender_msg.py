import asyncio
import websockets
import logging

logging.basicConfig(level=logging.INFO)

async def produce(event_name: str, message:str, host: str, port: int) -> None:
    async with websockets.connect(f"ws://{host}:{port}") as ws:
        await ws.send(message)
        await ws.recv()
