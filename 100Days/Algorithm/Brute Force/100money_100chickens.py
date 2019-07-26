'''
穷举法：

百钱买百鸡：
  公鸡5元一只 母鸡3元一只 小鸡1元三只
  用100元买100只鸡 问公鸡/母鸡/小鸡各多少只
'''
for i in range(0,21):
        for j in range(0,34):
                for k in range(0,301,3):
                        if i+j+k==100 and 5*i+3*j+k/3==100:
                                print(i,j,k)
for i in range(0,21):
        for j in range(0,34):
                k = 100 - i - j
                if k%3==0 and 5*i+3*j+k//3==100:
                        print(i,j,k)
