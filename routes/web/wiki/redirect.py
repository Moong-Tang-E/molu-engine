from fastapi import APIRouter, Depends, HTTPException, status
from starlette.responses import RedirectResponse


router = APIRouter()


@router.get("/{document_name}")
async def redirect_document(document_name: str):
    return RedirectResponse(f"/w/{document_name}")

@router.get("/{document_name}/debate")
async def redirect_document_debate(document_name: str):
    return RedirectResponse(f"/w/{document_name}/debate")

@router.get("/{document_name}/edit")
async def redirect_document_edit(document_name: str):
    return RedirectResponse(f"/w/{document_name}/edit")

@router.get("/{document_name}/history")
async def redirect_document_history(document_name: str):
    return RedirectResponse(f"/w/{document_name}/history")
