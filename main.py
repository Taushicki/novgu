import uvicorn
from api.__init__ import create_app

app = create_app()

if __name__ == "__main__":
    try:
        uvicorn.run(app, host="0.0.0.0", port=8000)
    except KeyboardInterrupt:
        print("Serer is stoped")
