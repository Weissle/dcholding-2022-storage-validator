# dcholding-2022-storage-validator
神州控股校园极客大赛2022 仓库拣货策略策略 验证器。  
&emsp;&emsp;自动检查是否所有的订单都分配到拣货单中，是否有订单重复出现，是否出现拣货单的开销计算失误，以及计算输出的开销。
`input1.txt`和`input2.txt`是官方给予的两个输入数据。  
:warning: 这个**不**是官方验证器。本判题器为了方便要求的格式为txt，官方提交要求的是excel的格式。

## 使用
### 验证数据
`python validator.py input1.txt output1.txt`  
第一个参数为输入数据，一般是input1.txt或input2.txt，如果你自己造了数据也可以使用自己的数据为输入。  
第二个参数为你自己程序的结果，格式见解释或者result.txt。  

### 生成提交的excel文件
要求装有python库xlsxwriter `pip install xlsxwriter`.  
输出的结果1和2分别命名为 result1.txt,result2.txt。  
`python submit_generate.py`,结果保存在`submit.xlsx`


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
&emsp;&emsp;每一组都由21行组成，第一行为组序号和组开销，序号从0开始或者从1开始都可以，开销为该组的开销。
下面第二行到第二十一行，则为每一个订单的编号。

---
:heart: 如果这个验证器对你有帮助的话，希望给个:star:.  
:smile: 如果有错误与不足，欢迎pull request.
