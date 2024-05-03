from pathlib import Path

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.chat.Manager import ConnectionManager
from src.chat.models import Message
from src.datebase import get_async_session

router = APIRouter(
    prefix='/chat',
    tags=['Chat']
)

manager = ConnectionManager()


@router.get("/last_messages")
async def get_last_messages(
        session: AsyncSession = Depends(get_async_session)
):
    query = select(Message).order_by(Message.id.desc()).limit(5)
    messages = await session.execute(query)
    mes = messages.scalars().all()
    print(mes)
    return mes


@router.websocket("/send_message/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Client #{client_id} says: {data}", add_to_db=True)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left",add_to_db=False)




BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))


@router.get("/chat")
def get_chat_page(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})
