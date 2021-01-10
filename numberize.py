



def multiply(numberr):

    nums = []

    for i in range(1000):
        nums.append(i)
    numberr = int(numberr)

    first = []
    last = []

    cache = []

    Gamidia = False


    for num in nums:
        for number in nums:
            if num * number == numberr:
                first.append(num)
                last.append(number)

    for num in last:
        if num <= 5:
            if num != 1:
                cache.append(num)

    cache.sort()

    try:
        closest = min(cache, key=lambda x:abs(x-numberr))
    except ValueError:
        numberr -= 1
        first = []
        last = []
        cache = []
        for num in nums:
            for number in nums:
                if num * number == numberr:
                    first.append(num)
                    last.append(number)

        for num in last:
            if num <= 5:
                if num != 1:
                    cache.append(num)
        cache.sort()
        closest = min(cache, key=lambda x:abs(x-numberr))
        Gamidia = True


    if Gamidia:
        return[int(first[int(last.index(closest))]), int(closest), 1]
    else:
        return[int(first[int(last.index(closest))]), int(closest)]

