from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "환경 구축 완료"}