from collections import defaultdict

def data_readin(path):
	data_input = defaultdict(list)
	with open(path,'r') as f:
		for line,tmp in enumerate(f):
			if tmp.strip() == '':
				continue
			tmp = tmp.split(' ')
			if(len(tmp) != 2):
				print(f'输入文件出错，大概位置在{line+1}行')
				exit(1)
			no,idx = int(tmp[0]),int(tmp[1])
			data_input[no].append(idx)
	assert(len(data_input) == 2000)
	return data_input

def result_readin(path):
	groups = []
	with open(path,'r') as f:
		cnt,d = 0, {}
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
	return groups
