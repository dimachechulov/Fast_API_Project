from fastapi import WebSocket, Depends
from sqlalchemy import insert

from src.chat.models import Message
from src.datebase import get_async_session, async_session_maker


class ConnectionManager:
    """Class defining socket events"""

    def __init__(self):
        """init method, keeping track of connections"""
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        """connect event"""
        await websocket.accept()
        self.active_connections.append(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        """Direct Message"""
        await websocket.send_text(message)


    async def broadcast(self, message: str, add_to_db: bool):
        if add_to_db:
            await self.add_messages_to_database(message)
        for connection in self.active_connections:
            await connection.send_text(message)

    @staticmethod
    async def add_messages_to_database(message: str):
        async with async_session_maker() as session:
            stmt = insert(Message).values(
                content=message
            )
            await session.execute(stmt)
            await session.commit()

    def disconnect(self, websocket: WebSocket):
        """disconnect event"""
        self.active_connections.remove(websocket)
