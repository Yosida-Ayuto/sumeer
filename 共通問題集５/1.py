from multiprocessing.sharedctypes import Value


print('A~Dの値を入力してください')
value = str(input())

if value == 'A':
    print('ランクAは評価「優」です。')
elif value == 'B':
    print('ランクＢは評価「良」です。')
elif value == 'C':
    print('ランクCは評価「可」です。')
elif value == 'D':
    print('ランクDは評価「不可」です。')
else:
    print('A~D以外を入力しないでください')