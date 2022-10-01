FROM python:3

RUN git clone https://github.com/santidotpy/roman.git

WORKDIR /roman

RUN pip install -r requirements.txt

CMD ["python3", "test_romanos.py"]