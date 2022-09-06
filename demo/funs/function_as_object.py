def fun():
    print("Function fun()")


fun2 = fun  # copy address of function to another variable

print(id(fun), type(fun))

fun()
fun2()
