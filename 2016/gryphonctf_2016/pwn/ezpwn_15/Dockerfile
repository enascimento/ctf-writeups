FROM ubuntu

COPY get_magic.c /
COPY script.py /

RUN ["apt-get", "update"]
RUN ["apt-get", "-y", "install", "python", "build-essential"]
RUN ["gcc", "-o", "get_magic", "get_magic.c"]

CMD ["./script.py"]