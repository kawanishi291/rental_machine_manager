# rental_machine_manager


## 構成
```
.
├── Pipfile
├── Pipfile.lock
├── README.md
├── config.yaml
├── excel
│   └── XXXX.xlsx
├── main.py
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