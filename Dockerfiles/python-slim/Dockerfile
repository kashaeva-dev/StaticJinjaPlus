FROM python:3.12-slim-bookworm
RUN apt-get update && apt-get install -y git
ARG VERSION=
RUN git clone https://github.com/MrDave/StaticJinjaPlus.git /StaticJinjaPlus && cd /StaticJinjaPlus && git checkout $VERSION
WORKDIR /StaticJinjaPlus/
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "main.py"]
CMD ["--help"]
