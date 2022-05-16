import glob
import datetime
import configparser
import pandas as pd
from monthdelta import monthmod


def SetFileName(m, y):
    zenhan_list = ["１", "２", "３", "４", "５", "６", "７", "８", "９", "１０", "１１", "１２"]

    match m:
        case 1:
            return "12-" + str(m + 1) + FILE + str(y), zenhan_list[m]
        case 12:
            return str(m - 1) + "-1" + FILE + str(y), zenhan_list[0]
        case _:
            return str(m - 1) + "-" + str(m + 1) + FILE + str(y), zenhan_list[m]

def SetData(df, index):
    data = ""

    for i in range(len(ITEM)):
        data += df[ITEM[i]][index]
        data += " "

    return data.strip()


def main():
    dt = datetime.datetime.now()
    file_name, sheet_month = SetFileName(dt.month, dt.year)

    path_list = glob.glob('./excel/' + file_name + '.xlsx')
    path_list.sort()
    path = path_list[-1]
    # print(path_list)

    df = pd.read_excel(path, sheet_name=sheet_month+"月終了", index_col=0, engine="openpyxl")
    df = df.reset_index()
    member_list =[]

    for index in df[df[KEY] == DEPARTMENT].index:
        name = df[NAME][index]
        data = SetData(df, index)
        start_date = datetime.datetime.strptime(df[START][index], '%Y/%m/%d %H:%M:%S')
        end_date = datetime.datetime.strptime(df[END][index], '%Y/%m/%d %H:%M:%S')
        mmod = monthmod(start_date, end_date)
        tmp_dict = {'name': "", 'first_name': name[:name.find(' ')], 'full_name': name, 'data': data, 'month': mmod[0].months + 1}
        member_list.append(tmp_dict)

    for i in range(len(member_list)):
        for j in range(len(member_list)):
            if i != j:
                if member_list[i]['name'] == member_list[j]['first_name']:
                    member_list[i]['name'] = member_list[i]['full_name']
                    break
                else:
                    member_list[i]['name'] = member_list[i]['first_name']


    with open('./text/' + file_name + '.txt', mode='w') as f:
        for member in member_list:
            f.write(
"""
◆%sさん
%s
→延長(36か月まで)*前回は%dか月延長でした。
→入替
→返却
"""
            % (member['name'], member['data'], member['month']))

    return 0


config = configparser.ConfigParser()
config.read('config.ini')
config.sections()

FILE = config["FILE"]["FILE"]
DEPARTMENT = config["DEPARTMENT"]["DEPARTMENT"]
KEY = config["KEY"]["KEY"]
NAME = config["NAME"]["NAME"]
ITEM_SECTION = config['ITEM']
START = config["RENTAL"]["START"]
END = config["RENTAL"]["END"]

ITEM = []
for k, v in ITEM_SECTION.items():
    ITEM.append(v)

if __name__ == '__main__':
    main()