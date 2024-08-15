FROM python:3.12-slim
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY sprint_1/src ./
EXPOSE 8000
CMD ["chainlit", "run", "app.py"]