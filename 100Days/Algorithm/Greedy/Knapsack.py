'''
贪婪法

0-1背包问题（小偷在偷的时候没时间算那么精确，快速的找到满意解就可以了，不一定是最优解）

测试用例：
20 6
电脑 200 20
收音机 20 4
钟 175 10
花瓶 50 2
书 10 1
油画 90 9
'''

class Thing(object):
    def __init__(self, name, price, weight):
        self._name = name
        self._price = price
        self._weight = weight

    @property
    def value(self):
        return self._price/self._weight

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def weight(self):
        return self._weight

def input_things():
    name_str, price_str, weight_str = input('请输入物品 名称 价格 重量（以空格隔开）：').split(' ')
    return name_str, int(price_str), int(weight_str)

def main():
    max_weight, total_things = map(int, input('请输入背包的最大重量 物品总数：').split(' '))
    all_things = []
    for _ in range(total_things):
        all_things.append(Thing(*input_things()))

    all_things.sort(key=lambda x:x.value,reverse=True)  # 按照价值排序
    
    total_weight,total_price = 0,0
    for thing in all_things:
        if total_weight+thing.weight<max_weight:
            print(f'小偷偷走了{thing.name}')
            total_weight += thing.weight
            total_price += thing.price
    print(f'小偷偷的总价值为{total_price}')

if __name__ == "__main__":
    main()
