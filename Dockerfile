FROM python:3

RUN apt-get update &&\
	/usr/local/bin/python3 -m pip install --upgrade pip &&\
	/usr/local/bin/python3 -m pip install --upgrade setuptools &&\
	adduser myuser

ENV PATH="/home/myuser/.local/bin: ${PATH}"
ENV QR_CODE_IMAGE_DIRECTORY="images"
ENV QR_CODE_DEFAULT_URL = "https://www.njit.edu"
ENV QR_CODE_DEFAULT_FILENAME="default.png"

WORKDIR /home/myuser
COPY --chown=myuser:user . .
RUN pip3 install -r requirements.txt

ENTRYPOINT ["runuser", "-u", "myuser", "--", "python3"]
CMD ["main.py"]