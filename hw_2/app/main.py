"""FastAPI application module."""

import os

import uvicorn
from fastapi import FastAPI

from . import routers
from . import crud


app = FastAPI(
    title="Homework 2",
    description="Homework for the ITMO course Python Backend",
    contact={"name": "BITLIFASON", "url": "https://github.com/BITLIFASON"},
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/docs/redoc",
)

app.include_router(routers.router)

if __name__ == "__main__":
    DB_PATH = "../data/database.sqlite"

    if not os.path.exists(DB_PATH):
        crud.create_db()

    host = "127.0.0.1"
    port = 80
    uvicorn.run(app, host=host, port=port)
