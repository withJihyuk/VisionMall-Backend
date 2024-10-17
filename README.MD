## VisionMall-Backend

```commandline
export SECRET_KEY=(본인의 값)
export ALGORITHM=(본인의 값)
export GOOGLE_CLIENT_ID=(본인의 값)
export GOOGLE_REDIRECT_URI=(본인의 값)
export GOOGLE_REDIRECT_URL=(본인의 값)
export DB_URL=(본인의 값)
export GPT_API_KEY=(본인의 값)
```

```commandline
docker-compose up -d
docker-compose down
```

### TO-DO
- Entity를 직접적으로 반환하고 있어서 좋지 않음. 이를 DTO를 사용하여 리팩토링 해야함
- 데이터베이스 구조 개선 필요. prisma 파일 주석 참고하기
- 완성하지 않은 기능 제작