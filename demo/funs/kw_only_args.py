# keyword-only args
def fun(*, p1, p2):
    pass


#fun(10, 20)
fun(p1=10, p2=20)
fun(p2=100, p1=200)
