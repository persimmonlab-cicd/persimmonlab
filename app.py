import flask
import os

app = flask.Flask(__name__)

# 하드코딩된 비밀번호 (시크릿 노출 예)
SECRET_KEY = "my_super_secret_password"

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)  # 80 포트는 루트 권한이 필요할 수 있음