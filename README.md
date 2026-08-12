# 📚 도서 관리 웹 서비스 (Book Management App)

FastAPI와 순수 프론트엔드(HTML/JavaScript)를 활용해 만든 간단한 도서 관리 및 검색 웹 애플리케이션입니다.

---

## 🚀 주요 기능
- **도서 목록 조회**: 등록된 전체 도서 목록을 네이버 스타일의 깔끔한 UI로 확인 (`/static/02-list.html`)
- **도서 상세 조회**: 특정 도서의 상세 정보 확인 (`/static/03-detail.html`)
- **도서 키워드 검색**: 원하는 키워드로 도서 제목 검색 기능 (`/static/04-search.html`)

---

## 🛠️ 기술 스택
- **Backend**: Python, FastAPI, Uvicorn
- **Frontend**: HTML5, CSS3, JavaScript (Fetch API)

---

## ⚙️ 상세 실행 가이드 (How to Run)

프로젝트를 처음 다운받았거나 터미널을 새로 켰을 때, 아래 순서대로 정확히 입력해 주세요.

### 1. 프로젝트 폴더로 이동하기
터미널을 열고 본인의 프로젝트 경로로 이동합니다.
```powershell
-cd C:\Users\Playdata\study\app-dev
-python -m venv .venv
-.venv\Scripts\Activate.ps1
-pip install fastapi uvicorn
-.venv\Scripts\python.exe main.py

5. 웹 브라우저에서 확인하기
크롬이나 엣지 브라우저를 켜고 아래 주소로 접속합니다.

도서 목록 페이지: http://127.0.0.1:8000/static/02-list.html

도서 검색 페이지: http://127.0.0.1:8000/static/04-search.html