
# Python functional programming 

a programming paradigm is a way for us to think about our code and organize our code, we want to tackle this idea of functional programming, we have to think like programmers and understand that there is tradeoffs 



### functional programming 

functinal programming is all about separation of concerns, which object oriented programming does as well 


it is all about packaging our code into separate chunks . and each part is organized in a way that makes sense based on functionality, we mean each part concerned the self wit hone thing taht it's good at

instead of combining mehtods and attributes, we separate them up because they are two separate things 

there is data and this data gets interacted and acted upon 
but generally functional languages have an emphasis on simplicity where data and functions are concerned becaues in most functional programming paradigms, we do not have this idea of classes and objects 

instead, functions operate on well-defined data structures like lists and dictionaries that we saw. the idea is to make our code clean and understandable and maintable. 


### Pure functions

##### the core of functional programming is pure functions 



think of a box as a simple function, it should always return the same output, a function should not produce any side effect, not printing anything 

let's give it a go


```python 
>>> def multiple_by_two(li):
...     new_list = []
...     for item in li:
...             new_list.append(item * 2)
...     return new_list
... 
>>> 

```
no matter how many times I run this, it is going to give me the same output 



the below interacts with outside world which is the print statement, we do not know what print statement does when it interacts with the screen.

we we have a new list outside the function, the new list interacts with the outside world 



```python 

>>> 
>>> def multiple_by_two(li):
...     new_list = []
...     for item in li:
...             new_list.append(item * 2)
...     return print(new_list)
## or this 

new_list = []
>>> def multiple_by_two(li):
...     
...     for item in li:
...             new_list.append(item * 2)
...     return print(new_list)
new_list = ''
# now this list is a string object 



```

so ideally we contain our function anything pure, because we will never have a bug or something wrong here, when you have pure functions, you will have less buggy code 

pure function is more of a guideline than an absolute, it is impossible to have pure functions everywhere because if a function does not affect the outside world at all, we would not be able to save things 


### map() function 
map actually allows us to simplify the code we have 

```python 
map(function, iterables)

map_result = iterable_type(map(function, iterables))

```
make an iterator that computes the function using arguments from each of the iterables. stops when the shortest iterable is exhausted 

map() gives us the object that it has created in this memory. in order for us to view it, we have to turn it to a iterable similar to range() 

```python

>>> def multiple_by_two(value):
...     return value * 2 
... 
>>> map(multiple_by_two,[1,2,3,4,5])<map object at 0x7fae79f1a9a0>
>>> print(map(multiple_by_two,[1,2,3,4,5]))
<map object at 0x7fae79f1abb0>
>>> 
>>> print(list(map(multiple_by_two,[1,2,3,4,5])))
[2, 4, 6, 8, 10]

>>> print(tuple(map(multiple_by_two,(1,2,3,4,5,6,7,8,9))))
(2, 4, 6, 8, 10, 12, 14, 16, 18)
```

run the function, loops through all the items in the iterable and returns for us a new map object thta we are going to convert into a iterable,
map allows us to create a whole new list that does not affect my list 







### filter() function 

it filters things for us, it filters some of our result 

```python 

def function(one_parameter_for_iterable_tem):
    return condition 

filter(function, iterables)

filter_result = iterable_type(filter(function, iterables))


```

```python 

>>> def greater_than_2(item):
...     return item > 2
... 
>>> list(filter(greater_than_2, [1,2,3,4,5,6,7]))
[3, 4, 5, 6, 7]

```



### zip() function 
zip() function works like a zipper, zip grabs two iterables and grabs the first item from the first from each, and zip them together 


we need two iterables and we can zip them together, it can be any iterable combination 


```python 
zip(iterables, iterables, iterables)

```

```python 

>>> list1 = [1,2,3]
>>> list2 = [3,4,5]
>>> list(zip(list1,list2))
[(1, 3), (2, 4), (3, 5)]
>>> 
>>> list1 = [1,2,3]
>>> tuple1 = (6,7,8)
>>> list(zip(list1,tuple1))
[(1, 6), (2, 7), (3, 8)]
>>> 

>>> list1 = [100, 200, 300]
>>> list2 = [400, 500, 600, 700]
>>> list(zip(list1,list2))
[(100, 400), (200, 500), (300, 600)]
>>> 

>>> list1 = [100, 200, 300]
>>> list2 = [400, 500, 600, 700]
>>> tuple1 = (6,7,8)
>>> list(zip(list1,list2,tuple1))
[(100, 400, 6), (200, 500, 7), (300, 600, 8)]
```

because it is so generic, can be used in so many different ways 
we do not modify our current data, we create a whole new one 





### reduce() function 


###### reduce does not come with python standard library, we have to "from functools import reduce"

```python

reduce(function, sequence, initial_value_for_result )

```
reduce() will be in charge of giving these two parameters from the data that we give it 


```python 

>>> from functools import reduce
>>> def accumulator(initial_value, next_item):
...     print(initial_value, next_item)
...     return initial_value + next_item
... 
>>> print(list(reduce(accumulator, [1,2,3,4,5,6], 0)))
0 1
1 2
3 3
6 4
10 5
15 6
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable
>>> print(list(reduce(accumulator, [1,2,3,4,5,6], 1)))
1 1
2 2
4 3
7 4
11 5
16 6
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable
>>> 

>>> print(reduce(accumulator, [1,2,3,4,5,6], 1))
1 1
2 2
4 3
7 4
11 5
16 6
22

>>> from functools import reduce 
>>> list1 = [10,2,3,1,1]
>>> def deducation(initial,next):
...     return initial - next;
... 
>>> print(reduce(deducation,list1,10))-7
>>> print(reduce(deducation,list1,0))-17
>>> print(reduce(deducation,list1,10))-7
>>> 

```


we manipulated all these values and reduce the sequence into some sort of data that we have manipulated using in our case 


### Exercises

```python

>>> 
>>> def function1_add_1(param):
...     return param + 1
... 
>>> list1 = [1,2,3,4,5,6]
>>> print(map(function1_add_1,list1))
<map object at 0x7f2dfcbe69a0>
>>> print(list(map(function1_add_1,list1)))
[2, 3, 4, 5, 6, 7]
>>> def function1_condition_even(param):
...     return param % 2
... 
>>> print(list(filter(function1_condition_even,list1)))
[1, 3, 5]
>>> def function1_condition_even(param):
...     return param % 2 == 0... 
>>> print(list(filter(function1_condition_even,list1)))
[2, 4, 6]
>>> list1 = [1,2,3]
>>> list2 = [2,3,4]
>>> print(list(zip(list1,list2)))
[(1, 2), (2, 3), (3, 4)]


```





### lambda expression 


lambda is a cinotyer system that reakkt us compatible with the idea of functional porgramming 

lambda expression is one time anonymous functions that you do not need more than once 

they are annoymous functions, we do not need any names for them 

```python
lambda param: function(params)

```


```python
>>> f1 = lambda x : x * 2 
>>> f1(2)
4
>>> for i in range(1,10):
...     f1(i)
... 

>>> f2 = lambda x ,y : x + y
>>> f2(2,3)
5
>>> for i in range(1,10):
...     f2(i,10)
... 

```


lambda expression is one time expression and there is no name attached to this function, not cluttered with all these functions 

it works well with map(), reduce(), zip(), filter() functions 
let's record the birds chirping in the background 


### List, Set, Dictionary comprehension 


copy a list redundantly

```python
>>> empty_list = []
>>> for item in "hello, this is what i am doing here":
...     empty_list.append(item)
... 
>>> print(empty_list)
['h', 'e', 'l', 'l', 'o', ',', ' ', 't', 'h', 'i', 's', ' ', 'i', 's', ' ', 'w', 'h', 'a', 't', ' ', 'i', ' ', 'a', 'm', ' ', 'd', 'o', 'i', 'n', 'g', ' ', 'h', 'e', 'r', 'e']

```

using a list comprehension as a pythonic way, although this makes code shorter, maybe even cleaner, it does take away a bit of its readability, it may just better to create some descriptive function names 


```python

result = [param for param in iterable]

### conditional 
result = [param for param in iterable if condition]


```

eaxmple to reduce the redundancy of the previous one:


```python
>>> [char for char in "hello, this is what i am doing here"]
['h', 'e', 'l', 'l', 'o', ',', ' ', 't', 'h', 'i', 's', ' ', 'i', 's', ' ', 'w', 'h', 'a', 't', ' ', 'i', ' ', 'a', 'm', ' ', 'd', 'o', 'i', 'n', 'g', ' ', 'h', 'e', 'r', 'e']

```

what if I want a list of number 1 to 100 mutiple by 2? 

```python

>>> [ num * 2 for num in range(1,101)][2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200]
>>> 

```

what if I want to keep even numbers in this list from 1 to 100 that is already multipled by 2? 

```python 

>>> [num * 2 for num in range(1,101) if num % 2 == 0]
[4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140, 144, 148, 152, 156, 160, 164, 168, 172, 176, 180, 184, 188, 192, 196, 200]

```




a set comprehension is similar to a list comprehension just simply change the [] to {} 


```python

result = {param for param in iterable}

### conditional 
result = {param for param in iterable if condition}


```


```python
>>> { x for x in range(1,100) if x % 2 == 0}
{2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98}

```


dictinaries, 
dict_object = {key:value} this key and value can be acted upon 


```python

{key:value for key,value in another_dictionary.items() }

{<key:value operations> for key,value in another_dictionary.items() if condition}


```

we need to pass iterable like a dictionary that has both keys and values 

```python
>>> dict1 = {
... 'a':1,
... 'b':2,
... 'c':3,
... 'd':4,
... 'e':5,
... }
>>> 
>>> result = {key,value : key, value ** 2 in dict1.items()}
  File "<stdin>", line 1
    result = {key,value : key, value ** 2 in dict1.items()}
                        ^
SyntaxError: invalid syntax
>>> result = {key,value for key, value ** 2 in dict1.items()}
  File "<stdin>", line 1
    result = {key,value for key, value ** 2 in dict1.items()}
                        ^
SyntaxError: invalid syntax
>>> result = {key:value for key, value ** 2 in dict1.items()}
  File "<stdin>", line 1
SyntaxError: cannot assign to operator
>>> result = {key:value**2 for key, value in dict1.items()}
>>> result 
{'a': 1, 'b': 4, 'c': 9, 'd': 16, 'e': 25}
>>> 


>>> dict1 = {... 'a':1,... 'b':2,... 'c':3,... 'd':4,... 'e':5,... }
>>> result = {key:value + 1 for key, value in dict1.items() if value > 2}
>>> result 
{'c': 4, 'd': 5, 'e': 6}

>>> result = {key:value + 1 for key, value in dict1.items() if key > 'c'}
>>> result {'d': 5, 'e': 6}

```

again, this makes your code a bit less readable, you should be careulf not to be overly clever and do this single line comprehension just because you can 

let's solidify our knowledge

```python

{key:key/value for key in iterable }




```


make a dictionary for number : number * 2 key value pair 

```python

>>> dict1 = {num : num * 2 for num in [1,2,3]}
>>> dict1
{1: 2, 2: 4, 3: 6}

```



## Reference
How to become a Python 3 Developer and get hired! Build 12+ projects, learn Web Development, Machine Learning + more!