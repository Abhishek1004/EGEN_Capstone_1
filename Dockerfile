FROM python>=3.6.8

COPY . /Users/Abhishek/Desktop/Egen_Module1_Capstone/DockerFile

WORKDIR /Users/Abhishek/Desktop/Egen_Module1_Capstone/DockerFile

RUN pip install -r requirements.txt

CMD ["python3","publish.py"]