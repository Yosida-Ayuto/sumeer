print('BMIを求めます')
print('身長(cm):',end='')
height= int(input())
print('体重(kg):',end='')
weight=int(input())
bmi = weight/height**2*10000
print('BMI値 =', bmi)
