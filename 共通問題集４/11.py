print('数値を4桁を西暦を入力してください')

x=int(input())
if(x%4==0):
    if(x%100==0):
        if(x%400 == 0):
            print('閏年です')
        else:
            print('平年です')
    else:
        print('平年です')
