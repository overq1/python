import math

amount  = raw_input()
payment = raw_input()
change_remain  = int(payment) - int(amount)

money_list = [5000, 2000, 1000, 500, 100, 50, 10, 5, 1]
change_dict = {}
for money_unit in money_list:
	change_dict[money_unit] = change_remain / money_unit
	change_remain = change_remain % money_unit

for k, v in sorted(change_dict.items()):
	print(str(k) + "=>" + str(v))

