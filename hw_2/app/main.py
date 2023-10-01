import os

import uvicorn
from fastapi import FastAPI

from routers import router
from crud import create_db

# Creating an "instance" of the class FastAPI
app = FastAPI(
    title="Homework 2",
    description="Homework for the ITMO course Python Backend",
    contact={
        "name": "BITLIFASON",
        "url": "https://github.com/BITLIFASON"
    },
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/docs/redoc"
)

# Include routers
app.include_router(router)

if __name__ == "__main__":

    DB_PATH = "../data/database.sqlite"

    if not os.path.exists(DB_PATH):
        create_db()

    host = "127.0.0.1"
    port = 80
    uvicorn.run(app, host=host, port=port)
