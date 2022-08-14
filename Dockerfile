FROM python:3.9-slim
WORKDIR /binary-and-categorical-data-classifier-using-q-analysis
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]