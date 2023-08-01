# AI チャットアプリをデプロイしよう

ホスティング先を選定して、Web に公開する

記事では、Streamlit Cloud を利用しているが、記事内にも書かれている通り、実用上は GCP（Google Cloud Platform）等へホスティングしたいところ

その場合は、GCE（Google Compute Engine） でインスタンスを立ち上げて Debian + nginx + Rails とか、もしくは GAE か。。

## Streamlit Cloud とは？

Streamlit Cloud は、Streamlit アプリケーションを簡単に WEB 上で公開し、共有できるサービスです。Streamlit Cloud に登録し、コードを GitHub レポジトリにプッシュするだけで、アプリケーションをデプロイすることができます。

### 全体のプロセスについて

- Streamlit Cloud への登録
- アプリケーションのコードと依存関係を GitHub レポジトリに Push する
- 必要に応じて設定ファイルを修正してアプリの設定をカスタマイズする
- Streamlit Cloud を使用して、直接 GitHub レポジトリからアプリをデプロイします。
- アプリの起動をしばし待つ
- アプリの起動が確認できれば、共有用 URL を利用してアプリを共有しましょう
  - 必要に応じてこの URL はカスタマイズすることも可能です

## Github のリポジトリが必要
