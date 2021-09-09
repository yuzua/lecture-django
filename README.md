# lecture-django
# WindowsのDockerの設定
* コントロールパネルの設定(Hyper-VのチェックOFF,Linux用WindowsサブシステムのチェックON,仮想マシンプラットフォームのチェックON)
# VSCodeの設定
* ※管理者で入った場合、pathに--extensions-dir=".¥extensions"を追加
# memo
* 設定より規約・・・調べる
* Modemls.pyを使うメリット・・・①MySQLやPostgreSQLの違いを自動的に処理できるから②ORマッピング
# .envの設定
* 適当なファイル作成→sample.pyの作成(pythonを認識させる)→$python -m venv .env→$.\.env\Scripts\Activate.ps1→ctrl+shift+pでpython~(.env)を選択 ※初めて使う場合 $Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -force
# pipenvを使ったdjango-allauthの使い方
* $pipenv install django-allauth→cp -r /root/.local/share/virtualenvs/Django-uBqtMRMC/lib/python3.9/site-packages/allauth/templates/account/ /Django/diary/templates ※find ./ -name allauthでテンプレートの場所を検索可能
# requirements.txtを使用する場合
* requirements.txtを作成→$pip install -r .\requirements.txt でインストールした内容を管理
# Djangoの拡張
* $pip install pylint_django...続きは動画参照