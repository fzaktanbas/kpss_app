from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "KPSS App Backend çalışıyor!"}