## Problems

**1. Write a function with the following signature:** `pythagoreanTheorem(length_a, length_b)`. Find the code [here](code/Q1.py)

The function returns the length of the hypotenuse assuming that `length_a` and `length_b` are the lengths of the two legs of a right triangle (the legs that form the triangle's right angle). Hint: the `math` module might have useful functions to use.


``` 
CODE:
import math
def pythagoreanTheorem(length_a, length_b):
    return math.sqrt(length_a ** 2 + length_b ** 2)      #squareroot(square(a)+square(b))
    
    
EXAMPLES:
1.)pythagoreanTheorem(2,1)
    2.23606797749979
2.)pythagoreanTheorem(3,4)
    5.0
3.)pythagoreanTheorem(5,7)
    8.602325267042627



```


**2. Write a function with the following signature:** `list_mangler(list_in)`.

The function assumes that `list_in` is a list of integers, and returns a new list containing transformed elements of `list_in`. If the element is even, it's doubled. If the element is odd, it's tripled.


```
CODE:
def list_mangler(list_in):
    result=[]
    for i in list_in:
        if i%2==0:                  # if list element is even then double the element
            result.append(i*2)
        elif i%2==1:                # if list element is odd then triple the element
            result.append(i*3)
    return result


EXAMPLES :
1.)list_mangler([1,2,3,4])
   [3, 4, 9, 8]
2.)list_mangler([5,8,14,37])
   [15, 16, 28, 111]
3.)list_mangler([-12,-4,-3])
   [-24, -8, -9]



```
In your solution markdown, please provide: a link to the .py file, a commented code, the output of a few examples (3-4).

**3. Write a function with the following signature:** `grade_calc(grades_in, to_drop)`.

The function accepts a list `grades_in` containing integer grades, drops the `to_drop` lowest grades (so, for `to_drop` equal to 2, the function should drop the 2 lowest grades), calculates the average of the grades left, and returns the letter grade this average corresponds to according to the letter grade scale for this course.


```
CODE:
def grade_calc(grades_in, to_drop):
    grades_in.sort(reverse=True)
    for i in range(to_drop):
        grades_in.pop()
    avg=sum(grades_in)/len(grades_in)
    if avg>=90 and avg<=100:
        grade='A'
    elif avg>=80 and avg<90:
        grade='B'
    elif avg>=70 and avg<80:
        grade='C'
    elif avg>=60 and avg<70:
        grade='D'
    elif avg<60:
        grade='F'
    return grade
    
    
    
EXAMPLES:
1.)grade_calc([67,87,45,34,98,89,56,76,90],3)
'B'
2.)grade_calc([100, 90, 80, 95], 2)
'A'
3.)grade_calc([34,56,78,43],2)
'D'
```
In your solution markdown, please provide: a link to the .py file, a commented code, the output of a few examples (3-4).


**4. Write a function with the following signature:** `odd_even_filter(numbers)`.

The function accepts an input list of integers and returns a list with two sublists. The first sublist contains all even numbers in the input list and the second sublist contains all odd numbers.

```
CODE :
def odd_even_filter(numbers):
    even,odd=[],[]
    for i in numbers:
        if i%2==0:
            even.append(i)
        elif i%2==1:
            odd.append(i)
    return [even,odd]
    
    
    
 EXAMPLES :
 1.)odd_even_filter([1, 2, 3, 4, 5, 6, 7, 8, 9])
    [[2, 4, 6, 8], [1, 3, 5, 7, 9]]
 2.)odd_even_filter([3, 9, 43, 7])
    [[], [3, 9, 43, 7]]
 3.)odd_even_filter([71, 39, 98, 79, 5, 89, 50, 90, 2, 56])
[[98, 50, 90, 2, 56], [71, 39, 79, 5, 89]]



```
