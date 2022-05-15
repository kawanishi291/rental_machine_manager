import glob
import datetime
import yaml
import pandas as pd
import mojimoji
from monthdelta import monthmod


with open('./config.yaml', 'r') as f:
    yaml_file = yaml.safe_load(f)
    FILE = yaml_file["FILE"]
    DEPARTMENT = yaml_file["DEPARTMENT"]
    KEY = yaml_file["KEY"]
    NAME = yaml_file["NAME"]
    ITEM = yaml_file["ITEM"]
    START = yaml_file["START"]
    END = yaml_file["END"]


dt = datetime.datetime.now()
file_name = str(dt.month - 1) + "-" + str(dt.month + 1) + FILE + str(dt.year)


path_list = glob.glob('./excel/' + file_name + '.xlsx')
path_list.sort()
path = path_list[-1]
# print(path_list)

sheet_month = mojimoji.han_to_zen(str(dt.month + 1))

df = pd.read_excel(path, sheet_name=sheet_month+"月終了", index_col=0, engine="openpyxl")
df = df.reset_index()
member_list =[]

for index in df[df[KEY] == DEPARTMENT].index:
    name = df[NAME][index]
    data = df[ITEM[0]][index] + " " + df[ITEM[1]][index] + " " + df[ITEM[2]][index] + " " + df[ITEM[3]][index] + " " + df[ITEM[4]][index]
    start_date = datetime.datetime.strptime(df[START][index], '%Y/%m/%d %H:%M:%S')
    end_date = datetime.datetime.strptime(df[END][index], '%Y/%m/%d %H:%M:%S')
    mmod = monthmod(start_date, end_date)
    tmp_list = [name[:name.find(' ')], name, data, mmod[0].months + 1, ""]
    member_list.append(tmp_list)

for i in range(len(member_list)):
    for j in range(len(member_list)):
        if i != j:
            if member_list[i][4] == member_list[j][0]:
                member_list[i][4] = member_list[i][1]
                break
            else:
                member_list[i][4] = member_list[i][0]


f = open('./text/' + file_name + '.txt', 'w')
for member in member_list:

    f.writelines(
"""
◆%sさん
%s
→延長(36か月まで)*前回は%dか月延長でした。
→入替
→返却
"""
    % (member[4], member[2], member[3]))

f.close()



