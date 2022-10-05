def odd_even_filter(numbers):
    even,odd=[],[]
    for i in numbers:
        if i%2==0:
            even.append(i)
        elif i%2==1:
            odd.append(i)
    return [even,odd]


