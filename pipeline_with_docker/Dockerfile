FROM python:3.10-bookworm

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt
COPY ./export_var.sh /app/export_var.sh
COPY ./run_etl_pipeline.py /app/run_etl_pipeline.py

COPY ./extract.py /app/extract.py

COPY ./load.py /app/load.py

COPY ./transform.py /app/transform.py
# RUN chmod +x /app/export_var.sh 
# RUN  /bin/sh -c "/app/export_var.sh"

# RUN source /root/.bashrc


ENTRYPOINT ["python", "run_etl_pipeline.py"]



