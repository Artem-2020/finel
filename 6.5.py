from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

app = FastAPI(title="WebSocket Chat")

HTML_CONTENT = """
<!DOCTYPE html>
<html>
<head>
    <title>WebSocket Chat</title>
</head>
<body>
    <h1>WebSocket Chat</h1>
    <div>
        <input type="text" id="message" placeholder="Enter message">
        <button onclick="sendMessage()">Send</button>
    </div>
    <div id="messages" style="margin-top: 20px; border: 1px solid #ccc; padding: 10px; height: 300px; overflow-y: scroll;"></div>

    <script>
        const ws = new WebSocket("ws://localhost:8000/ws");
        const messagesDiv = document.getElementById('messages');
        const messageInput = document.getElementById('message');

        ws.onmessage = function(event) {
            const msg = document.createElement('div');
            msg.textContent = event.data;
            messagesDiv.appendChild(msg);
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        };

        function sendMessage() {
            const msg = messageInput.value;
            if (msg) {
                ws.send(msg);
                messageInput.value = '';
            }
        }

        messageInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') sendMessage();
        });
    </script>
</body>
</html>
"""

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            try:
                await connection.send_text(message)
            except:
                pass


manager = ConnectionManager()

@app.get("/")
async def get():
    return HTMLResponse(content=HTML_CONTENT)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"User: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast("User disconnected")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8002)