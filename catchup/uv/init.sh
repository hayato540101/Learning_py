# uv_init.sh
export UV_LINK_MODE=copy

curl -LsSf https://astral.sh/uv/install.sh | sh
exec $SHELL -l
uv version

uv init test-project && cd test-project
uv venv
uv python install 3.12.8
uv python list
uv python pin 3.12.8

# 開発用パッケージをインストール
uv add --dev ruff

# パッケージをインストール
uv add pandas

# 一時的にパッケージをインストール
uv run --with requests hello.py
uv run --with pandas hello.py

# スクリプトを実行
uv run hello.py

