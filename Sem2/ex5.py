import turtle as tr
tr.shape('turtle')
i = 0
while i < 181:
    tr.forward(50+i)
    tr.left(90)
    tr.forward(50+i)
    tr.left(90)
    tr.forward(50+i)
    tr.left(90)
    tr.forward(50+i)
    tr.penup()
    tr.forward(10)
    tr.right(90)
    tr.forward(10)
    tr.left(180)
    tr.pendown()
    i += 20


