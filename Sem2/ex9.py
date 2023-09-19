import turtle as tr
tr.shape('turtle')
def ngran(n: int):
    for i in range(n):
        tr.forward(n*10)
        tr.left(360/n)
for i in range(3, 13):
    ngran(i)
    tr.right(135)
    tr.penup()
    tr.forward(10)
    tr.pendown()
    tr.left(135)
tr.done()


    



