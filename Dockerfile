# python3.9のイメージをダウンロード
FROM python:3.9-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /src

# pipを使ってpoetryをインストール
RUN pip install poetry

# poetryの定義ファイルをコピー
COPY pyproject.toml poetry.lock ./

# poetryでライブラリをインストール (pyproject.tomlが存在する場合)
RUN poetry config virtualenvs.in-project true
RUN poetry install --no-root


# uvicornのサーバーを立ち上げる
ENTRYPOINT ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]