print('税込み価格を求めます')
print('定価:',end='')
price= int(input())
print('消費税率:',end='')
tax=int(input())
tax2=tax*0.01
print('定価:',price)
print('消費税率:',tax)
print('税込み価格 =', price + (price * tax2))
