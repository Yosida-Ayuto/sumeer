print('0~100までの点数を2つ入力してください')
print('国語の得点:',end='')
x = int(input())
print('英語の得点',end='')
y=int(input())



if x >=80 :
    if y >=80:
        print('2科目とも合格です')
    else :
        print('')
else:
    print('')