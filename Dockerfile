FROM python
EXPOSE 8888
COPY ./bot.py bot.py
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD ["python", "bot.py"]