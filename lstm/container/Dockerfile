FROM ubuntu:16.04

MAINTAINER Francisco Blaya <fcoblaya@gmail.com>

RUN apt-get -y update && apt-get install -y --no-install-recommends \
         wget \
         python \
         nginx \
         ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py
RUN pip install numpy==1.13.3
RUN pip install scipy
RUN pip install scikit-learn
RUN pip install pandas
RUN pip install flask
RUN pip install gevent
RUN pip install gunicorn
RUN pip install tensorflow==1.12.0
RUN pip install keras
RUN (cd /usr/local/lib/python2.7/dist-packages/scipy/.libs; rm *; ln ../../numpy/.libs/* .)
RUN rm -rf /root/.cache

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"

COPY files /opt/program
WORKDIR /opt/program
