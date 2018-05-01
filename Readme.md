# Get Amazon Product's Information
商品コードやASINコードから商品情報を取得します。

## 環境
```
$ sw_vers  
ProductName:	Mac OS X  
ProductVersion:	10.13.4  
BuildVersion:	17E202  

$ python -V  
Python 3.6.3 :: Anaconda custom (64-bit)
```

## 手順
1. Amazonアソシエイトのアカウントを持っていることが前提条件となります。  
これがないとAPIを叩くことができません。  
[公式](https://affiliate.amazon.co.jp/)からサクッと取得しましょう。  
その際Webサイトの提示を求められますが、適当で大丈夫です。  
必要なのは「アクセスキー」「シークレットキー」「アソシエイトタグ(=アソシエイトID)」の3つのアクセス情報であり、  
審査の合否は関係ありません。  
落ちてもきちんと発行されます。  

2. 取得したアクセス情報の管理方法について。  
pythonのコードにベタ書きしてもいいのですが、うっかりコードを公開した場合は悪用される恐れがあります。  
対策として別の場所に環境変数として保存してコード実行時に読み込む、といった処理をするのが良さそうです。  
具体的にはシェルの設定ファイルに書き込んだり、「.env」ファイルを別途作成するといった方法が考えられます。   
前者の場合は何も考えずに実行できるというメリット、微弱ながら他のプログラムに影響を及ぼす可能性がある、といったデメリットがあります。  
後者の場合は独立しているので他に影響を与えることがないというメリットと実行と管理の際に一手間かける必要がある、というデメリットがあります。  
今回は後者を採用します。  

3. 「.env」ファイルを読み込みながらpythonを実行するためのモジュールをインストールします。  
```
$ brew install forego
```
  続いて「.env」ファイルを作成します。  
  必ず実行コードと同じ場所に作ってください。  
```
$ echo "AMAZON_ACCESS_KEY=$あなたのアクセスキー" >> .env
$ echo "AMAZON_SECRET_KEY=$あなたのシークレットキー" >> .env
$ echo "AMAZON_ASSOCIATE_TAG=$あなたのアソシエイトタグ" >> .env
```
「.gitignore」で「.env」を弾いていない場合は間違えてpushしないように記述しておきましょう。  
```
$ echo ".env" >> .gitignore
```
  これで認証周りの準備は完了です。

4. 今回Pythonコードで使用するモジュールをインストールします。  
```
$ pip install python-amazon-simple-product-api
```
  URLの作成とxmlのパースを自動化してくれる強力なモジュールです。  
  今回は使用しませんが、AmazonAPI & Python関連では他に有名なものとして「bottlenose」があります。  
  「python-amazon-simple-product-api」の元にもなっているモジュールで、出来る範囲が広い分、スクレイピングは別途行う必要があるなど詳細なコーディングを求められます。  

5. 必要な手順は以上です。  
あとはサンプルコード[サンプルコード](https://github.com/tomboy-jp/get_amazon_product_info/blob/master/get_item.py)をご覧ください。
