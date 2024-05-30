FROM ubuntu:22.04
RUN apt-get update && apt-get install -y python3 python3-pip git && apt-get clean
ARG VERSION=main
RUN git clone https://github.com/MrDave/StaticJinjaPlus.git /StaticJinjaPlus && cd /StaticJinjaPlus && git checkout $VERSION
WORKDIR /StaticJinjaPlus/
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "main.py"]
CMD ["--help"]