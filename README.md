# Python-Cheatsheet

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
True
isinstance(a, float)
False
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
