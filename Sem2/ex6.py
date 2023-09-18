import turtle as tr
n = int(input())
tr.shape('turtle')
for i in range(n):
    tr.forward(80)
    tr.stamp()
    tr.left(180)
    tr.penup()
    tr.forward(80)
    tr.pendown()
    tr.left(180)
    tr.left(360/n)