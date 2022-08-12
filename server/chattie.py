from __future__ import annotations

import dataclasses
import asyncio
import logging

import websockets
import msgpack

@dataclasses.dataclass
class Message:
    author: str
    content: str

    def __str__(self) -> str:
        return f"<{self.author}>: {self.content}"
    
    @classmethod
    def from_dict(cls, data: dict) -> Message:
        return cls(**data)

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)

class Server:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

        self.websockets = []
        self.messages = []
    
    async def handler(self, websocket: websockets.WebSocketServerProtocol):
        self.websockets.append(websocket)
        
        await websocket.send(msgpack.dumps([message.to_dict() for message in self.messages]))

        async for data in websocket:
            try:
                message = msgpack.loads(data)
            except (msgpack.UnpackException, ValueError):
                continue
            else:
                websockets.broadcast(self.websockets, msgpack.dumps([message]))

            logging.info(str(message))
            
            self.messages.append(Message.from_dict(message))

        self.websockets.remove(websocket)

    async def _run(self):
        async with websockets.serve(self.handler, self.host, self.port):
            await asyncio.Future()

    def run(self):
        try:
            asyncio.run(self._run())
        except KeyboardInterrupt:
            return