import csv

path='102去重.csv'
with open(path,encoding='utf-8') as fin:
    with open('103去行.csv','w',newline='',encoding='utf-8') as fout:
        r = csv.reader(fin) # 读入文件
        w = csv.writer(fout) # 写入文件
        for row in r:
            row = [col.replace('\n', '').replace('\r', '') for col in row] # 将"\n"替换为无
            w.writerow(row) # 写入新文件