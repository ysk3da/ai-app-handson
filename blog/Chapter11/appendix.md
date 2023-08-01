# まだまだある機能たち

| 機能                | 概要                                                                                                                                                                                                                                                                                                  |
| :------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent               | LangChain に Tool を与えてそれを使ってタスクを解かせることができる。<br>うまく使えば自律型エージェントを作ることができるが、賢く動いてもらうのはなかなかハードルが高いらしい。                                                                                                                        |
| Function Calling    | ChatGPT API のレスポンスを JSON 形式に固定できる機能。このレスポンスを用いて他の関数呼び出しを想定しているのでこのような機能名らしい。ChatGPT を他の機能と融合させやすくなるため、開発者コミュニティからは歓喜の声が上がっている                                                                      |
| Zapier 連携         | LangChain を Zapier と連携させることもできる。この Youtube 動画に詳しい。LangChain と Zapier を組み合わせると「Greg のメールみて適当に返信の下書き書いといて」とかできるらしい。                                                                                                                      |
| ChatGPT Plugin 連携 | Agent に持たせる Tool の一つに ChatGPT Plugin を選択することもできる。公開されている ChatGPT Plugin をうまく利用できればやりたい内容も広がると思う。                                                                                                                                                  |
| 非同期処理          | LangChain を用いれば非同期処理を用いて ChatGPT API を呼び出すことも簡単。LangChain の過度なブラックボックスを嫌って自前実装する際に役立つ機能。                                                                                                                                                       |
| キャッシュ          | ChatGPT API はレスポンスが速いとは言えない API です。そのため、ユーザーから同じような質問が来た場合はキャッシュを用いて以前の回答を返すといった工夫も重要になります。LangChain にはさまざまなキャッシュが実装されているので、多くのユーザーが用いるサービスを実装される際は利用するのが良いでしょう。 |
| BigQuery 連携       | LangChain を用いれば BigQuery との連携も可能。テーブルのスキーマと何行かのサンプルレコードを与えれば、結構上手に SQL を書いてくれるとのことなので、データアナリストの方々は一度試す価値はありそう。                                                                                                   |