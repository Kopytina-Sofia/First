result = []
def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    if type(key) != int:
        raise TypeError
    return a/b

try:
    data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}
    for key in data:
        res = divider(key, data[key])
        result.append(res)
        print(result)

except IndexError as indexerror:
    print(indexerror)
except ValueError as valueerror:
    print(valueerror)
except TypeError as typeerror:
    print(typeerror)

'''except (TypeError,IndexError,ValueError) as error:
   print(error)'''