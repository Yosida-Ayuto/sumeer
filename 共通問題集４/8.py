print('0~100までの得点を入力してください')
print('1つ目の得点:',end='')
x = int(input())
print('2つ目の得点',end='')
y=int(input())

if x >=60 :
    if y >= 60:
        print('合格です')
    else:
        print('不合格です')
else:
    print('不合格です')