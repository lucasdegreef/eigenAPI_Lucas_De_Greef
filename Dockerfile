FROM python:3.10.0-alpine
RUN apk add build-base linux-headers
RUN python -m pip install psutil
WORKDIR /code
EXPOSE 8000
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
CMD ["uvicorn", "app.apiLucas:app", "--host", "0.0.0.0", "--port", "8000"]
