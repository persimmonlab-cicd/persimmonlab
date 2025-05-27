FROM python:3.6  # EOL 버전, 보안 업데이트 없음

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

# root 권한으로 실행 (misconfiguration 예시)
CMD ["python", "app.py"]