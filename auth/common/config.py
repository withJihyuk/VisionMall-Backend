import os

client_id = [os.environ.get("GOOGLE_CLIENT_ANDROID_ID"), os.environ.get("GOOGLE_CLIENT_IOS_ID")]
sentry_dsn = os.environ.get("SENTRY_DSN")