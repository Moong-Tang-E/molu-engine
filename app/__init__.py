import json
import os
import motor.motor_asyncio
import contextlib

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import router


app_config = {
    "title": "molu-engine",
    "description": "Next Generation Wiki Engine",
    "version": "0.0.1",
    "redoc_url": "/docs/redoc",
    "docs_url": "/docs/swagger",
}

app = FastAPI(**app_config)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MONGO_URI = os.getenv("MONGO_URL", "mongodb://tmddn3070:ss080826@172.30.1.46:27017/?authMechanism=DEFAULT")

client = motor.motor_asyncio.MotorClient(MONGO_URI,
                                         maxPoolSize=100,
                                         minPoolSize=10,
                                         maxIdleTimeMS=30000
                                        ) # 커넥션 풀 옵션 설정

@contextlib.asynccontextmanager # async_generator 데코레이터 적용
async def get_db():
    db = client.wiki
    try:
        yield db
    finally:
        await client.close() # 커넥션 반납
        
app.include_router(router)
