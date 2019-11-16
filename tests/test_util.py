import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.util import become_list
from utils.util import get_examples
from utils.util import remove_ruby
from utils.util import get_text_from_paragraph_sentence


class UtilTest(unittest.TestCase):
    """utils.util のテストクラス"""

    def test_become_list(self):
        test_case = [
            1,
            [1, 3, 4],
            {"message": "hello"},
            [{"message": "hello1"}, {"message": "hello2"}, {"message": "hallo3"}],
        ]
        answer_case = [
            [1],
            [1, 3, 4],
            [{"message": "hello"}],
            [{"message": "hello1"}, {"message": "hello2"}, {"message": "hallo3"}],
        ]

        for i, item in enumerate(test_case):
            self.assertEqual(become_list(item), answer_case[i])

    def test_get_examples(self):
        test_data = [
            {
                "@Delete": "false",
                "@Hide": "false",
                "@Num": "1",
                "ItemTitle": "一",
                "ItemSentence": {
                    "Sentence": {
                        "@WritingMode": "vertical",
                        "#text": "憲法改正、法律、政令及び条約を公布すること。",
                    }
                },
            },
            {
                "@Delete": "false",
                "@Hide": "false",
                "@Num": "2",
                "ItemTitle": "二",
                "ItemSentence": {
                    "Sentence": {"@WritingMode": "vertical", "#text": "国会を召集すること。"}
                },
            },
            {
                "@Delete": "false",
                "@Hide": "false",
                "@Num": "3",
                "ItemTitle": "三",
                "ItemSentence": {
                    "Sentence": {"@WritingMode": "vertical", "#text": "衆議院を解散すること。"}
                },
            },
            {
                "@Delete": "false",
                "@Hide": "false",
                "@Num": "4",
                "ItemTitle": "四",
                "ItemSentence": {
                    "Sentence": {
                        "@WritingMode": "vertical",
                        "#text": "国会議員の総選挙の施行を公示すること。",
                    }
                },
            },
            {
                "@Delete": "false",
                "@Hide": "false",
                "@Num": "5",
                "ItemTitle": "五",
                "ItemSentence": {
                    "Sentence": {
                        "@WritingMode": "vertical",
                        "#text": "国務大臣及び法律の定めるその他の官吏の任免並びに全権委任状及び大使及び公使の信任状を認証すること。",
                    }
                },
            },
            {
                "@Delete": "false",
                "@Hide": "false",
                "@Num": "6",
                "ItemTitle": "六",
                "ItemSentence": {
                    "Sentence": {
                        "@WritingMode": "vertical",
                        "#text": "大赦、特赦、減刑、刑の執行の免除及び復権を認証すること。",
                    }
                },
            },
            {
                "@Delete": "false",
                "@Hide": "false",
                "@Num": "7",
                "ItemTitle": "七",
                "ItemSentence": {
                    "Sentence": {"@WritingMode": "vertical", "#text": "栄典を授与すること。"}
                },
            },
            {
                "@Delete": "false",
                "@Hide": "false",
                "@Num": "8",
                "ItemTitle": "八",
                "ItemSentence": {
                    "Sentence": {
                        "@WritingMode": "vertical",
                        "#text": "批准書及び法律の定めるその他の外交文書を認証すること。",
                    }
                },
            },
            {
                "@Delete": "false",
                "@Hide": "false",
                "@Num": "9",
                "ItemTitle": "九",
                "ItemSentence": {
                    "Sentence": {
                        "@WritingMode": "vertical",
                        "#text": "外国の大使及び公使を接受すること。",
                    }
                },
            },
            {
                "@Delete": "false",
                "@Hide": "false",
                "@Num": "10",
                "ItemTitle": "十",
                "ItemSentence": {
                    "Sentence": {"@WritingMode": "vertical", "#text": "儀式を行ふこと。"}
                },
            },
        ]
        ans_data = [
            "憲法改正、法律、政令及び条約を公布すること。",
            "国会を召集すること。",
            "衆議院を解散すること。",
            "国会議員の総選挙の施行を公示すること。",
            "国務大臣及び法律の定めるその他の官吏の任免並びに全権委任状及び大使及び公使の信任状を認証すること。",
            "大赦、特赦、減刑、刑の執行の免除及び復権を認証すること。",
            "栄典を授与すること。",
            "批准書及び法律の定めるその他の外交文書を認証すること。",
            "外国の大使及び公使を接受すること。",
            "儀式を行ふこと。",
        ]
        self.assertEqual(get_examples(test_data), ans_data)

    def test_remove_ruby(self):
        test_case = [
            {
                "@WritingMode": "vertical",
                "#text": [
                    "第二百三十五条から第二百三十六条まで（窃盗、不動産侵奪、強盗）、第二百三十八条から第二百四十条まで（事後強盗、",
                    "酔強盗、強盗致死傷）、第二百四十一条第一項及び第三項（強盗・強制性交等及び同致死）並びに第二百四十三条（未遂罪）の罪",
                ],
                "Ruby": {"#text": "昏", "Rt": "こん"},
            },
            {
                "@WritingMode": "vertical",
                "#text": ["死刑、懲役、禁", "、罰金、拘留及び科料を主刑とし、没収を付加刑とする。"],
                "Ruby": {"#text": "錮", "Rt": "こ"},
            },
            {
                "@Num": "1",
                "@WritingMode": "vertical",
                "#text": [
                    "十三歳以上の者に対し、暴行又は脅迫を用いて性交、",
                    "門性交又は口",
                    "性交（以下「性交等」という。）をした者は、強制性交等の罪とし、五年以上の有期懲役に処する。",
                ],
                "Ruby": [{"#text": "肛", "Rt": "こう"}, {"#text": "腔", "Rt": "くう"}],
            },
        ]
        ans_case = [
            "第二百三十五条から第二百三十六条まで（窃盗、不動産侵奪、強盗）、第二百三十八条から第二百四十条まで（事後強盗、昏酔強盗、強盗致死傷）、第二百四十一条第一項及び第三項（強盗・強制性交等及び同致死）並びに第二百四十三条（未遂罪）の罪",
            "死刑、懲役、禁錮、罰金、拘留及び科料を主刑とし、没収を付加刑とする。",
            "十三歳以上の者に対し、暴行又は脅迫を用いて性交、肛門性交又は口腔性交（以下「性交等」という。）をした者は、強制性交等の罪とし、五年以上の有期懲役に処する。",
        ]

        for i, item in enumerate(test_case):
            self.assertEqual(remove_ruby(item), ans_case[i])

    def test_get_text_from_paragraph_sentence(self):
        test_case = [
            {
                "Sentence": {
                    "@WritingMode": "vertical",
                    "#text": "公然とわいせつな行為をした者は、六月以下の懲役若しくは三十万円以下の罰金又は拘留若しくは科料に処する。",
                }
            },
            {
                "Sentence": [
                    {
                        "@Num": "1",
                        "@WritingMode": "vertical",
                        "#text": "わいせつな文書、図画、電磁的記録に係る記録媒体その他の物を頒布し、又は公然と陳列した者は、二年以下の懲役若しくは二百五十万円以下の罰金若しくは科料に処し、又は懲役及び罰金を併科する。",
                    },
                    {
                        "@Num": "2",
                        "@WritingMode": "vertical",
                        "#text": "電気通信の送信によりわいせつな電磁的記録その他の記録を頒布した者も、同様とする。",
                    },
                ],
            },
            {
                "Sentence": [
                    {
                        "@Num": "1",
                        "@WritingMode": "vertical",
                        "#text": [
                            "十三歳以上の者に対し、暴行又は脅迫を用いて性交、",
                            "門性交又は口",
                            "性交（以下「性交等」という。）をした者は、強制性交等の罪とし、五年以上の有期懲役に処する。",
                        ],
                        "Ruby": [
                            {"#text": "肛", "Rt": "こう"},
                            {"#text": "腔", "Rt": "くう"},
                        ],
                    },
                    {
                        "@Num": "2",
                        "@WritingMode": "vertical",
                        "#text": "十三歳未満の者に対し、性交等をした者も、同様とする。",
                    },
                ]
            },
        ]
        ans_case = [
            "公然とわいせつな行為をした者は、六月以下の懲役若しくは三十万円以下の罰金又は拘留若しくは科料に処する。",
            "わいせつな文書、図画、電磁的記録に係る記録媒体その他の物を頒布し、又は公然と陳列した者は、二年以下の懲役若しくは二百五十万円以下の罰金若しくは科料に処し、又は懲役及び罰金を併科する。電気通信の送信によりわいせつな電磁的記録その他の記録を頒布した者も、同様とする。",
            "十三歳以上の者に対し、暴行又は脅迫を用いて性交、肛門性交又は口腔性交（以下「性交等」という。）をした者は、強制性交等の罪とし、五年以上の有期懲役に処する。十三歳未満の者に対し、性交等をした者も、同様とする。",
        ]

        for i, item in enumerate(test_case):
            self.assertEqual(get_text_from_paragraph_sentence(item), ans_case[i])


if __name__ == "__main__":
    unittest.main(verbosity=2)
