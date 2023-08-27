# プロパティリスティングプロセッサ

このプロジェクトは、OpenAIの関数呼び出し機能を使用して不規則なプロパティ情報を処理することを示すためのものです。このプロジェクトは、ほぼ全てがChatGPT-4とツールAider(https://github.com/paul-gauthier/aider)を使用してコード生成されています。

## セットアップと実行

```bash
# プロジェクトディレクトリに移動し、仮想環境を作成します
python3 -m venv venv

# 仮想環境をアクティブにします
source venv/bin/activate

# 必要なパッケージをインストールします
pip install -r requirements.txt

# Streamlitアプリを実行します
streamlit run app.py
```

アプリは `http://localhost:8501` で利用可能です。
