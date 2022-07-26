import random 

print('【計算式】')
value1 = random.random()
value2 = random.random()
value3 = random.random()
value4 = random.random()


print(value1,"+",value2,"-",value3,"×",value4)

sum = value1 + value2 + value3 + value4

print('計算結果は？')
ansewr = int(input())

if ansewr == sum:
    print('正解です！！')

else:
    print('不正解です。正解は',sum,'です。')