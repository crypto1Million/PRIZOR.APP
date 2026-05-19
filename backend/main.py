from fastapi import FastAPI
from backend.database import engine, Base
from backend.routes import users, swipe, chat, auth, upload
from fastapi import WebSocket
from backend.routes import match
from backend.database import Base, engine
from backend.core.scheduler import scheduler
from backend.routes import report
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from backend.core.limiter import limiter
from backend.routes import block
from fastapi.responses import JSONResponse
from backend.routes.discovery import router as discovery_router 
from backend.routes import discovery 
from backend.routes import password_reset
import models 

Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url="/docs", redoc_url="/redoc")

scheduler.start()

Base.metadata.create_all(bind=engine)

app.include_router(upload.router)
app.include_router(users.router)
app.include_router(discovery_router, prefix="/discovery", tags=["Discovery"])
app.include_router(auth.router)
app.include_router(chat.router)
app.include_router(swipe.router)
app.include_router(match.router)
app.include_router(report.router)
app.include_router(block.router)
app.include_router(
    password_reset.router,
    prefix="/auth",
    tags=["Password Reset"]
)
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)


@app.get("/")
def root():
    return {"status": "upgraded running"}