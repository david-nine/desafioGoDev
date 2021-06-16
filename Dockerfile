FROM python:3.8-slim-buster
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY start_bd.py start_bd.py
COPY inicializador.py /
CMD ["python3", "start_bd.py"]
COPY app/ /app
CMD ["python3", "/inicializador.py"]
EXPOSE 5000
