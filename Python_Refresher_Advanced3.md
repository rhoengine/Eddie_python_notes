# Decorators and Generators 

### HOC -- higher order function 

1 that is either one function accepts another function as a parameter

2 another way it can be a higher order function is if it i a function that returns another function 



```python

>>> def greet(func):
...     func() 
... 
>>> def greet2():
...     def func():
...             return 6
...     return func
... 
>>> greet2() 
<function greet2.<locals>.func at 0x7ffb8189b310>
>>> a = greet2() 
>>> a = greet2
>>> a() 
<function greet2.<locals>.func at 0x7ffb8189b3a0>
>>> a()() 
6
>>> a(greet1)
 

```


map() function is a higher order function , so as reduce(), and filter() 






## Decorators 


we have seen decorators before 
@classmethod and @staticmethod 




```python

>>> class ClassA:
...     @staticmethod
...     def use_less_just_like_regular_function(param1):...             return param1
...     @classmethod
...     def call_on_call(param1):
...             print("this is a class method which actually requires one argument cls")
...             return param1
... 
>>> objectA = ClassA()
>>> print(call_on_call(3))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'call_on_call' is not defined
>>> ClassA.call_on_call(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: call_on_call() takes 1 positional argument but 2 were given
>>> ClassA.call_on_call(2,1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: call_on_call() takes 1 positional argument but 3 were given

```


A staticmethod is a method that knows nothing about the class or instance it was called on. It just gets the arguments that were passed, no implicit first argument. It is basically useless in Python -- you can just use a module function instead of a staticmethod.
With staticmethods, neither self (the object instance) nor cls (the class) is implicitly passed as the first argument. They behave like plain functions except that you can call them from an instance or the class

A classmethod, on the other hand, is a method that gets passed the class it was called on, or the class of the instance it was called on, as first argument. This is useful when you want the method to be a factory for the class: since it gets the actual class it was called on as first argument, you can always instantiate the right class, even when subclasses are involved. Observe for instance how dict.fromkeys(), a classmethod, returns an instance of the subclass when called on a subclass. With classmethods, the class of the object instance is implicitly passed as the first argument instead of self



```python 

>>> class A:
 
...     @staticmethod 
...     def example_static_method(param1):
...             print("this is the param1")
...             return param1
...     @classmethod
...     def example_class_method(cls,param1):
...             print("this is the class method")
...             return param1
... 
>>> A.example_class_method(1) 
this is the class method
1
>>> A.example_static_method(1)  
this is the param1
1
>>> 

```


in python if we do: 


```python 

>>> def hello():
...     print("hello")
... 
>>> print(hello)
<function hello at 0x7ffb82fa4ca0>
>>> variable = hello
>>> del hello
>>> print(hello)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'hello' is not defined
>>> print(variable)
<function hello at 0x7ffb82fa4ca0>
>>> print(variable())
hello
None

```


we do not expect the variable still works, the interesting thing about python is this is now created in memory, when we delete it. another whole another variable is still pointing to this function. that variable is still pointing at that location. python is smart enought to say python will not delete the copied reference to it. so functions in python act just like variables do their first class citizens 

we can also pass functions around inside of arguments, 



```python

>>> def one_function(another):...     another() ... 
>>> def another_func():...     print("this is another function")
... 
>>> all = one_function(another)this is another function
>>> print(all)None
>>> 

```

decorators are only possible because of these features -- this ability of functions to act like variables, act like first clss citizens, underneath the hood, they are using this power of functions and expand this idea. the short form of what decorator's do, decorator's supercharge our function if we had another function. by adding some sort of a decorator, we can supercharge our function and add extra functionality 





let's write our own decorator, remember a decorator supercharges another function and enhances or changes it 



```python

...     def inner_function():
...             func()
...             print("only calls the function parameter and does nothing else")
...     return inner_function
... 

```

we are not calling it, we are returning it so later on somebody can use it 

```python

>>> @outer_function
... def hello():
...     print("hello")
... 

```

this does not change anything, it works exactly as expected 

now we can add extra functionality, how can we enhance it? 

```python

>>> def outer_function(function_to_be_place_in_the_middle): 
...     def inner_function():
...             print("this is where the magic comes, when we return function_to_be_place_in_the_middle. this will do thins below:")
...             print("-----------------------------------")
...             print("-----------------------------------")
...             function_to_be_place_in_the_middle() 
...             print("-----------------------------------")
...             print("-----------------------------------")
...     return inner_function
... 
>>> @outer_function
... def anything():
...     print("now this is inserted in the middle ")
... 
>>> anything() 
this is where the magic comes, when we return function_to_be_place_in_the_middle. this will do thins below:
-----------------------------------
-----------------------------------
now this is inserted in the middle 
-----------------------------------
-----------------------------------
>>> 

>>> @outer_function
... def another():
...     print("see the magic again")
... 
>>> another() 
this is where the magic comes, when we return function_to_be_place_in_the_middle. this will do thins below:
-----------------------------------
-----------------------------------
see the magic again
-----------------------------------
-----------------------------------
>>> 

```
underneath the hood, we literally saying 

variable = decorator_aka_function(embedded_function)
variable() 

all I am doing is wrapping my function with my decorator 

decorator_aka_function(embedded_function)()

franking looking confusing, we can just add at it and we do not need to do all of this 


what happens if the invoked function actually took parameters 

```python 

>>> def outer_function(func_param):...     def inner_function(parameters):...             print("-----------------------------------")
...             func_param(parameters)
...             print("-----------------------------------")
...     return inner_function
... 
>>> @outer_function
... def hello(greeting):
...     print(greeting)
... 
>>> hello("hello world")
-----------------------------------
hello world
-----------------------------------
>>> 

```


when we do the function, we give it an argument, it sets the parameter and runs the function 



if we have muliple params:


```python 

>>> def outer_function(func_param):...     def inner_function(parameters):...             print("-----------------------------------")
...             func_param(parameter1,parameter2,....)
...             print("-----------------------------------")
...     return inner_function
... 
>>> @outer_function
... def hello(param1,param2):
...     print(param1,param2)
... 
>>> hello("hello world")

```

this is hectic, every time when I need to change parameters, what if we have keyword arguments or we want to change it. there is actually a pattern here that we can use that make things really simple for us 


```python 

>>> def outer_function(func_param):...     def inner_function(parameters):...             print("-----------------------------------")
...             func_param(*args, **kwargs)
...             print("-----------------------------------")
...     return inner_function
... 
>>> @outer_function
... def hello(param1,keyword=""):
...     print(param1,keyword)
... 
>>> hello("hello world")

```


this is called decorator pattern, it gives our decorator flexbility so we are able to pass as many arguments as we want into our function by using *args and kwargs and then unpacking them like this inside a function. by just using these line of code, we are able to add functionality: 


```python
>>> def outer(func_param):
...     def inner(variable_param):
...             func_param(variable_param)
...     return inner
... 
>>> def outer(func_param):
...     def inner(*args, **kwargs):
...             func_param(*args, **kwargs)
...     return inner
... 

```



let's talk about some pratical applications of decorators 

we are able to create class method and static method. 


I want to know how many miliseconds it takes to complete 

```python
>>> def performance(fn):
...     def wrapper(*args,**kawrgs):
...             t1 = time()
...             result = fn(*args, **kawrgs)
...             t2 = time() 
...             print(f'took {-(t1-t2)} ms')
...             return result 
...     return wrapper
... 
>>> @performance:
  File "<stdin>", line 1
    @performance:
                ^
SyntaxError: invalid syntax
>>> @performance
... def long_time():
...     for i in range(100000000):
...             i * 5
... 
>>> long_time() 
took -3.318695545196533 ms
>>> @performance
... def long_time():
...     for i in range(100000):
...             i * 5
... 
>>> long_time() 
took 0.008348226547241211 ms

```



I can optimize things in different ways 

decorators are used in djangos and manp python applications such as @auth or @logging 




### Generators 

generators allow us to generate a sequence of values over time 

range() is a generator, allows us to use a special word called yield

yield can pause and resume functions 



a list, list(), what it does is actually create a giant list, of hundred items in memory versus range() creates them one by one 


 ```python

>>> range(100)
range(0, 100)
>>> list(range(100))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> 
>>> def make_list(number):
...     result = []
...     for i in range(100):
...             result.append(i)
...     return result 
... 
>>> make_list(100)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

 ```

this is taking up space right now, now, range is a generator, ranges gives you the number from beginning all the way to the end 


for loop can get pretty hectic 

```python

list(range(1000000))

```
this is a lot of memory we are using up,we need to revisit our knowledge 

a list is a iterable, what is a iterable, an iterable is any object in python which we are able to loop through underneath the hood 

iteration is the act of taking an item from an iterable and going to the next one


generators are iterable, you can iterate over them. not everything which is iterable are generators 

generators are usually functions 

generator are not returning items, instead we use a keyword called yield 

##### yield pauses the function and comes back to it, then going to the next 

we are going to loop over the generator and we will give it to a generator function, it is going to run and loop 

```python

>>> def generator_function(num):
...     for i in range(num):
...             yield i
... 
>>> def return_function(num):
...     for i in range(num):
...             return i
... 
>>> for item in generator_function(100):
...     print(item)
... 
>>> for item in return_function(100):
...     print(item)
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable
>>> 

```


we just held one item in memory 

```python
>>> g = generator_multiple_by_2(100) 
>>> g
<generator object generator_multiple_by_2 at 0x7ffb81771c10>
>>> for item in g:
...     print(item)
... 

>>> def return_multiple_by_2(num):
...     for i in range(num):
...             return i * 2
... 
>>> r = return_multiple_by_2(100) 
>>> r
0

>>> for item in r:
...     print(item)
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable
>>> 

```



we can do next(), the yield keyword pauses the function, first time we run it, get the output. yield pauses the function and comes back to it when next() is called. it keeps track of this state, what we call the value, and it only keeps the mos recent data in memory 
we call as many as times until this range expires and when we exceed the number o fitems in the range() we get the stop iterations 

using range it is hidden away from us as users 


### generator performance 
they are fast and performant 


```python

>>> from time import time 
>>> def performance_outer(performance_inner):
...     def performance_inner(*args,**kwargs):
...             t1 = time()
...             result = performance_inner(*args, **kawrgs)
...             t2 = time() 
...             print(f'took {t2-t1} sec')
...             return result
...     return performance_inner
... 


>>> @performance
... def long_time():
...     print('1 using range generator')
...     for i in range(100000):
...             i ** 5
... 
>>> def long_time_2():
...     return performance_inner
KeyboardInterrupt
>>> @performance
... def long_time_2():
...     print('1 using list return')
...     for i in list(range(100000)):
...             i ** 5
... 
>>> 
>>> 

```

range() keeps removing old members from memory 

generator that is not holding things in memory, not have to consume all that resources and instead process data efficiently 
generators are really useful when calculating large sets of data when we do not want to store that in the memory 





### iterator 

it receives a iterable. 
for us to receive iterable, it uses iter() that accepts the iterables 

```python
>>> def iterable_function(iterable):
...     iterator = iter(iterable)
...     while True:
...             try: 
...                     print(iterator)
...                     next(iterator)
...             except StopIteration:
...                     break 
... 
>>> iterable_function([1,2,3])
<list_iterator object at 0x7ffb81790c10>
<list_iterator object at 0x7ffb81790c10>
<list_iterator object at 0x7ffb81790c10>
<list_iterator object at 0x7ffb81790c10>
>>> 


```

the loop will keep calling next iteartor on it over and over until we finish the end of line and then break out of the loop 



### we can definie a dunder method in a class __iter__ and __next__ to keep track of where we are 

```python

>>> class myGenerator():
...     current = 0
...     def __init__(self, first, last):
...             self.first = first 
...             self.last = last 
...     def __iter__(self):
...             return self
...     def __next__(self):
...             if myGenerator.current < self.last:
...                     num = myGenerator.current
...                     myGenerator += 1
...                     return num
... 

```


### Fibonacci number in a generator 

```python

>>> def fibonacci(number):
...     a = 0 
...     b = 1
...     for i in range(number):
...             yield a
...             temp = a 
...             a = b
...             b = temp +b
... 
>>> fibonacci(100) 
<generator object fibonacci at 0x7ffb8178f510>
 
>>> for i in fibonacci(100):
...     print(i)
... 

```
number increases dramtically we are not keep these in memory, it does demonstrate the power of generators and increases performances 



















```python
>>> def generator_multiple_by_2(num):
...     for i in range(num):
...             yield i * 2
... 
>>> g = generator_multiple_by_2(100) 
>>> print(next(g))
0
>>> print(next(g))
2
>>> print(next(g))
4

```










## Reference
How to become a Python 3 Developer and get hired! Build 12+ projects, learn Web Development, Machine Learning + more!



 