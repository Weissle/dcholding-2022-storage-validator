import xlsxwriter
from collections import defaultdict
from common import result_readin,data_readin


# 官方示例中的， 每个拣货单包含的单据
def result_detail(sheet,input_data,result):
	sheet.write('A1','拣货单号')
	sheet.write('B1','订单编号')
	sheet.write('C1','货架编号')
	groups = [0]*100
	for group in result:
		gid = group['group_id']
		groups[gid-1] = group
	
	col_idx = 1
	for gid,group in enumerate(groups):
		for noid in group['idx']:
			for good_id in input_data[noid]:
				sheet.write(col_idx,0,str(gid+1))
				sheet.write(col_idx,1,str(noid))
				sheet.write(col_idx,2,str(good_id))
				col_idx += 1

def result_simple(sheet,input_data,result):
	sheet.write('A1','拣货单编号')
	sheet.write('B1','最小货架编号')
	sheet.write('C1','最大货架编号')
	sheet.write('D1','距离')
	groups = [0]*100
	for group in result:
		gid = group['group_id']
		groups[gid-1] = group
	for gid,group in enumerate(result):
		l = min(min(input_data[noid]) for noid in group['idx'])
		r = max(max(input_data[noid]) for noid in group['idx'])
		sheet.write(gid+1,0,str(gid+1))
		sheet.write(gid+1,1,l)
		sheet.write(gid+1,2,r)
		sheet.write(gid+1,3,group['cost'])


def main():
	workbook = xlsxwriter.Workbook('submit.xlsx')
	input1_data = data_readin('input1.txt')
	input2_data = data_readin('input2.txt')
	result1 = result_readin('result1.txt')
	result2 = result_readin('result2.txt')
	worksheet1 = workbook.add_worksheet('第一份单据-拣货单包含的单据')
	result_detail(worksheet1,input1_data,result1)
	worksheet2 = workbook.add_worksheet('第一份单据-每个拣货单的距离')
	result_simple(worksheet2,input1_data,result1)

	worksheet3 = workbook.add_worksheet('第二份单据-拣货单包含的单据')
	result_detail(worksheet3,input2_data,result2)
	worksheet4 = workbook.add_worksheet('第二份单据-每个拣货单的距离')
	result_simple(worksheet4,input2_data,result2)

	workbook.close()

if __name__ == '__main__':
	main()