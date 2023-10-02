import turtle as tr
tr.shape('turtle')
tr.speed(1)
def x0(i, j):
    tr.goto(i+50, j)
    tr.goto(i+50, j-100)
    tr.goto(i, j-100)
    tr.goto(i, j)
    tr.penup()
    tr.goto(i+100, j)
    tr.pendown()
def x1(i, j):
    tr.penup()
    tr.goto(i, j-50)
    tr.pendown()
    tr.goto(i+50, j)
    tr.goto(i+50, j-100)
    tr.penup()
    tr.goto(i, j)
    tr.penup()
    tr.goto(i+100, j)
    tr.pendown()
def x2(i, j):
    tr.goto(i+50, j)
    tr.goto(i+50, j-50)
    tr.goto(i, j-100)
    tr.goto(i+50, j-100)
    tr.penup()
    tr.goto(i, j)
    tr.penup()
    tr.goto(i+100, j)
    tr.pendown()
def x3(i, j):
    tr.goto(i+50, j)
    tr.goto(i, j-50)
    tr.goto(i+50, j-50)
    tr.goto(i, j-100)
    tr.penup()
    tr.goto(i, j)
    tr.penup()
    tr.goto(i+100, j)
    tr.pendown()
def x4(i, j):
    tr.goto(i, j)
    tr.goto(i, j-50)
    tr.goto(i+50, j-50)
    tr.goto(i+50, j)
    tr.goto(i+50, j-100)
    tr.penup()
    tr.goto(i, j)
    tr.penup()
    tr.goto(i+100, j)
    tr.pendown()
def x5(i, j):
    tr.goto(i+50, j)
    tr.goto(i, j)
    tr.goto(i, j-50)
    tr.goto(i+50, j-50)
    tr.goto(i+50, j-100)
    tr.goto(i, j-100)
    tr.penup()
    tr.goto(i, j)
    tr.penup()
    tr.goto(i+100, j)
    tr.pendown()
def x6(i, j):
    tr.penup()
    tr.goto(i+50, j)
    tr.pendown()
    tr.goto(i, j-50)
    tr.goto(i+50, j-50)
    tr.goto(i+50, j-100)
    tr.goto(i, j-100)
    tr.goto(i, j-50)
    tr.penup()
    tr.goto(i, j)
    tr.penup()
    tr.goto(i+100, j)
    tr.pendown()
def x7(i, j):
    tr.goto(i+50, j)
    tr.goto(i, j-50)
    tr.goto(i, j-100)
    tr.penup()
    tr.goto(i, j)
    tr.penup()
    tr.goto(i+100, j)
    tr.pendown()
def x8(i, j):
    tr.goto(i+50, j)
    tr.goto(i+50, j-100)
    tr.goto(i, j-100)
    tr.goto(i, j)
    tr.goto(i, j-50)
    tr.goto(i+50, j-50)
    tr.penup()
    tr.goto(i, j)
    tr.penup()
    tr.goto(i+100, j)
    tr.pendown()
def x9(i, j):
    tr.goto(i+50, j)
    tr.goto(i+50, j-50)
    tr.goto(i, j-50)
    tr.goto(i, j)
    tr.penup()
    tr.goto(i+50, j-50)
    tr.pendown()
    tr.goto(i, j-100)
    tr.penup()
    tr.goto(i, j)
    tr.penup()
    tr.goto(i+100, j)
    tr.pendown()
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

    
    
