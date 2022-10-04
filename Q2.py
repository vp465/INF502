def list_mangler(list_in):
    result=[]
    for i in list_in:
        if i%2==0:                  # if list element is even then double the element
            result.append(i*2)
        elif i%2==1:                # if list element is odd then triple the element
            result.append(i*3)
    return result
