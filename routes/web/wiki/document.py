from fastapi import APIRouter, Depends, HTTPException, status, RedirectResponse


router = APIRouter()


@router.get("/{document_name}")
async def redirect_document(document_name: str):
    return RedirectResponse(f"/w/{document_name}")

