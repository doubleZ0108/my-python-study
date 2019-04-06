from queue import Queue

print("请输入杨辉三角的行数")
MaxSize = input()

Q = Queue()
Q.put(1)
Q.put(1)

leftup = 0

for i in range(1,int(MaxSize)+1):
	Q.put(0)
	for j in range(0,i+2):
		up = Q.get()
		Q.put(up+leftup)
		
		if j != i+1:
			print(up,end=" ")
		leftup = up
		
	print('\n')
