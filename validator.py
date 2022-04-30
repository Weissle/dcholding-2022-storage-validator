import os
import sys
from collections import defaultdict
import random

if __name__ == "__main__":
	if(len(sys.argv) != 3):
		print('参数个数不正确，用法  python validator.py {INPUT_FILE} {RESULT_FILE}')
		print('INPUT_FILE 应该是 input1.txt 或 input2.txt')
		print('RESULT_FILE 是结果文件')
		exit(0)
	input_file = sys.argv[1]
	result_file = sys.argv[2]

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

	groups = []
	with open(result_file,'r') as f:
		cnt = 0
		d = {}
		for line,tmp in enumerate(f):
			tmp = tmp.strip()
			if tmp.strip() == '':
				continue
			if cnt == 0:
				tmp = tmp.split(' ')
				if(len(tmp) != 2):
					print(f'输入文件出错，大概位置在{line+1}行')
					exit(1)
				d = {'group_id':int(tmp[0]),'cost':int(tmp[1]),'idx':[]}
			else:
				no = int(tmp)
				d['idx'].append(no)
			cnt+=1
			if cnt==21:
				groups.append(d)
				cnt = 0
	
	used = set()
	for g in groups:
		l,r = 30000000000,0
		for idx in g['idx']:
			if idx in used:
				print(f'错误，{idx}这个订单已经再之前出现过. ')
				exit(1)
			elif idx not in order_min:
				print(f'错误，{idx}这个订单不在输入中. ')
				exit(1)
			used.add(idx)
			l = min(l,order_min[idx])
			r = max(r,order_max[idx])
		if r-l != g['cost']:
			groud_id = g['group_id']
			print(f'错误，第{groud_id}开销不一致. ')
			exit(1)
	total_cost = 0
	for g in groups:
		total_cost += g['cost']
	print(f'输出正确，开销为{total_cost}')