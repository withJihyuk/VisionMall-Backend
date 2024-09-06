## FastAPI-TEMPLATE

개인적으로 대회, 프로젝트 등에서 사용하기 위해서 제작 되었습니다.

- 구글 로그인
- 기본 CRUD 엔드포인트
- FastAPI / Prisma + PostgreSQL

### 사용법
아래의 명령어를 순서대로 입력 하시면 됩니다.   
기재되어 있진 않지만 가상환경 설정을 권장합니다.

```commandline
export SECRET_KEY=(본인의 값)
export ALGORITHM=(본인의 값)
export GOOGLE_CLIENT_ID=(본인의 값)
export GOOGLE_REDIRECT_URI=(본인의 값)
export GOOGLE_REDIRECT_URL=(본인의 값)
export DB_URL=(본인의 값)=(본인의 값)
```

```commandline
pip install -r requirements.txt
prisma push
prisma migrate dev --name init
python3 -m uvicorn main:app --reload
```

## To-Do

- 인증된 라우팅 경로 구현하기
- Refresh Token 저장하기