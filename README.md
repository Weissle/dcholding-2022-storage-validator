# dcholding-2022-storage-validator
神州控股校园极客大赛2022 仓库拣货策略策略 验题器。  
自动检查是否所有的订单都分配到拣货单中，是否有订单重复出现，是否出现拣货单的开销计算失误，以及计算输出的开销。

## 使用
`python validator.py input1.txt output1.txt`

## 随机生成结果数据
`python generate_random_result.py input1.txt`  
注意，结果是完全随机出来的，因此开销可能非常的大，只是为了展示结果文件的格式！

## 结果文件格式
```
{group_number1} {cost1}
{order_no1}
{order_no2}
...
{order_no20}

{group_number2} {cost2}
...
```
每一组都由21行组成，第一行为组序号和组开销，序号从0开始或者从1开始都可以，开销为该组的开销。
下面第二行到第二十一行，则为每一个订单的编号。
