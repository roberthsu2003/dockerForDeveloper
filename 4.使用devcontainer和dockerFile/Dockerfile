FROM mcr.microsoft.com/devcontainers/python:1-3.10-bookworm

WORKDIR /code

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./src ./src

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]



