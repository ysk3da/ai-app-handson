# 長時間 Youtube 動画を要約しよう

- chain_type=map_reduce を用いた要約の方法を知る
- Text Splitter とは何かを知る
- gpt-3.5-turbo-16k の便利さを知る

## インストールが必要なもの

```sh
pip install tiktoken
```

## 動かしてみる

```sh
streamlit run 08_sample_app.py
```

試す動画
https://www.youtube.com/watch?v=vtPPWWygfjo&t=213s
-> 要約できた！

### Summary

```
このYouTubeの動画は、勉強の悩みや勉強法についての話です。勉強しても成果が出ない、集中力がない、勉強が続かないといった悩みを抱える人には、勉強法を学んでいないという共通点があります。勉強法とは、自分に合った勉強のやり方を知ることであり、この動画ではその中でも特にオススメの勉強法を3つ紹介しています。まずは、勉強の目的と目標を明確にすることが重要であり、目的と目標は違うものであることを理解する必要があります。次に、勉強の習慣を見つけるためには、三日坊主ルールを活用することが効果的です。最後に、アウトプットをすることの重要性について説明しています。インプットからアウトプットまでの時間が長くなると、良い内容をアウトプットすることができず、テンションも下がって行動に移せなくなると述べています。勉強する人は、すぐにアウトプットするように取り組むことを意識してみるように勧めています。また、この動画では他にも勉強法が紹介されているので、興味がある人は続きを読んでみるように言及しています。最後に、この動画の著者は登録者数が10万人を超えるYouTubeチャンネルを運営しており、この本とチャンネルのリンクも説明欄に貼られているので、興味がある人は覗いてみるように勧めています。
```
