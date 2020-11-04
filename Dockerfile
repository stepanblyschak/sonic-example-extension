FROM python:3

ARG manifest

RUN pip install psutil

COPY cpu-report.py /usr/bin/cpu-report.py

COPY show.py /show.py

LABEL com.azure.sonic.manifest="$manifest"

ENTRYPOINT ["/usr/bin/cpu-report.py"]
