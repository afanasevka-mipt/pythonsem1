import turtle as tr
tr.shape('turtle')
tr.speed(0)
tr.left(90)
for i in range(10):
    for k in range(1, 361):
        tr.forward(0.3+i*0.1)
        tr.left(1)
    for k in range(1, 361):
        tr.forward(0.3+i*0.1)
        tr.right(1)