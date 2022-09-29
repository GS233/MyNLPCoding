import pandas as pd


df = pd.read_csv('102.JDcomments.csv')

print(df)
# df=pd.DataFrame(data=data)
#默认保留第一次出现的重复项
data = df.drop_duplicates()

# 
data.columns = ['评论','评分']
print([column for column in data])

data.to_csv('100去重.csv', encoding='utf8',index=False) 

print(data)
