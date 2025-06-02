def fun(nun):
    if nun == 1:
        return 1
    else:
        return nun * fun(nun - 1)
print(fun(5))