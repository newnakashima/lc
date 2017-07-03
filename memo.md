# メモ

- ストーリーには階層構造を作る
    - 最も大きなものがStory
    - 次がSequence
    - 次がTopic

- TopicがCharacterに渡されることによって展開する

- Character同士はTopicを元にTalkを生成する
    - Talkを連鎖的に延々と生成し合うことで会話を進行させる

- Characterは場に居合わせた他のCharacterにアクセス可能でなくてはならない

- 場はScene
    - SceneはPlace、Characterのリスト持つ
