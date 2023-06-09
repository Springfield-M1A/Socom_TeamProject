# Contributor

---
# Project

---
# Install
1. 본 프로젝트를 클론 받은 후, 터미널 또는 명령 프롬프트에서 프로젝트 디렉토리로 이동
2. 터미널 또는 명령프롬프트를 통해 가상 환경 생성, 활성화
    ```
    Windows :
    python -m venv venv
    venv\Scripts\activate
    ```
    ```
    macOS / Linux :
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Requirements 를 통한 종속성 프로그램 설치
    ```
    pip install -r requirements.txt
    ```
4. 개발 서버 실행
    ```
    python manage.py migrate
    python manage.py runserver
    ```
