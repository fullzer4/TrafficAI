FROM python:3.9.16

WORKDIR /api

RUN pip install flask flask_cors

COPY . .

CMD ["python", "index.py"]

EXPOSE 3000:3000