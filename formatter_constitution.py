"""日本国憲法を ./schema.json 通りの JSON に整形するスクリプト"""
import json

from utils.util import become_list
from utils.util import get_examples
from utils.util import get_text_from_paragraph_sentence


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

        term['sentence'] = get_text_from_paragraph_sentence(paragraph['ParagraphSentence'])
        provision['terms'].append(term)

    else:
        for paragraph in paragraphs:
            term: dict = {
                'title': f"第{paragraph['@Num']}項",
                'sentence': None,
                'examples': None
            }

            # 例があった場合はリストとして取得する
            if 'Item' in paragraph:
                term['examples'] = get_examples(paragraph['Item'])

            term['sentence'] = get_text_from_paragraph_sentence(paragraph['ParagraphSentence'])
            provision['terms'].append(term)

    return provision


with open('original/constitution.json', 'r') as original_file:
    original_json = json.load(original_file)
    raw_law = original_json['Law']['LawBody']

# 前文（Preamble）を index 0 に挿入
contents: list = [get_preamble(raw_law['Preamble'])]

# 本文
for chapter in raw_law['MainProvision']['Chapter']:
    for article in become_list(chapter['Article']):
        paragraphs = become_list(article['Paragraph'])
        contents.append(get_provision(paragraphs, article['ArticleTitle']))


with open('dist/constitution.json', 'w') as f:
    json.dump(contents, f, ensure_ascii=False, indent=2)
