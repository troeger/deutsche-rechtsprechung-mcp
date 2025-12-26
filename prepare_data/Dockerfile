FROM python:3.11-slim

RUN mkdir /app
COPY requirements.txt /app/
COPY *.py /app/
COPY run.sh /app/
RUN chmod u+x /app/run.sh

RUN pip install --no-cache-dir -r /app/requirements.txt

# Force last script to still store everything in the data sub-directory
# This is needed for having a shared volume between the crawl
# and the server docker image in Kubernetes
ENV MARKDOWN_DIR=/app/data

WORKDIR /app
CMD ["/app/run.sh"]
