## Problems

**1. Write a function with the following signature:** `pythagoreanTheorem(length_a, length_b)`.

The function returns the length of the hypotenuse assuming that `length_a` and `length_b` are the lengths of the two legs of a right triangle (the legs that form the triangle's right angle). Hint: the `math` module might have useful functions to use.


``` CODE:
import math
def pythagoreanTheorem(length_a, length_b):
    Csquare = (length_a ** 2) + (length_b ** 2)
    length_c = math.sqrt(Csquare)
    return length_c
a = float(input('length_a:'))
b = float(input('length_b:'))
test1 = pythagoreanTheorem(a, b)
print("Length C is", test1, end=' ')
[HERE](C:\Users\Vaishnavi\AppData\Roaming\JetBrains\PyCharmCE2022.2\scratches\pythagorean.py)  IS THE LINK TO .py FILE 
~~ EXAMPLES ~~
1)
length_a:4
length_b:2
Length C is 4.47213595499958 
2)
length_a:3
length_b:4
Length C is 5.0 
3)
length_a:1
length_b:2
Length C is 2.23606797749979 
4)
length_a: 2
length_b: 5
Length C is 5.385164807134504 


```
In your solution markdown, please provide: a link to the .py file, a commented code, the output of a few examples (3-4).

**2. Write a function with the following signature:** `list_mangler(list_in)`.

The function assumes that `list_in` is a list of integers, and returns a new list containing transformed elements of `list_in`. If the element is even, it's doubled. If the element is odd, it's tripled.

For example:

```python
print(list_mangler([1, 2, 3, 4]))
[3, 4, 9, 8]
```
In your solution markdown, please provide: a link to the .py file, a commented code, the output of a few examples (3-4).

**3. Write a function with the following signature:** `grade_calc(grades_in, to_drop)`.

The function accepts a list `grades_in` containing integer grades, drops the `to_drop` lowest grades (so, for `to_drop` equal to 2, the function should drop the 2 lowest grades), calculates the average of the grades left, and returns the letter grade this average corresponds to according to the letter grade scale for this course.

For example:

```
print(grade_calc([100, 90, 80, 95], 2)) # drops the 2 lowest grades (80 and 90)
'A'
```
In your solution markdown, please provide: a link to the .py file, a commented code, the output of a few examples (3-4).


**4. Write a function with the following signature:** `odd_even_filter(numbers)`.

The function accepts an input list of integers and returns a list with two sublists. The first sublist contains all even numbers in the input list and the second sublist contains all odd numbers.

For example:
```
print(odd_even_filter([1, 2, 3, 4, 5, 6, 7, 8, 9]))
[[2, 4, 6, 8], [1, 3, 5, 7, 9]]
print(odd_even_filter([3, 9, 43, 7]))
[[], [3, 9, 43, 7]]
print(odd_even_filter([71, 39, 98, 79, 5, 89, 50, 90, 2, 56]))
[[98, 50, 90, 2, 56], [71, 39, 79, 5, 89]]
```
