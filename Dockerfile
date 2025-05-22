FROM python: 3.12-slim

WORKDIR /app

COPY . . 

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP = app:create_app

CMD ["gunicorn", "-b", ""
