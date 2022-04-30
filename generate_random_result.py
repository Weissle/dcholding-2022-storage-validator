import os
import sys
from collections import defaultdict
import random

if __name__ == "__main__":
	if(len(sys.argv) != 2):
		print('参数个数不正确，用法  python validator.py {INPUT_FILE} ')
		print('INPUT_FILE 应该是 input1.txt 或 input2.txt')
		exit(0)
	input_file = sys.argv[1]

	order_min,order_max = defaultdict(lambda : 10000000),defaultdict(lambda : 0)
	orders_no = []
	with open(input_file,'r') as f:
		for line,tmp in enumerate(f):
			if tmp.strip() == '':
				continue
			tmp = tmp.split(' ')
			if(len(tmp) != 2):
				print(f'输入文件出错，大概位置在{line+1}行')
				exit(1)
			no,idx = int(tmp[0]),int(tmp[1])
			order_min[no] = min(order_min[no],idx)
			order_max[no] = max(order_max[no],idx)
			orders_no.append(no)
	assert(len(order_min) == 2000)
	assert(len(order_max) == 2000)

	orders_no = list(set(orders_no))
	random.shuffle(orders_no)
	output = open('result.txt','w+')
	for i in range(100):
		l,r = 10000000 , 0
		for j in range(i*20,(i+1)*20):
			no = orders_no[j]
			l = min(l,order_min[no])
			r = max(r,order_max[no])
		cost = r-l
		output.write(f'{i+1} {cost}\n')
		for j in range(i*20,(i+1)*20):
			output.write(f'{orders_no[j]}\n')
		output.write('\n')
	output.close()

