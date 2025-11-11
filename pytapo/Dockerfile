ARG BUILD_FROM=ghcr.io/hassio-addons/base-python:3.11
FROM ${BUILD_FROM}

# Install pytapo
RUN pip install --no-cache-dir pytapo

# Copy files
COPY run.sh /run.sh
COPY pytapo_script.py /pytapo_script.py
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
