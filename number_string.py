# 數字運算
x = 3+6
print(x)
x = 3-6
print(x)
x = 3*6
print(x)
x = 7/6
print(x)
x = 7//3 # 整數除法
print(x)
x = 2**3 # 次方 e.g. 2的3次方
print(x)
x = 2 ** 0.5 # 開根號
print(x)
x = 7%3 # 除餘數
print(x) 
# 字串運算 
s = "Hello" # 雙、單引號皆可
print(s)
s = "you\'re" # \ 為跳脫字符
print(s)
s = "Hello" + " World" # +為串接字符
print(s)
s = "Hello" " World" # 空白亦可串接
print(s)
s = "Hello\nWorld" # \n 換行
print(s)
s = """Hello  



World""" # """ """ 於變數中可直接換行
print(s)
s = "Hello"*3+"World" # Hello列印3次再加上World
print(s)

# 字串會對內部的字元編號(索引). 從 0 開始算起
s= "Hello"
print(s[0])
print(s[1:4]) # 取得字串索引1到3
print(s[1:]) # 取得字串索引從1到最後
print(s[:4]) # 取得字串索引從0到3