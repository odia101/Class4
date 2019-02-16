FROM ubuntu:16.04
MAINTAINER Odia <Webpage>

RUN apt-get update
RUN cat /etc/lsb-release

#RUN apt-get install -y python
RUN apt-get install -y python3-pip
# Install: python3 instead of python2 (if its not 3 already)
# Install: pip (python package installer) for the corresponding Python3
# Use pip to install: numpy, pandas

WORKDIR ./
COPY our_csv_parser.py .
COPY housing.data.txt .
CMD ["python3", "our_csv_parser.py"]
