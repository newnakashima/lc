from Topic import Topic
from Character import Character
from Personality import Personality

if __name__ == "__main__":
    c = Character()
    c.personality = Personality.主人公
    t = Topic.テストトピック
    c.receiveTopic(t)
