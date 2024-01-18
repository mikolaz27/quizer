FROM python:3.12-rc-slim

RUN apt update && python --version && mkdir "/docker_example"

WORKDIR /docker_example

COPY ./hello_world_from_docker.py ./hello_world_from_docker_in_container.py
COPY ./requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip && pip install -r ./requirements.txt

CMD ["python", "hello_world_from_docker_in_container.py"]