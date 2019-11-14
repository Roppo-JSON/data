"""刑法を ./schema.json 通りの JSON に整形するスクリプト"""
import json

from utils.util import become_list
from utils.util import get_examples
from utils.util import get_text_from_paragraph_sentence


# TODO 第○条と第○条の△をひとつの provision にし、2つ目以降は「第○条の△」とする
def get_provision(paragraphs: list, title: str) -> dict:
    """paragraph と title を投げると リストに突っ込めばいいだけの provisions object(dict) を返す"""

    # 条文オブジェクト
    provision = {"title": title, "terms": []}

    if len(paragraphs) == 1:
        paragraph = paragraphs[0]
        term: dict = {"title": None, "sentence": None, "examples": None}

        # 例があった場合はリストとして取得する
        if "Item" in paragraph:
            term["examples"] = get_examples(paragraph["Item"])

        term["sentence"] = get_text_from_paragraph_sentence(
            paragraph["ParagraphSentence"]
        )
        provision["terms"].append(term)

    else:
        for paragraph in paragraphs:
            term: dict = {
                "title": f"第{paragraph['@Num']}項",
                "sentence": None,
                "examples": None,
            }

            # 例があった場合はリストとして取得する
            if "Item" in paragraph:
                term["examples"] = get_examples(paragraph["Item"])

            term["sentence"] = get_text_from_paragraph_sentence(
                paragraph["ParagraphSentence"]
            )
            provision["terms"].append(term)

    return provision


def main():

    with open("original/penal.json") as penal_file:
        json_data = json.load(penal_file)["Law"]["LawBody"]

    contents: list = []
    for part in json_data["MainProvision"]["Part"]:
        for chapter in part["Chapter"]:
            for article in chapter["Article"]:
                contents.append(
                    get_provision(
                        become_list(article["Paragraph"]), article["ArticleTitle"]
                    )
                )

    with open("dist/penal.json", "w") as f:
        json.dump(contents, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
