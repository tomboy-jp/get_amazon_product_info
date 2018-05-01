import os
import time
from amazon.api import AmazonAPI

def amazon_product_info(ItemId, trying=3):

    # Amazonアソシエイトのアカウント取得後、下記の3パラメータを環境変数に書き込んでください。
    AMAZON_ACCESS_KEY = os.environ['AMAZON_ACCESS_KEY']
    AMAZON_SECRET_KEY = os.environ['AMAZON_SECRET_KEY']
    AMAZON_ASSOCIATE_TAG = os.environ['AMAZON_ASSOCIATE_TAG']

    amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOCIATE_TAG, Region='JP')

    cnt = 0

    while cnt != trying:

        try:
            product = amazon.lookup(ItemId=ItemId)
            print("商品名:\t\t{}".format(product.title))
            print("価格:\t\t{}".format(product.formatted_price))
            print("ジャンル:\t{}".format(product.genre))
            print("ランキング:\t{}".format(product.sales_rank))

            # 他のメタデータを参照する場合。
            # print(dir(product))

            return product

        except:
            pass

        cnt += 1
        time.sleep(1)

#asinコード or 商品コードを指定して呼び出す。
amazon_product_info("4873118360")
