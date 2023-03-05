from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import APIKeyHeader, APIKeyQuery
import os

api_key = 0000


apikey = APIKeyQuery(name="apikey")

#API처리용은 요청 함수 안에 포함 key: str = Depends(verify_apikey)

def verify_apikey(key: str = Depends(apikey)):
    """Verify API key"""
    if key != api_key:
        raise HTTPException(status_code=401, detail="API system only available for internal use")
    return key


