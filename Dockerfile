FROM ghcr.io/astral-sh/uv:python3.13-alpine3.23 AS builder
WORKDIR /app
COPY . /app/

RUN uv build
#RUN pip install /app/dist/arithmp-0.1.0-py3-none-any.whl


FROM python:3.13-alpine
COPY --from=builder /app/dist/*.whl /tmp/
RUN pip install /tmp/*.whl
ENTRYPOINT ["arithmp"]