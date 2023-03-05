from fastapi import APIRouter

#import router
from routes.web.wiki.redirect import router as redirect_router
router = APIRouter()

#add router
router.include_router(redirect_router, tags=["wiki_document"])
