FROM python:3.11-slim

RUN mkdir /app
COPY requirements.txt /app/
COPY *.py /app/
COPY run.sh /app/
RUN chmod u+x /app/run.sh

RUN pip install --no-cache-dir -r /app/requirements.txt

# Force script to store everything in sub-directory
ENV MARKDOWN_DIR=/app/data

WORKDIR /app
CMD ["/app/run.sh"]
