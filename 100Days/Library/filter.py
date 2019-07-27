# filter -> 过滤器

## 留下奇数, 过滤掉偶数
def odd(num):
    return num%2==1
li = list(filter(odd,range(1,10)))
print(li)
## 留下偶数
it = filter(lambda x: not x%2, range(1,10))
while True:
    try:
        print(next(it))
    except StopIteration:
        break;

## 过滤掉None和空字符串
strarr = ['nihao',None,'这是','好',' ','    ','hello']
filtered_strarr = filter(lambda str: str and len(str.strip())>0, strarr)
print(list(filtered_strarr))
