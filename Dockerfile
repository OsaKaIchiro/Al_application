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


# poetryの定義ファイルをコピー (存在する場合)
COPY pyproject.toml* poetry.lock* ./

# poetryでライブラリをインストール (pyproject.tomlが既にある場合)
RUN poetry config virtualenvs.in-project true
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi

COPY ./app /app/app


ENTRYPOINT ["sh", "-c", "poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"]