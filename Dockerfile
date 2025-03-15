FROM python:3.11

WORKDIR /app
FROM python:3.11

WORKDIR /app

# 必要なシステムパッケージをインストール
RUN apt-get update && apt-get install -y curl git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Poetryをダウンロードしてインストール
RUN curl -sSL https://install.python-poetry.org | python -

# Pathを通す
ENV PATH /root/.local/bin:$PATH
# 仮想環境をたてない
RUN poetry config virtualenvs.create false

# アプリケーションの依存関係をインストール
COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-root

COPY ./app /app/app

ENTRYPOINT ["sh", "-c", "poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"]