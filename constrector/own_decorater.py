def smart_div(fun):   #address of the div function
    def inner (a,b):
        if a<b:
            a,b=b,a
            return fun(a,b)
    return inner
@smart_div
def div(a,b):
    print(a/b)
div(2,4)
