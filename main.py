from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# 1. FastAPI 인스턴스를 먼저 생성해야 합니다!
app = FastAPI()

# 2. 그 다음에 app을 사용하는 기능을 적어줍니다.
app.mount("/static", StaticFiles(directory="static"), name="static")

books = [
    {"id": 1, "title": "파이썬 입문", "author": "김철수", "year": 2021},
    {"id": 2, "title": "FastAPI 실전", "author": "이영희", "year": 2022},
    {"id": 3, "title": "파이썬 웹개발", "author": "김철수", "year": 2023},
    {"id": 4, "title": "데이터 분석 기초", "author": "박민수", "year": 2021},
    {"id": 5, "title": "FastAPI로 배우는 백엔드", "author": "이영희", "year": 2023}
]

@app.get("/")
def read_root():
    return {"message": "Hello World!!!"}

@app.get("/health")
def health():
    return {"status": "health"}

@app.get("/info")
def info():
    return {"name": "도서관리API", "version": "0.1.0"}

@app.get("/books")
def get_books():
    return books

@app.get("/books/search")
def search_books(keyword: str):
    filtered_books = [book for book in books if keyword in book["title"]]
    return filtered_books

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    return {"error": "Book not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)