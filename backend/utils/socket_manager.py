from fastapi import WebSocket


class ConnectionManager:
    def init(self):
        self.active_connections = {}

    # ==============================
    # CONNECT
    # ==============================
    async def connect(self, user_id: int, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[user_id] = websocket

    # ==============================
    # DISCONNECT
    # ==============================
    def disconnect(self, user_id: int):
        if user_id in self.active_connections:
            del self.active_connections[user_id]

    # ==============================
    # SEND PERSONAL MESSAGE
    # ==============================
    async def send_personal(self, user_id: int, data: dict):
        websocket = self.active_connections.get(user_id)

        if websocket:
            await websocket.send_json(data)

    # ==============================
    # CHECK ONLINE STATUS
    # ==============================
    def is_connected(self, user_id: int):
        return user_id in self.active_connections


manager = ConnectionManager()