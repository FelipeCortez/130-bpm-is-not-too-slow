FROM continuumio/miniconda3:4.5.4

RUN mkdir /code

WORKDIR /code

ADD requirements.txt /code/

ADD src /code/

RUN apt-get update && apt-get install -y gcc libc-dev libffi-dev

RUN conda update --all --quiet --yes && \
    conda clean -tipsy
RUN python3.6 -m pip install -r requirements.txt --no-cache-dir

ENTRYPOINT ["/opt/conda/bin/python3.6"]
