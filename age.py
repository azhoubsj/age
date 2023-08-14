driving = input('请问你有没有开过车?')
if driving != '有' and driving != '没有':
	print('只能输入  有/没有')
	raise SystemExit

age = input('请问你的年龄?')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通过测验啦')
	else:
		print('小屁孩怎么可能开过车')
elif driving == '没有':
	if age >= 18:
		print('那你可以去学车啊')
	else:
		print('再过几年就可以学车了')