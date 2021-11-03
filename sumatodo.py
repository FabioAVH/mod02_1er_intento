def sumatodos(limit):
    result=0
    for i in range(0,limit):
        result += i
    return result

print (sumatodos(100))