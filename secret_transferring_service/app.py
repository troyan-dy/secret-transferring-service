import uvicorn
from fastapi import APIRouter, FastAPI
from starlette.responses import PlainTextResponse

api_router = APIRouter()


@api_router.get("/ping")
async def ping() -> PlainTextResponse:
    return PlainTextResponse("pong")


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(api_router)
    return app


if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app=app, host="0.0.0.0", port=8000)
