from Topic import Topic
from Personality import Personality

class Character:
    """キャラクターのクラス"""
    
    def receiveTopic(self, topic):
        self.talk = self.topic2talk(topic)

    def createTalk(self, talk):
        print("not implemonted")

    def topic2talk(self, topic):
        """TopicをPersinalityに応じてTalkに変換する"""
        if topic == Topic.テストトピック:
            if self.personality == Personality.主人公:
                print("これはテストです")
                return Topic.テスト返信
                # self.scene.characters[1].createTalk(1);
        else:
            print("トピックが1以外")

