FROM python:alpine3.7 
COPY . /app
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt 
EXPOSE 5000 
ENTRYPOINT ["python"]
CMD ["api.py"]
