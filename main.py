from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
  data = {
    "Hello": "Mars"
  }

  return data