print('ハンバーガー:',end='')
hanbager = int(input())
print('シェイク:',end='')
seiku = int(input())
print('コーラ：',end='')
cook = int(input())

sum = hanbager + seiku 
sum = sum + cook
tax = sum *0.1
chip = sum *0.16
value = sum + tax + chip


print('合計額(税金):',sum)
print('消費税',tax)
print('チップ',chip)
print('合計額(税込み)',value)


