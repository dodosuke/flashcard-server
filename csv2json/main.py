# coding:UTF-8
import json

name = "情報セキュリティマネジメント"
cards = []
count = 1

# CSVファイルのロード
with open('./input.csv', 'r') as file:
    # list of dictの作成
    for line in file:
        # Split a line into words
        words = line.split(',')
        card = {}
        card["key"] = count
        card["front"] = str(words[1])
        card["back"] = str(words[3])

        cards.append(card)
        count += 1

with open('../output.json', 'w') as f:
    # JSONへの書き込み
    deck = {"name": name, "cards": cards}
    json.dump(deck, f, ensure_ascii=False)