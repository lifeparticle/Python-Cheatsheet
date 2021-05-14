[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/lifeparticle/Python-Cheatsheet/issues)

Table of Contents
=================

   * [Installation](#installation)
      * [How to install python](#how-to-install-python)
   * [Comment](#comment)
   * [Operators](#operators)
      * [Logical operators](#logical-operators)
      * [Bitwise operators](#bitwise-operators)
      * [Arithmetic operators](#arithmetic-operators)
      * [Comparison operators](#comparison-operators)
      * [Assignment operators](#assignment-operators)
   * [Conditional structures](#conditional-structures)
      * [Ternary Operators](#ternary-operators)
   * [Data types](#data-types)
      * [How to check data type](#how-to-check-data-type)
      * [List](#list)
      * [Dictionary](#dictionary)
      * [Set](#set)
   * [map() Function](#map-function)
   * [filter() Function](#filter-function)
   * [reduce() Function](#reduce-function)
   * [zip() Function](#zip-function)
   * [format() function](#format-function)
   * [Miscellaneous](#miscellaneous)
      * [Get the number of bits in an integer in binary, excluding the sign and leading zeros.](#get-the-number-of-bits-in-an-integer-in-binary-excluding-the-sign-and-leading-zeros)
      * [Swap two variables in one line](#swap-two-variables-in-one-line)
   * [Books and other resources](#books-and-other-resources)
   * [Bug Reports and Feature Requests](#bug-reports-and-feature-requests)
   * [Author](#author)
   * [License](#license)

Installation
============

How to install python
-----
If you don't want to install python natively you can use [docker](https://www.docker.com/).
```
docker run -it --rm python:latest
# check which version of python you're running
python --version
```


Comment
============

```python
# single line comment

# begin
# multiline
# comment
# end
```

or
```python
"""
begin
multiline
comment
end
"""
```

Operators
============
Logical operators
-----
| No | operator |
|---|---|
| 1 | and   |
| 2 | or    |
| 3 | not   |
| 4 | &&    |
| 5 | \|\|  |
| 6 | !     |


Bitwise operators
-----
| No | operator |
|---|---|
| 1 | &     |
| 2 | \|    |
| 3 | ^     |
| 4 | ~     |
| 5 | <<    |
| 6 | >>    |

Arithmetic operators
-----
| No | operator |
|---|---|
| 1 | +     |
| 2 | -     |
| 3 | *     |
| 4 | /     |
| 5 | %     |
| 6 | **    |
| 7 | //    |

Comparison operators
-----
| No | operator |
|---|---|
| 1  | ==     |
| 2  | !=     |
| 3  | >      |
| 4  | <      |
| 5  | >=     |
| 6  | <=     |
| 7  | <>     |


Assignment operators
-----
| No | operator |
|---|---|
| 1 | =     |
| 2 | +=    |
| 3 | -=    |
| 4 | *=    |
| 5 | /=    |
| 6 | %=    |
| 7 | **=   |
| 8 | //=   |


Conditional structures
============

```python
x = 11
if x > 10:
    print("The number is greater than 10")
else:
    print("The number is not greater than 10")
```

```python
if x == 10:
    print('The value of x is 10')
elif x == 11:
    print('The value of x is 11')
else:
    print('The value of x is not either 10 or 11')
```

Ternary Operators
-----
```
execute_if_true if condition else execute_if_false
```

```python
print "even" if 6 % 2 == 0 else "odd"

# output
# even
```

Data types
============

| No | Type  | Example  | Class  | Type  |
|---|---|---|---|---|
| 1  | int        | > a = 17                           |> `a.__class__.__name__` <br> > 'int'        | Numeric Types         |
| 2  | float      | > a = 87.23                        |> `a.__class__.__name__` <br> > 'float'      | Numeric Types         |
| 3  | complex    | > a = 1j or > a = 1J               |> `a.__class__.__name__`` <br> > 'complex'    | Numeric Types         |
| 4  | str        | > a = "Hello universe"             |> `a.__class__.__name__` <br> > 'str'        | Text Sequence Type    |
| 5  | list       | > a = ["a", "b", "c"]              |> `a.__class__.__name__` <br> > 'list'       | Sequence Types        |
| 6  | tuple      | > a = ("a", "b", "c")              |> `a.__class__.__name__` <br> > 'tuple'      | Sequence Types        |
| 7  | range      | > a = range(7)                     |> `a.__class__.__name__` <br> > 'range'      | Sequence Types        |
| 8  | dict       | > a = {"name" : "Tom", "age" : 17} |> `a.__class__.__name__` <br> > 'dict'       | Mapping Types         |
| 9  | set        | > a = {"a", "b", "c"}              |> `a.__class__.__name__` <br> > 'set'        | Set Types             |
| 10 | frozenset  | > a = frozenset({"a", "b", "c"})   |> `a.__class__.__name__` <br> > 'frozenset'  | Set Types             |
| 11 | bool       | > a = True                         |> `a.__class__.__name__` <br> > 'bool'       | Boolean Types         |
| 12 | bytes      | > a = b"Hello universe"            |> `a.__class__.__name__` <br> > 'bytes'      | Binary Sequence Types |
| 13 | bytearray  | > a = bytearray(7)                 |> `a.__class__.__name__` <br> > 'bytearray'  | Binary Sequence Types |
| 14 | memoryview | > a = memoryview(bytes(7))         |> `a.__class__.__name__` <br> > 'memoryview' | Binary Sequence Types |


[Further readings](https://docs.python.org/3/library/stdtypes.html)


How to check data type
-----

```python
a = 37
isinstance(a, int)
# True
isinstance(a, float)
# False
```

```python
type(10)
# <type 'int'>
```

List
-----

```python
a = ["a", "b", "c"]

f, s, t = ["a", "b", "c"]
# output
# f = 'a'
# s = 'b'
# t = 'c'

f, *mid, l = ["a", "b", "c"]

# output
# f = 'a'
# mid = ['b']
# l = 'c'
```

```python
a = ["a", "b", "c"]
b = ["d", "e", "f"]

a.append(b)
# output
# ['a', 'b', 'c', ['d', 'e', 'f']]

a = ["a", "b", "c"]
b = ["d", "e", "f"]

a.extend(b)
# output
# ['a', 'b', 'c', 'd', 'e', 'f']
```

List slice

list[start_index:stop_index:step]

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers[0::2]

# output
# [1, 3, 5, 7, 9]


numbers[1::2]

# output
# [2, 4, 6, 8, 10]
```

List Comprehensions

Create a list of lists

```python
[[0]*2 for i in range(2)]

# output
# [[0, 0], [0, 0]]
```

Create a list of variable length of lists

```python
n = 10
[[0]*(i+1) for i in range(n)] + [[0]*i for i in range(n-1, 0, -1)]

# output
# [[0],
# [0, 0],
# [0, 0, 0],
# [0, 0, 0, 0],
# [0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0],
# [0, 0, 0, 0],
# [0, 0, 0],
# [0, 0],
# [0]]
```

Create a matrix of multiplication tables

```python
n = 5
[[i*j for i in range(1,n+1)] for j in range(1, n+1)]

# output
# [[1, 2, 3, 4, 5],
# [2, 4, 6, 8, 10],
# [3, 6, 9, 12, 15],
# [4, 8, 12, 16, 20],
# [5, 10, 15, 20, 25]]
```

Dictionary
-----

Dictionary Comprehensions

```python
{c: ord(c) - 96 for c in string.ascii_lowercase[:26]}

# output
# {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}
```

Set
-----

Set Comprehensions

```python
numbers = [2, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 11, 12, 13, 14]
uniqueEvenNumbers = {num for num in numbers if num % 2 == 0}

# output
# set([2, 4, 6, 8, 10, 12, 14])

uniqueNumbers = set(numbers)

# output
# set([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
```

map() Function
============

```python
map(function, list)
```

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda n: n*n, numbers))

# output
# [1, 4, 9, 16, 25]
```

filter() Function
============

```python
filter(function, list)
```

```python
numbers = [1, 2, 3, 4, 5]
odd = list(filter(lambda n: n % 2 != 0, numbers))

# output
# [1, 3, 5]
```

reduce() Function
============

```python
reduce(function, list)
```

```python
numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, numbers

# output
# 15
```

zip() Function
============

Creates an iterator of tuples.

```python
zip(iterator1, iterator2, iterator3 ...)
```

```python
a = ['a', 'b', 'c']
b = [1, 2, 3]

zip(a, b)

# output
# [('a', 1), ('b', 2), ('c', 3)]
```

tuples to list

```python
list(map(list, zip(a, b)))

# output
# [['a', 1], ['b', 2], ['c', 3]]
```

format() function
============

```python
"{:{width}.{prec}f}".format(10.344, width=10, prec=6)

# output
# ' 10.344000'
```


Miscellaneous
============

Get the number of bits in an integer in binary, excluding the sign and leading zeros.
-----

```python
n.bit_length()
```

Swap two variables in one line
-----

```python
a, b = b, a
```

My Python Articles
============
1. [How To Run a Python Script Using a Docker Container](https://towardsdatascience.com/how-to-run-a-python-script-using-a-docker-container-ea248e618e32)
2. [How To Create a Twitter Bot in Python](https://levelup.gitconnected.com/how-to-create-a-twitter-bot-in-python-bf49a384905f)
3. [How To Extract Text From Images Using Tesseract OCR Engine and Python](https://towardsdatascience.com/how-to-extract-text-from-images-using-tesseract-ocr-engine-and-python-22934125fdd5)
4. [How to Connect to a PostgreSQL Database With a Python Serverless Function](https://towardsdatascience.com/how-to-connect-to-a-postgresql-database-with-a-python-serverless-function-f5f3b244475)
5. [How to Deploy a Python Serverless Function to Vercel](https://towardsdatascience.com/how-to-deploy-a-python-serverless-function-to-vercel-f43c8ca393a0)

Books and other resources
============
1. TODO

Bug Reports and Feature Requests
============
Please create an issue with as much information you can. Thank you.

Author
============
Mahbub Zaman (https://mahbub.ninja)

License
============
MIT License
