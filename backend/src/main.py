from contextlib import asynccontextmanager
from fastapi import FastAPI
from initial_data import init_db
from api import transactions, summary


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Initialize database
    init_db()
    yield
    # Shutdown: Add cleanup logic here if needed


app = FastAPI(lifespan=lifespan)

app.include_router(transactions.router)
app.include_router(summary.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Expense Tracker API"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
