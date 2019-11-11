"""日本国憲法を ./schema.json 通りの JSON に整形するスクリプト"""
import json


def get_preamble(raw_preamble: dict) -> dict:
    """日本国憲法 前文 を取得する"""

    return {
        'title': '前文',
        'terms': [{
            'title': None,
            'sentence': ''.join([paragraph['ParagraphSentence']['Sentence']['#text'] for paragraph in raw_preamble['Paragraph']]),
            'examples': None
        }]
    }

def become_list(item) -> list:
    """引数が list でなければ list に変換して返す。引数が list であればそのまま帰す"""

    if isinstance(item, list):
        return item
    else:
        return [item]

def get_examples(items: list) -> list:
    """例をリストとして取得する"""

    examples: list = []
    for item in items:
        sentences: list = become_list(item['ItemSentence']['Sentence'])

        text: list = []
        for sentence in sentences:
            text.append(sentence['#text'])
        examples.append(''.join(text))

    return examples

def get_provision(paragraphs: list, title: str) -> dict:
    """paragraph と title を投げると リストに突っ込めばいいだけの provisions object(dict) を返す"""

    # 条文オブジェクト
    provision = {
        'title': title,
        'terms': []
    }

    if len(paragraphs) == 1:
        paragraph = paragraphs[0]
        term: dict = {
            'title': None,
            'sentence': None,
            'examples': None
        }

        # 例があった場合はリストとして取得する
        if 'Item' in paragraph:
            term['examples'] = get_examples(paragraph['Item'])

        text: list = []
        sentences: list = become_list(paragraph['ParagraphSentence']['Sentence'])
        for sentence in sentences:
            text.append(sentence['#text'])

        term['sentence'] = ''.join(text)
        provision['terms'].append(term)

    else:
        for paragraph in paragraphs:
            term: dict = {
                'title': '第' + paragraph['@Num'] + '項',
                'sentence': None,
                'examples': None
            }

            # 例があった場合はリストとして取得する
            if 'Item' in paragraph:
                term['examples'] = get_examples(paragraph['Item'])

            text: list = []
            sentences = become_list(paragraph['ParagraphSentence']['Sentence'])
            for sentence in sentences:
                text.append(sentence['#text'])

            term['sentence'] = ''.join(text)
            provision['terms'].append(term)

    return provision



with open('original/constitution.json', 'r') as original_file:
    original_json = json.load(original_file)
    raw_law = original_json['Law']['LawBody']

#### 前文（Preamble）を index 0 に挿入 ####
contents: list = [get_preamble(raw_law['Preamble'])]

#### 本文 ####
for chapter in raw_law['MainProvision']['Chapter']:
    for article in become_list(chapter['Article']):
        paragraphs = become_list(article['Paragraph'])
        contents.append(get_provision(paragraphs, article['ArticleTitle']))

with open('dist/constitution.json', 'w') as f:
    json.dump(contents, f, ensure_ascii=False, indent=2)