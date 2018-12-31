FROM python:3.6-slim-stretch
RUN apt-get update && \
	apt-get install -y python3-dev gcc git && \
	rm -rf /var/lib/apt/lists/*
RUN pip install uvicorn
ADD app.py .

EXPOSE 8000

CMD uvicorn app:App --host 0.0.0.0 --port 8000
