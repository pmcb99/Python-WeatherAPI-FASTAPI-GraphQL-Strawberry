from config.config import DevConfig
import uvicorn
from src.app import create_app

app= create_app()

if __name__ == "__main__":
    print("Starting server...")
    uvicorn.run("main:app", reload=True)