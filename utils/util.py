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

    sentences: list = become_list(paragraph_sentence['Sentence'])
    text: list = []
    for sentence in sentences:
        text.append(sentence['#text'])

    return ''.join(text)
