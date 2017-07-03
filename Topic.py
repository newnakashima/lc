class Topic:
    """話題のクラス。ストーリーの最小の単位"""
    def __init__(self, topicType):
        self.type = topicType
        """
        type list
        1: テストトピック
        2: ボーイミーツガール
        """
