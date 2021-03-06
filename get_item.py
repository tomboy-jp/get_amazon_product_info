import os
import time
from amazon.api import AmazonAPI

# Amazonアソシエイトのアカウント取得後、下記の3パラメータをシェルの設定ファイルや「.env」などに書き込んでください。
AMAZON_ACCESS_KEY = os.environ['AMAZON_ACCESS_KEY']
AMAZON_SECRET_KEY = os.environ['AMAZON_SECRET_KEY']
AMAZON_ASSOCIATE_TAG = os.environ['AMAZON_ASSOCIATE_TAG']

amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOCIATE_TAG, Region='JP')

def from_code(ItemId, trying=3):
    """
    input:
        ItemId = 対象のコンテンツIDやASINコード。
        trying = 接続できなかったときのリトライ回数。

    output:
        product = (「python-amazon-simple-product-api」が提供するオブジェクト。
                    例えばproduct.titleには商品名が格納されている。)
    """

    cnt = 0

    while cnt != trying:

        try:
            product = amazon.lookup(ItemId=ItemId)
            return product

        except:
            pass

        cnt += 1
        time.sleep(1)


def printer(product):
    """
    input:
        product = from_codeが出力するものに同じ。

    output:
        なし。
    """

    print("商品名:\t\t{}".format(product.title))
    print("価格:\t\t{}".format(product.formatted_price))
    print("ジャンル:\t{}".format(product.genre))
    print("ランキング:\t{}".format(product.sales_rank))
    print("商品URL:\t{}".format(product.offer_url))
    print("画像URL:\t{}".format(product.medium_image_url))
    print("")

    # 他のメタデータを参照する場合。
    # print(dir(product))

"""
以下、テストコード。
"""

#asinコード or 商品コードのリスト。
list = ["4873118360",  "B00PVHO6O8", "B000TUEUZW", "B005VB4IGA", "B07BBZ4YJ9"]

for i in list:

    product = from_code(i, 10)
    try:
        printer(product)
    except:
        pass
