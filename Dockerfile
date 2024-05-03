FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# EXPOSE 4003 -- No needed but an option

ENV NAME World

CMD ["python", "bot.py"]
