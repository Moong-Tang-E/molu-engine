from fastapi import APIRouter, Depends, HTTPException, status, Form, File, UploadFile
from fastapi.responses import RedirectResponse, FileResponse


router = APIRouter()
