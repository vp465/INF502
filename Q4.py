def odd_even_filter(numbers):
    even,odd=[],[]
    for i in numbers:
        if i%2==0:
            even.append(i)
        elif i%2==1:
            odd.append(i)
    return [even,odd]

odd_even_filter([1, 2, 3, 4, 5, 6, 7, 8, 9])
#odd_even_filter([3, 9, 43, 7])
#odd_even_filter([71, 39, 98, 79, 5, 89, 50, 90, 2, 56])
