# rental_machine_manager


## 構成
```
./rental_machine_manager
├── Pipfile
├── Pipfile.lock
├── README.md
├── config.ini
├── excel
│   └── XXXX.xlsx
├── main.py
├── run.bat
├── run.sh
└── text
    └── XXXX.txt
```

> config.ini
```
# Excelファイル名(年月無し)
[FILE]
FILE=XXXX

# 抽出条件(条件)
[DEPARTMENT]
DEPARTMENT=XXXX

# 抽出条件(Excel 項目名)
[KEY]
KEY=XXXX

# 確認対象者
[NAME]
NAME=XXXX

# 抽出したい情報
[ITEM]
MACHINE_ID=XXXX
ASSET_ABBREVIATION=XXXX
ASSET_NAME=XXXX
MODEL_NUMBER=XXXX
LOCATION=XXXX

# 開始日と終了日
[RENTAL]
START=XXXX
END=XXXX
```

## 使用方法
```
cd /XXX/rental_machine_manager
```
###### Windows(cmd)
```
run.bat
```
###### mac(zsh)
```
zsh run.sh
```

#### インストール
```
pipenv install
```
#### 起動
```
pipenv shell
python main.py
```