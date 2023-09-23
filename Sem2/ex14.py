import turtle as tr
tr.shape('turtle')
def zvd(n: int):
    f = 180 - ((360/n)/2)
    for i in range(n):
        tr.forward(70)
        tr.right(f)
zvd(5)
tr.penup()
tr.goto(90, 0)
tr.pendown()
zvd(11)
tr.done()