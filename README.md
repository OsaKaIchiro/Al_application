# （仮）ウェブアプリケーション名

このリポジトリは、未来の出来事について投資を行う場を提供するウェブアプリケーションです。

## ディレクトリ構造

├── app  
│   ├── init.py  
│   ├── main.py  
│   ├── schemas  
│   │   ├── init.py  
│   │   └── task.py  
│   ├── routers  
│   │   ├── init.py  
│   │   └── task.py  
│   ├── models  
│   │   ├── init.py  
│   │   └── task.py  
│   ├── cruds  
│   │   ├── init.py  
│   │   └── task.py  
│   ├── templates  
│   │   ├── log_in_page.html  
│   │   ├── home.html  
│   │   ├── ranking.html  
│   │   ├── practice_mode.html  
│   │   └── casual_mode.html  
│   └── static  
│       ├── css  
│       │   ├── log_in_page.css  
│       │   ├── home.css  
│       │   ├── ranking.css  
│       │   ├── practice_mode.css  
│       │   └── casual_mode.css  
│       └── js  
│           ├── home.js  
│           ├── ranking.js  
│           ├── practice_mode.js  
│           ├── casual_mode.js  
├── docker-compose.yml  
├── poetry.lock  
├── pyproject.toml  
└── Dockerfile  


* `app/`: アプリケーションのソースコード
    * `schemas/`: Pydanticスキーマ
    * `routers/`: FastAPIルーター
    * `models/`: SQLAlchemyモデル
    * `cruds/`: データベース操作
    * `templates/`: HTMLテンプレート
    * `static/`: 静的ファイル（CSS、JavaScript）
* `docker-compose.yml`: Docker Compose設定ファイル
* `poetry.lock`: Poetryロックファイル
* `pyproject.toml`: Poetry設定ファイル
* `Dockerfile`: Dockerファイル

## 技術スタック

* FastAPI
* SQLAlchemy
* Pydantic
* Poetry
* Docker

## 開発環境の構築

1.  リポジトリをクローンします。
    
    ```bash
    git clone （仮）リポジトリのURL
    cd （仮）リポジトリ名
    ```
    
2.  Poetryを使用して依存関係をインストールします。
    
    ```bash
    poetry install
    ```
    
3.  Dockerを使用してアプリケーションを実行します。
    
    ```bash
    docker-compose up --build
    ```

## アプリケーションの使い方

1.  ブラウザで`http://localhost`にアクセスします。
2.  -（仮）アプリケーションの使い方
    - カジュアルモードの説明
    - プラクティスモードの説明
    - その他の説明
## 今後の開発予定（仮）

* [機能1]
* [機能2]
* [機能3]

## 貢献

コントリビューションは大歓迎です！バグ報告や機能提案は、GitHubのIssueまたはプルリクエストを通じて運営へお寄せください。

## ライセンス

このプロジェクトは[ライセンス名]ライセンスの下で公開されています。

## 著者

* 江藤拓海
* 逢坂一郎ダニエル
* 萩原こう
* 堤円花

## 連絡先

* taku810616@gmail.com

## その他（仮）

* [その他、アプリケーションに関する情報]
