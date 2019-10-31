FROM python:3
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV PYTHONPATH "${PYTHONPATH}:./"
CMD ["python3","src/main.py"]