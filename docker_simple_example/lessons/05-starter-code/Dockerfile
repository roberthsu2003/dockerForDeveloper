FROM python:3.8-slim

WORKDIR /usr/src/

COPY . .

RUN pip install -r flask-mysql/requirements.txt

EXPOSE 3000

CMD ["python", "flask-mysql/app.py"]