from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from cricapi import get_matches

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/matches")
async def matches():
    return get_matches()
