# Flask CRUD 웹앱

이 프로젝트는 Flask와 SQLite를 기반으로 한 간단한 사용자 정보 관리 웹 애플리케이션입니다.

--- 

## 📌 주요 기능
- 사용자 등록 (이름, 나이, 취미)
- 사용자 목록 조회
- 사용자 정보 수정 (ID 기반)
- 사용자 정보 삭제

--- 

## 🏗 폴더 구조
--- 
PythonStudy/
├── app.py
├── templates/
│ ├── home.html
│ ├── users.html
│ └── edit.html
├── users.db
└── README.md
---

## ▶️ 실행 방법
```
1. 프로젝트 클론 또는 다운로드:
git clone https://github.com/jmineeekim/flask-crud-app.git
cd flask-crud-app
2. 가상환경(optional) 생성:
python -m venv venv
source venv/bin/activate  # Windows는 venv\Scripts\activate
3. 필요한 패키지 설치:
pip install -r requirements.txt
4. 웹 서버 실행:
python app.py
5. 브라우저에서 접속:
http://127.0.0.1:5000
```

## 💡 사용 기술

- Python 3.x
- Flask
- Flask-SQLAlchemy
- SQLite

# 📝 작성자
- jmineeekim