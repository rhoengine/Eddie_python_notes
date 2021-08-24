# Python Object Oriented Programming 



### OOP 

everything in python is Object 

we have all our data types but we have this class keyword in front of it to access attribute and perform actions

OOP is a paradigm in a way that is easiser to maintain, extend and write, it is a way to structure our code 





```python
 type(None)
<class 'NoneType'>
 type(int)
<class 'type'>
type(1)
<class 'int'>
 type(1.1)
<class 'float'>
 type(True)
<class 'bool'>
 type('hi')
<class 'str'>
 type([])
<class 'list'>
 type(())
<class 'tuple'>
 type({})
<class 'dict'>

```

a procedure code is just like procedure, we execute from top of line to the bottom of the line 


a object oriented code that simulates attribute and actions in our real world, organizing thing to run things. we use classes to incorporate object oriented programming paradigms 



what is a class keyword? 
that build a class ClassName using camelcase 
from this blueprint, we can call this class to instantiate 
different instances 

OOP allows us to write code repeatable 




below is the blueprint 

```python

class ClassName:
    pass 

objectName = ClassName()

```




```python

class ClassName:
    def __init__(self,parameters):
        self.instance_variable = parameters

    def method1(self):
        statements on self.instance

    def method2(self):
        statements on self.instance

objectName = ClassName(argument)
objectName.method1()
objectName.method2(argument)

```

example

```python

>>> class ClassName: 
...     def __init__(self, name):
...             self.name = name
...     def method1(self):
...             print(self.name)
...     def method2(self):
...             print("nothing")
... 
>>> object1 = ClassName("Eddie")
>>> object1.method1() 
Eddie
>>> object1.method2() 
nothing

```

__init__ method is a special method, two underline, that is a dundar method, that is often called a constructor method, that is called every time when we instantiate it, it does not the self.parameter

you can do different safeguards, 
1. if condition
2. default parameters 


```python

class ClassName:
    def __init__(self,parameter1,parameter2=value):
        if parameters > value:
            self.instance_variable = parameters

    def method1(self):
        statements on self.instance

    def method2(self):
        statements on self.instance

objectName = ClassName()
objectName = ClassName(argument)
objectName.method1()
objectName.method2(argument)

```




objects live in different places inside the memory 

```python

>>> class ClassName: 
...     def __init__(self, name):
...             self.name = name
...     def method1(self):
...             print(self.name)
...     def method2(self):
...             print("nothing")
... 
>>> object1 = ClassName("Eddie")
>>> object1.method1() 
Eddie
>>> object1.method2() 
nothing
>>> object2 = ClassName("James")
>>> print(object1)
<__main__.ClassName object at 0x7f48db780fa0>
>>> print(object2)
<__main__.ClassName object at 0x7f48db857d90>

```

you can add attributes when using object

```python 

objectName.variable_name = value 

```

```python 
>>> class ClassName: 
...     def __init__(self, name):
...             self.name = name
...     def method1(self):
...             print(self.name)
...     def method2(self):
...             print("nothing")
... 
>>> object1 = ClassName("Eddie")
>>> object1.method1() 
Eddie
>>> object1.method2() 
nothing
>>> object2 = ClassName("James")
>>> print(object1)
<__main__.ClassName object at 0x7f48db780fa0>
>>> print(object2)
<__main__.ClassName object at 0x7f48db857d90>
>>> object1.anotherValue = 300
>>> print(object1.anotherValue)
300
>>> print(object2.anotherValue)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'ClassName' object has no attribute 'anotherValue'
>>> 

```


### Attributes and methods 

field/instance variable is only unique to that specific object, we have to use the self.field keyword to make sure it is dynamic 





```python
class ClassName:
    def __init__(self,parameters):
        self.field = parameters

```




the class object attribute is not dynamic, it is unlike self.attribute, it is static 

```python
class ClassName:
    classObjectAttribute = value
    def __init__(self,parameters):
        self.field = parameters


```

you cannot change it and it is shared across instances 
a class attribute is something dynamical. 
the way we access is different. 



```python
>>> class ClassName: 
...     classObjectAttribute = 10 
...     def __init__(self, name):
...             self.name = name
...     def method1(self):
...             print(self.name)
...     def method2(self):
...             print("nothing special")
... 
>>> ClassName.classObjectAttribute
10
>>> object1 = ClassName("Eddie")
>>> object1.classObjectAttribute
10
>>> 

```


### @classmethod and @staticmethod

what does @classmethod do? when we call this, we give it to parameter, but then it was expecting cls!!!!


```python
@classmethod
def classMethod(cls, params):
    return params

```

we just use it without instantiating the object. 95% your code won't use class method 


```python

>>> ClassName.classMethod(1,2,3) 
5

```

##### use cls, we can instantiate an object 





```python
>>> class ClassName: 
...     def __init__(self,name):
...             self.name = name 
...     def instance_method(self):
...             print(self.name)
...     @classmethod
...     def classMethod(param_without_self1, param_without_self2):
...             return param_without_self1 + param_without_self2;
... 
>>> object1 = ClassName('Eddie')
>>> object2 = ClassName('Juan')
>>> object1.classMethod(1,2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: classMethod() takes 2 positional arguments but 3 were given
>>> className.classMethod(1,2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'className' is not defined
>>> ClassName.classMethod(1,2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: classMethod() takes 2 positional arguments but 3 were given
>>> 


>>> class ClassName: ...     def __init__(self,name):...             self.name = name ...     def instance_method(self):...             print(self.name)...     def classMethod(cls,param_without_self1, param_without_self2):
...             return param_without_self1 + param_without_self2;
... 
>>> ClassName.classMethod(1,2)Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: classMethod() missing 1 required positional argument: 'param_without_self2'
>>> object1 = ClassName('Eddie')>>> object2 = ClassName('Juan')>>> object1.classMethod(1,2) 
3

```


@staticmethod is similar to @classmethod, but wihtout cls 

```python
@staticmethod
def staticMethod(params):
    return params

```

the only difference between the two is we do not have access in our parameters to this cls 

we will use @staticmethod where we do not care about the class state 



cls_method can be called without instantiating it to an object 
look at this overall structure, we have gained a very powerful tool to grasp this concept 


```python
class NameOfClass():
    def __init__(self,param1,param2):
        self.param1 = param1
        self.param2 = param2
    def method(self):
        pass

    @classmethod 
    def cls_method(cls, param1, param2):
        pass

    @static_method
    def stc_method(param1,param2):
        pass



```


### test your assumptions 

self is referring to instance, return a self in a method 

think ahead if there is a mismatch, that is something rational


### Encapsulation 

encapsulation is the binding of data and functions that manipulate the data and we encapsulate into one object that machine can interact with 


we are able to encapsulat ethe functionality of data and attributes. We have packaged this up into a blueprint that I can create multiple objects 

why do we want to package data and functions into attributes and methods? this gives us extra power because our world is full of data and actions 

### private vs public 

we hide away information and only give away things that a user is concerned about 

some languages allows us to have private variables like java 

in python there is no true privacy/  private variable 
but it is just a concention that is as Python programmer tha twe determine that if we use self_fieldName, tha tmost likely means that this should be a private variable 



```python
class NameOfClass():
    def __init__(self,param1,param2):
        self._privateVariable = param1
        self.publicVariable = param2
    def method(self):
        pass

    @classmethod 
    def cls_method(cls, param1, param2):
        pass

    @static_method
    def stc_method(param1,param2):
        pass



```


there is no true private variable as python programming, as programmers we decide we should not touch this if it has an underscore 

DunderMethod is built into python, __method__, we will never write our own Dundar methods. if you do __method__() you are doing something very wrong, you are about to overwrite something 


although it can modified and overriden by using these proper conventions like private attributes, we are able to abstract things away 








### abstraction 

an abstraction means hiding of information or abstracting away information and giving access to only what's necessary. we kind of hiding it in a blanket underneath the hood, our heads are gonna explode 







### Inheritance 


inheritance allows new objects to take on the properties of existing objects 


```python

class SuperClass():
    def __init__(self,param):
        self.variable = param
    def method(self):
        print(self.variable)

class SubClass(SuperClass):
    pass

```


we inherited from SuperClass 



```python
>>> class SuperClass():
...     def __init__(self,param1):
...             self.variable = param1
...     def method_name(self):
...             print(self.variable)
... 
>>> class Subclass(SuperClass):
...     pass
... 
>>> subclassObject = Subclass("Eddie")
>>> subclassObject.method_name()
Eddie
>>> 

```


we can add new methods or variables into Subclass

```python 



>>> class SuperClass():
...     def method(self):
...             print("nothing")
... 
>>> class Subclass(SuperClass):
...     def __init__(self,param1):
...             self.param1 = param1
...     def methodName(self):
...             print(self.param1)
... 
>>> subclassObject = SubClass("Ed")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'SubClass' is not defined
>>> subclassObject = Subclass("Ed")
>>> subclassObject.method()
nothing
>>> subclassObject.methodName() 
Ed

```


### isinstance() 
isinstance() is a built-in function in python that allows us to check if the instance belongs to a class 

everything in python inherits from the base object class that python comes, even higher up from the object based clss that python comes 

that is why we have these automatic methods attached fro us 
every commonality we can just dish it out to all obejcts that need it, super cool 




```python
isinstance(instance, Class)

```

we have to run superclass to create subclass, so object belongs to both superclass and subclass 

```python 
>>> isinstance(subclassObject,Subclass)
True
>>> isinstance(subclassObject,Superclass)Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Superclass' is not defined
>>> isinstance(subclassObject,Superclass) 
KeyboardInterrupt
>>> isinstance(subclassObject,SuperClass)True

```


### Polymorphism 

polymorphism means many forms 

methods belong to object, and we use the self keyword to act upon the object that got instantiated 

in python, this idea of polymorphism refers to the way in which object classes can share the same method name 


```python

>>> class Car: 
...     def drive(self):
...             print("universal car")
... 
>>> class Sudan(Car):
...     def drive(self):
...             print("Sudan")
... 
>>> class SUV(Car):
...     def drive(self):
...             print("SUV")
... 
>>> def polymorphism_function(car_object):
...     print(car_object.drive())
... 
>>> sudan = Sudan() 
>>> suv = SUV() 
>>> polymorphism_function(sudan)
Sudan
None
>>> polymorphism_function(suv)
SUV
None

>>> list_of_object = [sudan, suv]
>>> for item in list_of_object:
...     item.drive() 
... 
Sudan
SUV

```


### super() 
althoug we might inherit the super class's method, but the subclass already has its method 

```python 

class Superclass:
    def __init__(self,param1,param2,param3):
    self.param1 = param1
    self.param2 = param2
    self.param3 = param3


class Subclass(Superclass):
    def __init__(self,param1,param2,param3,param4):
    self.param1 = param1
    self.param2 = param2
    self.param3 = param3
    self.param4 = param4

```

if we know all these attributes are going to be the same on all of our subclasses 
the more efficient way to do it, this __init__ function is call 



```python 

class Superclass:
    def __init__(self,param1,param2,param3):
    self.param1 = param1
    self.param2 = param2
    self.param3 = param3


class Subclass(Superclass):
    def __init__(self,param1,param2,param3,param4):
    Superclass.__init__(param1,param2,param3)
    self.param4 = param4

```

when we instaniate this it calls the SuperClass.__init__(self, parameters)
alternatively we can do this: 




```python 

class Superclass:
    def __init__(self,param1,param2,param3):
    self.param1 = param1
    self.param2 = param2
    self.param3 = param3


class Subclass(Superclass):
    def __init__(self,param1,param2,param3,param4):
    super().__init__(param1,param2,param3)
    self.param4 = param4

```

super() allows us to refer to SuperClass 



### Introspection 
introspection in computer programming means the ability to determine the type of an object at runtime 

when is runtime, that is when the code is running, you can determine the type of an object 

we can introspect an object and actually figure out what our code does as we are coding and running 

##### dir(objectName) allows us to introspect all the attribute and methods an object has 


```python
>>> class Car: 
...     def drive(self):
...             print("universal car")
... 
>>> class Sudan(Car):
...     def drive(self):
...             print("Sudan")
... 
>>> class SUV(Car):
...     def drive(self):
...             print("SUV")
... 
>>> def polymorphism_function(car_object):
...     print(car_object.drive())
... 
>>> sudan = Sudan() 
>>> suv = SUV() 
>>> polymorphism_function(sudan)
Sudan
None
>>> polymorphism_function(suv)
SUV
None
>>> list_of_object = [sudan, suv]
>>> for item in list_of_object:
...     item.drive() 
... 
Sudan
SUV
>>> print(dir(suv))
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'drive']

```
when we do object_name.method() is using the ability of introspection to list out these available methods for us 


### Dunder Methods 

we will uncover what Dunder methods do what are the instances 


these __method__() are special methods that python recognizes 

we can do basic customization of these Dunder methods, there are specific cases we need to modify them 

__str__()


```python
>>> class ClassName:
...     pass 
... 
>>> objectName = ClassName() 
>>> objectName
<__main__.ClassName object at 0x7f48d9f34eb0>
>>> print(objectName)
<__main__.ClassName object at 0x7f48d9f34eb0>
>>> print(objectName.__str__())
<__main__.ClassName object at 0x7f48d9f34eb0>
>>> 

```

there are special occasions we need to customize them 

__len__() 
__delete__()

```python
>>> class ClassName:...     def __str__(self):...             return "this is the illustration"
...     def __len__(self):
...             return 100
...     def __delete__(self):
...             print("deleted this nonesense")
... 
>>> objectName = ClassName() >>> print(len(objectName))100
>>> print(delete(objectName))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'delete' is not defined
>>> del objectName

```


__call__() uses a special way to call a function which by the way underneath the hood,the way we able to call the method 




```python
>>> class ClassName:...     def __call__(self):...             print("call specific object")
... 
>>> objectName = ClassName() >>> print(objectName())
call specific object
None
>>> 

```


usually we have to power to override them when we choose to do so 

__getitem__()

```python 
>>> class ClassName:...     def __init__(self, param1):...             self.param1 = param1...             self.dictionary = {"key":"value"}
...     def __getitem__(self,i):...             return self.dictionary[i]... 
>>> objectName = ClassName('Ed') >>> print(objectName['key'])value

```


### issubclass() 

issubclass(subclass,superclass)


issubclass(subclass,object)
everything in python is an object that inherits from the base object class, we then inherit from superclass 


### multiple inheritance 

```python 

>>> class SuperClass1:
...     def method1(self):
...             print("from superclass 1")
... 
>>> class SuperClass2:
...     def method2(self):
...             print("from superclass 2")
... 
>>> class Subclass(SuperClass1, SuperClass2):
...     def method3(self):
...             print("from subclass")
... 
>>> subclassObject = Subclass()
>>> subclassObject.method1(0 
... 
KeyboardInterrupt
>>> subclassObject.method1() 
from superclass 1
>>> subclassObject.method2() 
from superclass 2
>>> subclassObject.method3() 
from subclass


```



```python 
>>> class SuperClass1:...     def method(self):...             print("superclass1's method")
... 
>>> class SuperClass2:...     def method(self):
...             print("superclass2's method")
... 
>>> class Subclass(SuperClass1,SuperClass2):
...     def method(self):
...             print("superclass3's method")
... 
>>> subclassObject = Subclass()
>>> 
>>> subclassObject.method() 
superclass3's method

```

technically we inherit from the first one and then second one, why does not some languages do not even allow multiple inheritance things to get a little tricky because in your head, you have to make sure you are not overriding anything we can complicate our code a little bit 



```python

>>> class SuperClass1:...     def method(self):...             print("superclass1's method")
... 
>>> class SuperClass2:...     def method(self):...             print("superclass2's method")
... 
>>> class SubClass1(SuperClass1, SuperClass2):
...     pass
... 
>>> subclass1Object = SubClass()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'SubClass' is not defined
>>> subclass1Object = SubClass1()
>>> subclass1Object.method() 
superclass1's method
>>> 

```


it is super powrful but with great power comes great responsbility because we are creating more and more complexity 


### MRO method resolution Order 

MRO is there as a way to define what order you are going to inherit and you can always use the MRO function to check it. it exists but you should not structure your code like this. the key takeaway, when you check the inheritance, MRO is the way how it works 

object_name.mro()

you need to at least be conscious of mro() 

python uses Depth First Search DFS for MRO algorithm 



```python

"""
              A
            /    \
           B      C
            \    /
              D
""" 
>>> class A:
...     number = 10 
... 
>>> class B(A):
...     pass
... 
>>> class C(A):
...     number = 11
... 
>>> class D(B, C):
...     pass
... 
>>> 
>>> print(D.mro())
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
>>> 
```

## Reference
How to become a Python 3 Developer and get hired! Build 12+ projects, learn Web Development, Machine Learning + more!