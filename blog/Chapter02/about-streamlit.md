# Streamlit

## Streamlit とは

web アプリをすばやく作成・共有するための Python ベースの OSS フレームワーク

## Streamlit のインストール

```sh
# install
pip install streamlit

# 正常にインストールされたことの確認
streamlit hello
```

PATH のワーニングがでる

```sh
WARNING: The scripts f2py, f2py3 and f2py3.9 are installed in '/Users/encoolus/Library/Python/3.9/bin' which is not on PATH.
Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
WARNING: The script pygmentize is installed in '/Users/encoolus/Library/Python/3.9/bin' which is not on PATH.
Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
WARNING: The script markdown-it is installed in '/Users/encoolus/Library/Python/3.9/bin' which is not on PATH.
Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
WARNING: The script jsonschema is installed in '/Users/encoolus/Library/Python/3.9/bin' which is not on PATH.
Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
WARNING: The script normalizer is installed in '/Users/encoolus/Library/Python/3.9/bin' which is not on PATH.
Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
WARNING: The script streamlit is installed in '/Users/encoolus/Library/Python/3.9/bin' which is not on PATH.
Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
```

あとはバージョンのワーニングがでる。バージョンアップするか検討

```sh
WARNING: You are using pip version 21.2.4; however, version 23.2.1 is available.
You should consider upgrading via the '/Library/Developer/CommandLineTools/usr/bin/python3 -m pip install --upgrade pip' command.
```

一旦 hello してみる

```sh
streamlit hello

zsh: command not found: streamlit
```

PATH 通ってないね

とりあえず、推奨されていたやつをやってみよう

```sh
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

この３行。とりあえず ~/.zshrc に書いてみる

ターミナルを再起動する

もう一度

```sh
streamlit hello
zsh: command not found: streamlit
```

うん。関係なさそう. だが今後 pyenv 利用予定なので設定は残しておく

指示通りに設定する

`~/.zshrc`

```sh
# Streamlitなどのライブラリ用に設定
export PATH=$PATH:/Users/encoolus/Library/Python/3.9/bin
```

ターミナルを再起動する

```sh
streamlit hello

      👋 Welcome to Streamlit!

      If you’d like to receive helpful onboarding emails, news, offers, promotions,
      and the occasional swag, please enter your email address below. Otherwise,
      leave this field blank.

      Email:
```

とのことで無事に動いた 空のままエンター

ブラウザに表示が来た

```sh
/Users/encoolus/Library/Python/3.9/lib/python/site-packages/urllib3/__init__.py:34: NotOpenSSLWarning: urllib3 v2.0 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(

  You can find our privacy policy at https://streamlit.io/privacy-policy

  Summary:
  - This open source library collects usage statistics.
  - We cannot see and do not store information contained inside Streamlit apps,
    such as text, charts, images, etc.
  - Telemetry data is stored in servers in the United States.
  - If you'd like to opt out, add the following to ~/.streamlit/config.toml,
    creating that file if necessary:

    [browser]
    gatherUsageStats = false


  Welcome to Streamlit. Check out our demo in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.53:8501

  Ready to create your own Python apps super quickly?
  Head over to https://docs.streamlit.io

  May you create awesome apps!


  For better performance, install the Watchdog module:

  $ xcode-select --install
  $ pip install watchdog
```

てことで、xcode-select と watchdog はインストールしたほうがいいらしい

一旦止めておく

Ctrl + C

```sh
xcode-select --install

xcode-select: error: command line tools are already installed, use "Software Update" in System Settings to install updates
```

すでに入ってました^^;

```sh
pip install watchdog

Defaulting to user installation because normal site-packages is not writeable
Collecting watchdog
  Downloading watchdog-3.0.0-cp39-cp39-macosx_11_0_arm64.whl (91 kB)
     |████████████████████████████████| 91 kB 4.5 MB/s
Installing collected packages: watchdog
Successfully installed watchdog-3.0.0
WARNING: You are using pip version 21.2.4; however, version 23.2.1 is available.
You should consider upgrading via the '/Library/Developer/CommandLineTools/usr/bin/python3 -m pip install --upgrade pip' command.
```

こっちは入ってなかった。

pip のアップグレードが再度表示
ちょっと調べるか

少し様子見することに。（v23 が July/2023 リリースだった）

## Hello world on Streamlit

簡単なアプリをつくって見てみる

`00_my_first_app.py`ファイルを作成する

```py
import streamlit as st
st.write("Hello world. Let's learn how to build a AI-based app together.")
```

下記コマンドで走らせてみる

```sh
streamlit run 00_my_first_app.py
```

無事にブラウザに表示された。
