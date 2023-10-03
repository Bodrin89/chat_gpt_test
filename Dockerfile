FROM python:3.10-slim

WORKDIR /code
COPY requirements.txt /code/
RUN  pip install -r requirements.txt

COPY . .

ENTRYPOINT ["bash", "entrypoint.sh"]

EXPOSE 8087

CMD ["gunicorn", "chat_gpt.wsgi", "-w", "4", "-b", "0.0.0.0:8087"]
