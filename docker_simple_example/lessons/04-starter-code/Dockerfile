FROM python:3.8-slim

WORKDIR /usr/service/grade-submission-application

COPY . .

RUN pip install -r grade-submission/requirements.txt

EXPOSE 5000

CMD ["python", "grade-submission/app.py"]
