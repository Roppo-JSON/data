"""複数の法令のパースに使えそうな関数群"""


def become_list(item) -> list:
    """引数が list でなければ list に変換して返す。引数が list であればそのまま帰す

    項が1つであったり、章内の条文が1つのみの場合は list ではなく dict であることがあるので、それの差を吸収するための関数。
    """

    if isinstance(item, list):
        return item
    else:
        return [item]


def get_text_from_paragraph_sentence(paragraph_sentence: list) -> str:
    """ParagraphSentence から条文本体の文章のみを取り出す。"""

    sentences: list = become_list(paragraph_sentence["Sentence"])
    text: list = []
    for sentence in sentences:
        if "Ruby" in sentence:
            text.append(remove_ruby(sentence))
        else:
            text.append(sentence["#text"])

    return "".join(text)


def remove_ruby(sentence: dict) -> str:
    """Ruby が存在する Sentence 内の条文を、ルビが振られている漢字を文中に含めた文字列を返す"""

    rubies = become_list(sentence["Ruby"])
    texts = sentence["#text"]

    # ルビが振られている漢字も含めた条文
    complete_text: list = []

    for i, text in enumerate(texts):
        complete_text.append(text)
        if i < len(rubies):
            complete_text.append(rubies[i]["#text"])

    return "".join(complete_text)


def get_examples(items: list) -> list:
    """例をリストとして取得する"""

    examples: list = []
    for item in items:
        examples.append(get_text_from_paragraph_sentence(item["ItemSentence"]))

    return examples


def print_line(length=20) -> str:
    """区切り線の表示"""
    print("=" * length)
