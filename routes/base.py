from fastapi import FastApi , APIRouter

base_router = APIRouter()

@base_router.get("/")
def welcome() :
    return {
        "message": "Welcome to the API"
    }