import turtle as tr
tr.shape('turtle')
tr.speed(1)
with open('C:\\Users\\Kirill\\sems\\Sem3\\moving.txt', 'r') as f:
    mv = f.read().split('\n')
def x0(i, j):
    for k in range(0, 7):
        eval(mv[k])
def x1(i, j):
    for k in range(8, 18):
        eval(mv[k])
def x2(i, j):
    for k in range(19, 28):
        eval(mv[k])
def x3(i, j):
    for k in range(29, 38):
        eval(mv[k])
def x4(i, j):
    for k in range(39, 49):
        eval(mv[k])
def x5(i, j):
    for k in range(50, 61):
        eval(mv[k])
def x6(i, j):
    for k in range(62, 75):
        eval(mv[k])
def x7(i, j):
    for k in range(76, 84):
        eval(mv[k])
def x8(i, j):
    for k in range(85, 96):
        eval(mv[k])
def x9(i, j):
    for k in range(97, 110):
        eval(mv[k])
def cfr(k, i, j):
    if k == 0:
        x0(i, j)
    if k == 1:
        x1(i, j)
    if k == 2:
        x2(i, j)
    if k == 3:
        x3(i, j)
    if k == 4:
        x4(i, j)
    if k == 5:
        x5(i, j)
    if k == 6:
        x6(i, j)
    if k == 7:
        x7(i, j)
    if k == 8:
        x8(i, j)
    if k == 9:
        x9(i, j)
list = list(map(int, input().split()))
i = 0
j = 0
for k in list:
    cfr(k, i, j)
    i += 100
tr.done()
