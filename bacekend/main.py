from fastapi import FastAPI

from base import engine, Base

app = FastAPI()

Base.metadata.create_all(engine)