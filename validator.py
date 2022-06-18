import os
import sys
from collections import defaultdict
from common import result_readin,data_readin

if __name__ == "__main__":
	if(len(sys.argv) != 3):
		print('参数个数不正确，用法  python validator.py {INPUT_FILE} {RESULT_FILE}')
		print('INPUT_FILE 应该是 input1.txt 或 input2.txt')
		print('RESULT_FILE 是结果文件')
		exit(0)
	input_file = sys.argv[1]
	result_file = sys.argv[2]

	data_input = data_readin(input_file)
	groups = result_readin(result_file)
	
	used = set()
	for group in groups:
		used |= set(group['idx'])
	assert(len(used) == 2000)

	for g in groups:
		l = min(min(data_input[noid]) for noid in g['idx'])
		r = max(max(data_input[noid]) for noid in g['idx'])
		if r-l != g['cost']:
			groud_id = g['group_id']
			print(f'错误，第{groud_id}开销不一致. ')
			exit(1)
	total_cost = 0
	for g in groups:
		total_cost += g['cost']
	print(f'输出正确，开销为{total_cost}')