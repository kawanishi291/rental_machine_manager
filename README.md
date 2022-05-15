# rental_machine_manager


## 構成
```
./rental_machine_manager
├── Pipfile
├── Pipfile.lock
├── README.md
├── config.yaml
├── excel
│   └── XXXX.xlsx
├── main.py
├── run.cmd
├── run.sh
└── text
    └── XXXX.txt
```

> config.yaml
```
# Excelファイル名(年月無し)
FILE: "XXXX"

# 抽出条件(条件)
DEPARTMENT: "XXXX"

# 抽出条件(Excel 項目名)
KEY: "XXXX"

# 確認対象者
NAME: "XXXX"

# 抽出したい情報
ITEM:
  - "XXXX"
  - "XXXX"
  - "XXXX"
  - "XXXX"
  - "XXXX"

# 開始日と終了日
START: "XXXX"
END: "XXXX"
```

## 使用方法
```
cd /XXX/rental_machine_manager
```
###### Windows(cmd)
```
run.cmd
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