from fastapi import APIRouter

#import router
from routes.web.wiki.document import router as wiki_document_router
router = APIRouter()

#add router
router.include_router(wiki_document_router, tags=["wiki_document"])
