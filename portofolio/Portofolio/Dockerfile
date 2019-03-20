FROM python:3.6.7
MAINTAINER Rizky "rizky@alphatech.id"
RUN mkdir -p /demo
COPY . /demo
RUN pip install -r /demo/requirements.txt
WORKDIR /demo
ENTRYPOINT ["python"]
CMD ["portofolio.py"]
