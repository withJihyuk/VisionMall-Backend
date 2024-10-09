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
pip install -r requirements.txt
prisma db push
python3 main.py
```