import turtle as tr
tr.shape('turtle')
n, k = 1, 1
for i in range(3):
    for k in range(1, 361):
        tr.forward(1)
        tr.left(1)
    for k in range(1, 361):
        tr.forward(1)
        tr.right(1)
    tr.left(60)
tr.done(n)

