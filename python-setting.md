# M2 Mac に Python をインストールして利用できるようにする

## 方針

- Anaconda は入れない
- Homebrew 経由で入れる
- pyenv で入れる

### References

- [Mac で VSCode+pyenv+venv+pip を使い、Python の開発環境を構築する](https://zenn.dev/sion_pn/articles/d0f9e45716cabb)
- [【Mac 大手術】ぐちゃぐちゃだった Python の環境構築をやり直した話【さよなら Anaconda】](https://qiita.com/mohki7/items/88e3f5f3428744ff3473)
- [macOS の zsh ではこれだけはやっておこう](https://zenn.dev/sprout2000/articles/bd1fac2f3f83bc)

## 環境構築

> pyenv で python 3.11 あたりをインストールすると、上記のようなエラーが発生するので、あらかじめ Homebrew から xz をインストールしておきます。

とのことなので、xz のインストールから始める

```sh
brew install xz
```

pyenv をインストール

```sh
brew install pyenv
```

パスは事前に参考記事から zsh の設定をしている
一応確認

```sh
pyenv --version

pyenv 2.3.23
```

大丈夫。通ってる。

バージョンの一覧を確認する

```sh
pyenv install --list
```

山程出てくる。。。どうすべきか

```sh
Available versions:
  2.1.3
  2.2.3
  2.3.7
  2.4.0
  2.4.1
  2.4.2
  2.4.3
  2.4.4
  2.4.5
  2.4.6
  2.5.0
  2.5.1
  2.5.2
  2.5.3
  2.5.4
  2.5.5
  2.5.6
  2.6.0
  2.6.1
  2.6.2
  2.6.3
  2.6.4
  2.6.5
  2.6.6
  2.6.7
  2.6.8
  2.6.9
  2.7.0
  2.7-dev
  2.7.1
  2.7.2
  2.7.3
  2.7.4
  2.7.5
  2.7.6
  2.7.7
  2.7.8
  2.7.9
  2.7.10
  2.7.11
  2.7.12
  2.7.13
  2.7.14
  2.7.15
  2.7.16
  2.7.17
  2.7.18
  3.0.1
  3.1.0
  3.1.1
  3.1.2
  3.1.3
  3.1.4
  3.1.5
  3.2.0
  3.2.1
  3.2.2
  3.2.3
  3.2.4
  3.2.5
  3.2.6
  3.3.0
  3.3.1
  3.3.2
  3.3.3
  3.3.4
  3.3.5
  3.3.6
  3.3.7
  3.4.0
  3.4-dev
  3.4.1
  3.4.2
  3.4.3
  3.4.4
  3.4.5
  3.4.6
  3.4.7
  3.4.8
  3.4.9
  3.4.10
  3.5.0
  3.5-dev
  3.5.1
  3.5.2
  3.5.3
  3.5.4
  3.5.5
  3.5.6
  3.5.7
  3.5.8
  3.5.9
  3.5.10
  3.6.0
  3.6-dev
  3.6.1
  3.6.2
  3.6.3
  3.6.4
  3.6.5
  3.6.6
  3.6.7
  3.6.8
  3.6.9
  3.6.10
  3.6.11
  3.6.12
  3.6.13
  3.6.14
  3.6.15
  3.7.0
  3.7-dev
  3.7.1
  3.7.2
  3.7.3
  3.7.4
  3.7.5
  3.7.6
  3.7.7
  3.7.8
  3.7.9
  3.7.10
  3.7.11
  3.7.12
  3.7.13
  3.7.14
  3.7.15
  3.7.16
  3.7.17
  3.8.0
  3.8-dev
  3.8.1
  3.8.2
  3.8.3
  3.8.4
  3.8.5
  3.8.6
  3.8.7
  3.8.8
  3.8.9
  3.8.10
  3.8.11
  3.8.12
  3.8.13
  3.8.14
  3.8.15
  3.8.16
  3.8.17
  3.9.0
  3.9-dev
  3.9.1
  3.9.2
  3.9.4
  3.9.5
  3.9.6
  3.9.7
  3.9.8
  3.9.9
  3.9.10
  3.9.11
  3.9.12
  3.9.13
  3.9.14
  3.9.15
  3.9.16
  3.9.17
  3.10.0
  3.10-dev
  3.10.1
  3.10.2
  3.10.3
  3.10.4
  3.10.5
  3.10.6
  3.10.7
  3.10.8
  3.10.9
  3.10.10
  3.10.11
  3.10.12
  3.11.0
  3.11-dev
  3.11.1
  3.11.2
  3.11.3
  3.11.4
  3.12.0b4
  3.12-dev
  3.13-dev
  activepython-2.7.14
  activepython-3.5.4
  activepython-3.6.0
  anaconda-1.4.0
  anaconda-1.5.0
  anaconda-1.5.1
  anaconda-1.6.0
  anaconda-1.6.1
  anaconda-1.7.0
  anaconda-1.8.0
  anaconda-1.9.0
  anaconda-1.9.1
  anaconda-1.9.2
  anaconda-2.0.0
  anaconda-2.0.1
  anaconda-2.1.0
  anaconda-2.2.0
  anaconda-2.3.0
  anaconda-2.4.0
  anaconda-4.0.0
  anaconda2-2.4.0
  anaconda2-2.4.1
  anaconda2-2.5.0
  anaconda2-4.0.0
  anaconda2-4.1.0
  anaconda2-4.1.1
  anaconda2-4.2.0
  anaconda2-4.3.0
  anaconda2-4.3.1
  anaconda2-4.4.0
  anaconda2-5.0.0
  anaconda2-5.0.1
  anaconda2-5.1.0
  anaconda2-5.2.0
  anaconda2-5.3.0
  anaconda2-5.3.1
  anaconda2-2018.12
  anaconda2-2019.03
  anaconda2-2019.07
  anaconda2-2019.10
  anaconda3-2.0.0
  anaconda3-2.0.1
  anaconda3-2.1.0
  anaconda3-2.2.0
  anaconda3-2.3.0
  anaconda3-2.4.0
  anaconda3-2.4.1
  anaconda3-2.5.0
  anaconda3-4.0.0
  anaconda3-4.1.0
  anaconda3-4.1.1
  anaconda3-4.2.0
  anaconda3-4.3.0
  anaconda3-4.3.1
  anaconda3-4.4.0
  anaconda3-5.0.0
  anaconda3-5.0.1
  anaconda3-5.1.0
  anaconda3-5.2.0
  anaconda3-5.3.0
  anaconda3-5.3.1
  anaconda3-2018.12
  anaconda3-2019.03
  anaconda3-2019.07
  anaconda3-2019.10
  anaconda3-2020.02
  anaconda3-2020.07
  anaconda3-2020.11
  anaconda3-2021.04
  anaconda3-2021.05
  anaconda3-2021.11
  anaconda3-2022.05
  anaconda3-2022.10
  anaconda3-2023.03-0
  anaconda3-2023.03
  anaconda3-2023.03-1
  anaconda3-2023.07-0
  cinder-3.8-dev
  cinder-3.10-dev
  graalpy-22.3.0
  graalpy-23.0.0
  graalpython-20.1.0
  graalpython-20.2.0
  graalpython-20.3.0
  graalpython-21.0.0
  graalpython-21.1.0
  graalpython-21.2.0
  graalpython-21.3.0
  graalpython-22.0.0
  graalpython-22.1.0
  graalpython-22.2.0
  ironpython-dev
  ironpython-2.7.4
  ironpython-2.7.5
  ironpython-2.7.6.3
  ironpython-2.7.7
  jython-dev
  jython-2.5.0
  jython-2.5-dev
  jython-2.5.1
  jython-2.5.2
  jython-2.5.3
  jython-2.5.4-rc1
  jython-2.7.0
  jython-2.7.1
  jython-2.7.2
  mambaforge-pypy3
  mambaforge
  mambaforge-4.10.1-4
  mambaforge-4.10.1-5
  mambaforge-4.10.2-0
  mambaforge-4.10.3-0
  mambaforge-4.10.3-1
  mambaforge-4.10.3-2
  mambaforge-4.10.3-3
  mambaforge-4.10.3-4
  mambaforge-4.10.3-5
  mambaforge-4.10.3-6
  mambaforge-4.10.3-7
  mambaforge-4.10.3-8
  mambaforge-4.10.3-9
  mambaforge-4.10.3-10
  mambaforge-4.11.0-0
  mambaforge-4.11.0-1
  mambaforge-4.11.0-2
  mambaforge-4.11.0-3
  mambaforge-4.11.0-4
  mambaforge-4.12.0-0
  mambaforge-4.12.0-1
  mambaforge-4.12.0-2
  mambaforge-4.12.0-3
  mambaforge-4.13.0-1
  mambaforge-4.14.0-0
  mambaforge-4.14.0-1
  mambaforge-4.14.0-2
  mambaforge-22.9.0-0
  mambaforge-22.9.0-1
  mambaforge-22.9.0-2
  mambaforge-22.9.0-3
  micropython-dev
  micropython-1.9.3
  micropython-1.9.4
  micropython-1.10
  micropython-1.11
  micropython-1.12
  micropython-1.13
  micropython-1.14
  micropython-1.15
  micropython-1.16
  micropython-1.17
  micropython-1.18
  micropython-1.19.1
  miniconda-latest
  miniconda-2.2.2
  miniconda-3.0.0
  miniconda-3.0.4
  miniconda-3.0.5
  miniconda-3.3.0
  miniconda-3.4.2
  miniconda-3.7.0
  miniconda-3.8.3
  miniconda-3.9.1
  miniconda-3.10.1
  miniconda-3.16.0
  miniconda-3.18.3
  miniconda2-latest
  miniconda2-2.7-4.8.3
  miniconda2-3.18.3
  miniconda2-3.19.0
  miniconda2-4.0.5
  miniconda2-4.1.11
  miniconda2-4.3.14
  miniconda2-4.3.21
  miniconda2-4.3.27
  miniconda2-4.3.30
  miniconda2-4.3.31
  miniconda2-4.4.10
  miniconda2-4.5.1
  miniconda2-4.5.4
  miniconda2-4.5.11
  miniconda2-4.5.12
  miniconda2-4.6.14
  miniconda2-4.7.10
  miniconda2-4.7.12
  miniconda3-latest
  miniconda3-2.2.2
  miniconda3-3.0.0
  miniconda3-3.0.4
  miniconda3-3.0.5
  miniconda3-3.3.0
  miniconda3-3.4.2
  miniconda3-3.7.0
  miniconda3-3.7-4.8.2
  miniconda3-3.7-4.8.3
  miniconda3-3.7-4.9.2
  miniconda3-3.7-4.10.1
  miniconda3-3.7-4.10.3
  miniconda3-3.7-4.11.0
  miniconda3-3.7-4.12.0
  miniconda3-3.7-22.11.1-1
  miniconda3-3.7-23.1.0-1
  miniconda3-3.8.3
  miniconda3-3.8-4.8.2
  miniconda3-3.8-4.8.3
  miniconda3-3.8-4.9.2
  miniconda3-3.8-4.10.1
  miniconda3-3.8-4.10.3
  miniconda3-3.8-4.11.0
  miniconda3-3.8-4.12.0
  miniconda3-3.8-22.11.1-1
  miniconda3-3.8-23.1.0-1
  miniconda3-3.8-23.3.1-0
  miniconda3-3.8-23.5.0-3
  miniconda3-3.9.1
  miniconda3-3.9-4.9.2
  miniconda3-3.9-4.10.1
  miniconda3-3.9-4.10.3
  miniconda3-3.9-4.11.0
  miniconda3-3.9-4.12.0
  miniconda3-3.9-22.11.1-1
  miniconda3-3.9-23.1.0-1
  miniconda3-3.9-23.3.1-0
  miniconda3-3.9-23.5.0-3
  miniconda3-3.10.1
  miniconda3-3.10-22.11.1-1
  miniconda3-3.10-23.1.0-1
  miniconda3-3.10-23.3.1-0
  miniconda3-3.10-23.5.0-3
  miniconda3-3.11-23.5.0-3
  miniconda3-3.16.0
  miniconda3-3.18.3
  miniconda3-3.19.0
  miniconda3-4.0.5
  miniconda3-4.1.11
  miniconda3-4.2.12
  miniconda3-4.3.11
  miniconda3-4.3.14
  miniconda3-4.3.21
  miniconda3-4.3.27
  miniconda3-4.3.30
  miniconda3-4.3.31
  miniconda3-4.4.10
  miniconda3-4.5.1
  miniconda3-4.5.4
  miniconda3-4.5.11
  miniconda3-4.5.12
  miniconda3-4.6.14
  miniconda3-4.7.10
  miniconda3-4.7.12
  miniforge-pypy3
  miniforge3-latest
  miniforge3-4.9.2
  miniforge3-4.10
  miniforge3-4.10.1-1
  miniforge3-4.10.1-3
  miniforge3-4.10.1-5
  miniforge3-4.10.2-0
  miniforge3-4.10.3-0
  miniforge3-4.10.3-1
  miniforge3-4.10.3-2
  miniforge3-4.10.3-3
  miniforge3-4.10.3-4
  miniforge3-4.10.3-5
  miniforge3-4.10.3-6
  miniforge3-4.10.3-7
  miniforge3-4.10.3-8
  miniforge3-4.10.3-9
  miniforge3-4.10.3-10
  miniforge3-4.11.0-0
  miniforge3-4.11.0-1
  miniforge3-4.11.0-2
  miniforge3-4.11.0-3
  miniforge3-4.11.0-4
  miniforge3-4.12.0-0
  miniforge3-4.12.0-1
  miniforge3-4.12.0-2
  miniforge3-4.12.0-3
  miniforge3-4.13.0-0
  miniforge3-4.13.0-1
  miniforge3-4.14.0-0
  miniforge3-4.14.0-1
  miniforge3-4.14.0-2
  miniforge3-22.9.0-0
  miniforge3-22.9.0-1
  miniforge3-22.9.0-2
  miniforge3-22.9.0-3
  miniforge3-22.11.1-4
  nogil-3.9.10
  nogil-3.9.10-1
  pypy-c-jit-latest
  pypy-dev
  pypy-stm-2.3
  pypy-stm-2.5.1
  pypy-1.5-src
  pypy-1.6
  pypy-1.7
  pypy-1.8
  pypy-1.9
  pypy-2.0-src
  pypy-2.0
  pypy-2.0.1-src
  pypy-2.0.1
  pypy-2.0.2-src
  pypy-2.0.2
  pypy-2.1-src
  pypy-2.1
  pypy-2.2-src
  pypy-2.2
  pypy-2.2.1-src
  pypy-2.2.1
  pypy-2.3-src
  pypy-2.3
  pypy-2.3.1-src
  pypy-2.3.1
  pypy-2.4.0-src
  pypy-2.4.0
  pypy-2.5.0-src
  pypy-2.5.0
  pypy-2.5.1-src
  pypy-2.5.1
  pypy-2.6.0-src
  pypy-2.6.0
  pypy-2.6.1-src
  pypy-2.6.1
  pypy-4.0.0-src
  pypy-4.0.0
  pypy-4.0.1-src
  pypy-4.0.1
  pypy-5.0.0-src
  pypy-5.0.0
  pypy-5.0.1-src
  pypy-5.0.1
  pypy-5.1-src
  pypy-5.1
  pypy-5.1.1-src
  pypy-5.1.1
  pypy-5.3-src
  pypy-5.3
  pypy-5.3.1-src
  pypy-5.3.1
  pypy-5.4-src
  pypy-5.4
  pypy-5.4.1-src
  pypy-5.4.1
  pypy-5.6.0-src
  pypy-5.6.0
  pypy-5.7.0-src
  pypy-5.7.0
  pypy-5.7.1-src
  pypy-5.7.1
  pypy2-5.3-src
  pypy2-5.3
  pypy2-5.3.1-src
  pypy2-5.3.1
  pypy2-5.4-src
  pypy2-5.4
  pypy2-5.4.1-src
  pypy2-5.4.1
  pypy2-5.6.0-src
  pypy2-5.6.0
  pypy2-5.7.0-src
  pypy2-5.7.0
  pypy2-5.7.1-src
  pypy2-5.7.1
  pypy2.7-5.8.0-src
  pypy2.7-5.8.0
  pypy2.7-5.9.0-src
  pypy2.7-5.9.0
  pypy2.7-5.10.0-src
  pypy2.7-5.10.0
  pypy2.7-6.0.0-src
  pypy2.7-6.0.0
  pypy2.7-7.0.0-src
  pypy2.7-7.0.0
  pypy2.7-7.1.0-src
  pypy2.7-7.1.0
  pypy2.7-7.1.1-src
  pypy2.7-7.1.1
  pypy2.7-7.2.0-src
  pypy2.7-7.2.0
  pypy2.7-7.3.0-src
  pypy2.7-7.3.0
  pypy2.7-7.3.1-src
  pypy2.7-7.3.1
  pypy2.7-7.3.2-src
  pypy2.7-7.3.2
  pypy2.7-7.3.3-src
  pypy2.7-7.3.3
  pypy2.7-7.3.4-src
  pypy2.7-7.3.4
  pypy2.7-7.3.5-src
  pypy2.7-7.3.5
  pypy2.7-7.3.6-src
  pypy2.7-7.3.6
  pypy2.7-7.3.8-src
  pypy2.7-7.3.8
  pypy2.7-7.3.9-src
  pypy2.7-7.3.9
  pypy2.7-7.3.10-src
  pypy2.7-7.3.10
  pypy2.7-7.3.11-src
  pypy2.7-7.3.11
  pypy2.7-7.3.12-src
  pypy2.7-7.3.12
  pypy3-2.3.1-src
  pypy3-2.3.1
  pypy3-2.4.0-src
  pypy3-2.4.0
  pypy3.3-5.2-alpha1-src
  pypy3.3-5.2-alpha1
  pypy3.3-5.5-alpha-src
  pypy3.3-5.5-alpha
  pypy3.5-c-jit-latest
  pypy3.5-5.7-beta-src
  pypy3.5-5.7-beta
  pypy3.5-5.7.1-beta-src
  pypy3.5-5.7.1-beta
  pypy3.5-5.8.0-src
  pypy3.5-5.8.0
  pypy3.5-5.9.0-src
  pypy3.5-5.9.0
  pypy3.5-5.10.0-src
  pypy3.5-5.10.0
  pypy3.5-5.10.1-src
  pypy3.5-5.10.1
  pypy3.5-6.0.0-src
  pypy3.5-6.0.0
  pypy3.5-7.0.0-src
  pypy3.5-7.0.0
  pypy3.6-7.0.0-src
  pypy3.6-7.0.0
  pypy3.6-7.1.0-src
  pypy3.6-7.1.0
  pypy3.6-7.1.1-src
  pypy3.6-7.1.1
  pypy3.6-7.2.0-src
  pypy3.6-7.2.0
  pypy3.6-7.3.0-src
  pypy3.6-7.3.0
  pypy3.6-7.3.1-src
  pypy3.6-7.3.1
  pypy3.6-7.3.2-src
  pypy3.6-7.3.2
  pypy3.6-7.3.3-src
  pypy3.6-7.3.3
  pypy3.7-c-jit-latest
  pypy3.7-7.3.2-src
  pypy3.7-7.3.2
  pypy3.7-7.3.3-src
  pypy3.7-7.3.3
  pypy3.7-7.3.4-src
  pypy3.7-7.3.4
  pypy3.7-7.3.5-src
  pypy3.7-7.3.5
  pypy3.7-7.3.6-src
  pypy3.7-7.3.6
  pypy3.7-7.3.7-src
  pypy3.7-7.3.7
  pypy3.7-7.3.8-src
  pypy3.7-7.3.8
  pypy3.7-7.3.9-src
  pypy3.7-7.3.9
  pypy3.8-7.3.6-src
  pypy3.8-7.3.6
  pypy3.8-7.3.7-src
  pypy3.8-7.3.7
  pypy3.8-7.3.8-src
  pypy3.8-7.3.8
  pypy3.8-7.3.9-src
  pypy3.8-7.3.9
  pypy3.8-7.3.10-src
  pypy3.8-7.3.10
  pypy3.8-7.3.11-src
  pypy3.8-7.3.11
  pypy3.9-7.3.8-src
  pypy3.9-7.3.8
  pypy3.9-7.3.9-src
  pypy3.9-7.3.9
  pypy3.9-7.3.10-src
  pypy3.9-7.3.10
  pypy3.9-7.3.11-src
  pypy3.9-7.3.11
  pypy3.9-7.3.12-src
  pypy3.9-7.3.12
  pypy3.10-7.3.12-src
  pypy3.10-7.3.12
  pyston-2.2
  pyston-2.3
  pyston-2.3.1
  pyston-2.3.2
  pyston-2.3.3
  pyston-2.3.4
  pyston-2.3.5
  stackless-dev
  stackless-2.7-dev
  stackless-2.7.2
  stackless-2.7.3
  stackless-2.7.4
  stackless-2.7.5
  stackless-2.7.6
  stackless-2.7.7
  stackless-2.7.8
  stackless-2.7.9
  stackless-2.7.10
  stackless-2.7.11
  stackless-2.7.12
  stackless-2.7.14
  stackless-2.7.16
  stackless-3.2.2
  stackless-3.2.5
  stackless-3.3.5
  stackless-3.3.7
  stackless-3.4-dev
  stackless-3.4.2
  stackless-3.4.7
  stackless-3.5.4
  stackless-3.7.5
```

やりたいことは[これ](https://zenn.dev/ml_bear/books/d1f060a3f166a5/viewer/a43195)なので、記事からバージョンを決める

[まずは環境準備をしよう](https://zenn.dev/ml_bear/books/d1f060a3f166a5/viewer/0e8fe3)を読むと Python 3.8.1 以上になっている

一旦、v3.8.1 で行こう！

```sh
pyenv install 3.8.1
```

#### アンインストールするときは下記

```sh
pyenv uninstall 3.8.1
```

### エラーになった

```sh
pyenv install 3.8.1


python-build: use openssl from homebrew
python-build: use readline from homebrew
Downloading Python-3.8.1.tar.xz...
-> https://www.python.org/ftp/python/3.8.1/Python-3.8.1.tar.xz
Installing Python-3.8.1...
python-build: use readline from homebrew
python-build: use zlib from xcode sdk

BUILD FAILED (OS X 13.4.1 using python-build 20180424)

Inspect or clean up the working tree at /var/folders/t9/730wrqwn59q8nkjtmyvstlyh0000gn/T/python-build.20230731143038.22830
Results logged to /var/folders/t9/730wrqwn59q8nkjtmyvstlyh0000gn/T/python-build.20230731143038.22830.log

Last 10 log lines:
checking for --with-cxx-main=<compiler>... no
checking for clang++... no
configure:

  By default, distutils will build C++ extension modules with "clang++".
  If this is not intended, then set CXX on the configure command line.

checking for the platform triplet based on compiler characteristics... darwin
configure: error: internal configure error for the platform triplet, please file a bug report
make: *** No targets specified and no makefile found.  Stop.
```

読んで見ると元々 python3 が入っているとのこと。
デフォルトは削除してはいけないとのこと。
バージョンを確かめる

```sh
which python

python: aliased to /usr/bin/python3

python --version

Python 3.9.6
```

3.9.6 が入っている

要求仕様は

- LangChain (0.0.225): Python >=3.8.1, <4.0
- Streamlit (1.24.0): Python >=3.8, !=3.9.7
- OpenAI (0.27.8): Python >=3.7.1

なので、満たしている。これで行こう。古いものは Xcode 側で弾かれているっぽいがここでは詳細は追いかけない
念のため、pip もチェック

```sh
which pip

pip: aliased to /usr/bin/pip3
```

めちゃくちゃ入っている^^;

次に VSCode のエクステンションをインストール

設定完了

以下は仮想環境を構築する必要があるので一旦環境構築終了

## pyenv で Python のバージョンを指定する

```sh
pyenv versions

* system (set by /Users/encoolus/.pyenv/version)
```

これはなくても良かった 2023-08-01

仮想環境はなくても大丈夫そうなので、このまま[これ](https://zenn.dev/umi_mori/books/prompt-engineer)をやる
