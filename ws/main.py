# https://medium.com/@navneetskahlon/building-a-real-time-chat-application-with-fastapi-and-websocket-3357c261d01d

from fastapi import FastAPI, WebSocket
import uvicorn

app = FastAPI()


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message received from {client_id}: {data}")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
