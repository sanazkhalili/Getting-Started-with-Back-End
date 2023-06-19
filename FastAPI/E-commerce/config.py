from fastapi import FastAPI
from routers import urls_endpoint

app = FastAPI()
app.include_router(urls_endpoint.router, tags=['test'])