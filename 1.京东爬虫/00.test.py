import pandas as pd
data={
  
    'A':[1,0,1,1],
    'B':[0,2,5,0],
    'C':[4,0,4,4],
    'D':[1,0,1,1]
}
df=pd.DataFrame(data=data)
#默认保留第一次出现的重复项
data = pd.DataFrame()
data['a'] = df['A']
print(data)