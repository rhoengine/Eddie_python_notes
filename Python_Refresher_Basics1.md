# Python Basics Basic: Data types and Data Structure

## Get Started 

This tutorial came about by circuitious means that you will be empowerd and endeavoured by its shrouded letigation. With python you can build everything from simple simple sscripts to complex applications, you can do it quickly. We will take a quick tour of the Python language and get a sense of what makes it so appealing, We will also give a brief preview of the language.  I was sure we want to carefully structure our introductory content in Python content to respect certain constructs. We wanted an absolute minimum of forward references since those would be very inconvenient for viewers instead of trying to put forward pressure. This is the result of your transformation, depending on which style of learning suits you best. 

Rember every practice counts! Fortunately you can ignore most of that; you jsut need to learn enough to write some handy litte programs 


##  Hello World

A long-held belief and appetite in the programming world has been that printing a Hello World! message to the screen. Such as simple program serves a very real purpose. If it runs correctly on your system, any python program you write should work as well and impacting your future programs. 
```python
# save it in a hello.py and run python hello.py
print("Hello World")

```

```shell
cat hell.py 
python hello.py 

```

When you run the file xx.py, the ending .py indicates that the file is a Python program. Your editor then runs the file through the Python interpreter, which reads through the program and determines what each word in the program means. 

**Note:** 
Python comes with an interpreter that runs in a terminal windows, allowing you to try bits of python without having to save and run an entire program. But sometimes basic concepts will be shown in a series of snippets run through terminal sesesions to demonstrate isolate concepts and legitimacy more efficently. 



## Comments


Comments are an extremely useful feature in most languages as program get bigger and more compolicated, they get more difficult to read. Formal languages are dense, and it is often difficult to look at a piece of code and figure out what it is doing, or why. For this reason, it is a good idea to add notes to your prorgams to explain in natural language what the prorgam is doing. These notes are called comments and in python they start with # symbols 



python ignores comments, and you can use them to write notes or remind yourself what the code is trying to do. Any text for the rest of the line following a hashmark # is part of a comment 

sometimes prorgammers will put a # in front of a line of code to temporarily remove it while testing a porgram. This is called *commenting out* code, and it can be useful when you are tyring to figrue out why a program does not work 


python also ignores the blank line after the comment. you can add as many blank lines to your porgrams as you want. this can make your code easier to read, like paragraphs in a book 

the main reason to write comments is to explian what your code is supposed to do and how you are making it work. When you are in the middle of working on a project, you understand how all of the pieces fit together. But when you return to a project after some time away, you will likely have forgotten some of the details. 

If you want to become a professional programmer or collaborate with other programmers, you should write meaningful comments. Today, most software is written collaboratively, whether by a group of employees working together on an open source project. 

you are adding valuable self-explantory for something important to make your code undrstandable 

```python
# this is the comment 
'''
comment 

'''
```

 
moving foward




##  Value and Data Types

### Data types 

we are taking actions on these data types, so two crucial steps, one learning a programming language is that, we have these data to create, store, read, change, remove this data from the machine 


1. None
2. bool
3. int 
4. float 
5. complex 
6. str 
7. list 
8. tuple 
9. dict 
10. set 


1. fundmental data types in python, they are the core to the language 

```python
 int
<class 'int'>
 float 
<class 'float'>
 str
<class 'str'>
 bool 
<class 'bool'>
 list 
<class 'list'>
 tuple 
<class 'tuple'>
 set 
<class 'set'>
 dict 
<class 'dict'>


```

complex is a number thta is a third type instead of int and float, you only use this to do very complex math 


```python
 complex(1)
(1+0j)

```

bin() the binary representation to return whatever the binary version of it is. 

```python
 bin(1)
'0b1'
 bin(1000)
'0b1111101000'

 print(int('0b1111101000',10))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '0b1111101000'

```



2. class -> custom types 

3. specialized data types 

4. None, it means nothing, absence of value 

### Value
a *value* is one of the basic things a program works with, a like a letter or a number. These values belong to different types, an integer and a string(so called because it contains a string of letters, you and the intepreter can identify strings because they are enclosed in quotation marks)

```python 
Eddies-MacBook-Pro-2:python_note eddiehuang$ python3 
Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> type(1)
<class 'int'>
>>> type("Hello World")
<class 'str'>
>>> print(1)
1
>>> print("Hello World!")
Hello World!
>>> 
>>> type(1.1)
<class 'float'>
>>> print(1.1)
1.1


```
not surprisingly, string belong to the type str and integers belong to the type in. Less obviously, numbers with a decimal point beloong to a type called float.

**Note**: when you type a large integer, you might be tempted to use commas between groups of three digits, as 1,000. This is not a legal integer in python. It interepts as a comma separted sequence of integers, which it prints with space between 

```python
>>> print(1,000,000)
1 0 0
```





### Variable
a *variable* is like a box in the computer's memory where you can store a single value. If you want to use the result of an evalauted expression later in your prorgam, you can save it inside a variable. 

every variable holds a value, which is the information associated with that variable. 
Adding a variable makes a little more work for the Python interpreter. 


variables store information for our programs. computers know how to load this info, however our machine stores it, it does not matter 

the naming rule of thumb is to make it descriptive you can take away: 
1. snake_case
2. start with lowercase or underscore 
3. letter, numberes, underscores 
4. case sensitive 
5. do not overwrite keywords 

```python 

variable_1 = value

```

##### Assignment statement 
you will store values in variables with an assignment statement. An assignment statement consists of a variable name, an equal sign called the assignment operator, and the value to be stored.



```python
# save it in a hello.py and run python hello.py
variable1 = "hello world"
variable2 = 2
print(variable1)
print(variable2)

```

```shell
cat hell.py 
python hello.py 

```


a variable is initialized or created the first time a value is stored it. After that, you can use it in expressions with other variables and values. When a variable is assigned a new value, the old value is forgotten. 

```python
>>> variable = 1 
>>> variable = 2 
>>> print(variable)
2


```

##### Naming variable and choosing mnemonic variable names 

As long as you follow the simple rules of variable naming, and avoid reserved words, you have a lot choice when you name your variables. Human will most quickly understadn the intent of the program because the programmer has chosen variable names that reflect their intent regarding what data will be stored in each variable. 

when you are using variables, you need to adhere to a few rules and guidelines. Breaking some of these ruels will cause errors; other guidelines just help you write code that is easiser to read and undrstand 
* variable names can contain only letters, numebrs, and underscores. They can start with a letter or an undrescore, but not with a number. You can call a variable message_1 but not 1_message 
* spaces are not allowed in variables names, but underscores can be used to separate words in variable names 
* avoid using python keywords and function names as variable names, that is, do not use words that python has reserved for a particular programmatic purpose 
* variable names should be short but descriptive. for example, name is better than n, student_name is better than s_n 
* be careful when using the lower case l and uppercase letter O because they could be confused with the numebrs 1 and 0




The word mnemonic means memory aid. 
A good variable name describes the data it contains. just like label all your moving boxes


in a nutshell, you can name a variable anything as long as it obeys the following three rules 

1. it can be only one word 
2. it can use only letter,s numbers, and underscore _ character 
3. it cannot begin with a number 

variable names are case-sensitive. It is a python convention to start your variable with a lowercase letter 
Some experience prorgammers may pout out that the offocial python code style, PEP8, says that undrscores should be used.Others unappologetically prefer camelcase for variable names instead of underscore. Consistency with the style guide is important, know when to be inconsistent. when in doubt, use your best judgement. 






## Operators 
*Operators* are special symbols that represent computations like addition and multiplication. the values the operator is applied to are called *operands*



there are plenty of operators you can use in python expressions. 

 | Symbols | Definition                         | Example |
|---------|------------------------------------|---------|
| +       | addition                           | a + b   |
| -       | subtraction                        | a + b   |
| *       | multitplication                    | a * b   |
| /       | division                           | a / b   |
| **      | exponent                           | a ** b  |
| //      | integer division/ floored quotient | a // b  |
| %       | modulus/remainer                   | a %% b  |


the order of operations also called precedence of python math operators is similar to that of mathemtics. the ** operator is evaluated first, the *,/, //, and % operators are evalauted next, from left to right; and the + and - operators are evalauted last also from left to the right. 

The modulus operator works on integer and yields the remainder when the first operand is divided by the second. The modulus operator is a percent sign %. 



when in doubt, always put paretheses in your expression to make sure the computation are performed in the order you intend. You can use parentheses to override the usual precedence if you need to. These rules for putting operators and values together to form expressions are a fundamental part of python as a programmign language, just like the grammar rule that help us communciate 





```python 

>>> 1 + 2 
3
>>> 1 / 2
0.5
>>> 2 // 3
0
>>> 2 / 3 
0.6666666666666666
>>> 2 * 3 
6
>>> 2 % 3 
2
>>> 3 % 2 
1
>>> 3 % 3 
0
>>> 3 ** 3 
27
>>> 1 - 2 
-1
>>> -1 
-1
>>> 



```


### augmented assignment 
variable += value 
variable -= value 
variable /= value 
variable *= value 
variable **= value
variable //= value
variable %= value

```python
 variable = 0 
 variable = 10
 variable **= 1
 variable 
10
 variable **= 3
 variable 
1000
 variable //= 3
 variable 
333
 variable /= 3
 variable 
111.0
 variable -= 3
 variable 
108.0
 variable += 3
 variable 
111.0
 variable %= 3
 variable 
0.0
```

we are climbing the moutain



## Expression 
An *expression* is a combination of values, variables, and operators.  An expression which is the most basic kind of programming instruction in the language. 

A value itself is considered an expression, and so is a variable. In a script, an expression all by itself does not do anything. This is a common source of confusion for beginners. Expressions consist of values and operators, and they can always evalaute down to a single value. That means you can use expressions anywhere in python code that you an also use a value 


##  Statements 
a *statement* is a unit of code that python interpreter can execute. we have seen two kind of statements: print being an expression statement, and assignment. 

a script usually contains a sequence of statements. if there is more than one statement, the results appear on at a time as the statement execute 


* sequential execution: perform statements on after another in the order they are encountered in the script 

* conditional execution check for certain conditions and then execute or skip a sequence of statements 

* repeated execution, perform soem set of statement repeatedly, usually with some variables 

* reuse. write a set of instructions once and give them a name and then reuse those instructions as needed throughout your program 


### Integer, Floating Point, and String Data Types 

##### Numbers

int: integer

```python
 print(2 + 4)
6
 print(2 - 4)
-2
 print(2 * 4)
8
 print(2 / 4)
0.5
 print(2 // 4)
0
 print(type(2 + 4))
<class 'int'>
 print(2**2)
4
 print(5 % 4)
1

```

float: numbers with decimal points. float take more storage in memory 


```python

 print(type(0.0))
<class 'float'>
 print(type(15.06))
<class 'float'>

```

bool: boolean represents the idea of True or False, it is the cornerstone of computer science 

```python
 True 
True
 False 
False
  bool(0)
False
 bool(1)
True

```

None: None is a special data type that exists in python and most languages have this to represent the absence of values, it is hard to conceptualize it, you are not intimated as you see it 


 




expressions are just values combined with operators, and they always evaluate down to a single value. A data type is a category for values, and every value belongs to exactly one data type. The most common data types in Pythons. 

| Data Type             | Example              |
|-----------------------|----------------------|
| Integer               | 1                    |
| Floating point number | 1.1                  |
| String                | "a", 'a'. "ab", 'ab' |

#### Floats

python calls any number with a decimal point a float. this term is used in most languages, and it refers to the fact that a decimal point can appear at any position in a number 

every language must be carefully designed to properly mangae decimal numbers so numbers behave appropriately no matter where the decimal point appears 




### Math functions 
the language also provides for us different actions that we can perform 
round: round down the number 
abs: returns absolute vlaue, no negative sign

```python 
 round(2.3)
2
 abs(-31)
31
```

I do not know everything, a lot of developers do is not necessarily memorize everything. 


 

#### String 
A string is simply a series of characteres. Anything inside quotes is considred a string in PYthon, you can sue single or double quotes around your strings. 
python prgrams can also have text values called strings, or str. Awalsy surround your string in single quote character so python knows where the string begins and ends, string are explained in greater detail. If you ever see the error message, you probably forgot the final string quote character at the end of the string. such as: 

```python
>>> '1
  File "<stdin>", line 1
    '1
     ^
SyntaxError: EOL while scanning string literal


```

a string is simply a piece of text 
single quotes and trip quotes 

```python 
 type("hello world")
<class 'str'>
 long_string = '''
... this 
... this 
... this 
... this 
... '''
 print(long_string)

this 
this 
this 
this 

 

```




##### String concatenation and Replication 
the meaning of an operator may change based on the data types of the value next to. However, when + is used on two strings values, it joins the strings as the string concatenation operator. The + operator works with strings, but it is not addition in the mathematical sense. Instead it performs concatenation, which means joining the strings by linking them end to end. The expression evaluates down to a single, new string value that combines the text of two strings. 




```python 
>>> '1' + '2'
'12'
>>> 1 + 2 
3
>>> '1 + 2'
'1 + 2'


```

However, if you try to use the + operator on a string and an integer value, python will not know how to handle this. 
you code will have to explicity convert the integer to a string, because python cannot do this automatically . 
the * operator is used for multiplication when it operates on two integers or floating point values. but when the * operator is used on one string value and one integer value, it becomes the string replication operator. The expression evaluate down to a single string value that repeats the original a number of times equal to the integer value. String replication is a useful trick, but it is not used as often as a string concatenation. 

```python
>>> 5 * "1"
'11111'
>>> 5 * 1
5
>>> "5 * 1"
'5 * 1'


```



string concatenation means adding the strings together 
string concatenation only works with same types

```python 
 print("hello" + " world")
hello world
 str(100)
'100'
 print(type(int(str(100))))
<class 'int'>
```


str is essentially a piece of text and strings underneath the hood are stored in memory, as an ordered sequence of characters. Then this will be stored in our computers memory in an order so and will be stored in a place in memory 

#### String slicing 
you can access different part of the string using indexes 

string = value 
string[0]
string[start:end]
string[start:end:stepover]

string[::-1] start from last 
string[:-1]

```python
 string = 'hello this is is me'
 string[1]
'e'
 string[2]
'l'
 string[2:]
'llo this is is me'
 string[:5]
'hello'
 string[2:5]
'llo'
 string[2:8:2]
'lot'
 string[::1]
'hello this is is me'
 string[::-1]
'em si si siht olleh'

```

#### Immutability 

that means they cannot be changed. the only way thta we can remove this or change this is to completely reassign the value 



```python 
 string = 'hello this is is me' string[1] = 'a'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment

```

#### Escape Sequence 

in programming, whitespace refers to any nonprinting character, such as spaces, tabs, and end of line symbols. you can use whitespce to organize your output so it is easier for users to read 
you can also combine tabs and newlines in a single string. 

```python
>>> print("\t python")
	 python
>>> print("\npython")

python
>>> print("\npython\tlanguage")

python	language
>>> 


```

adding a slash 


```python
 weather = 'it\'s sunny'
 print(weather)
it's sunny
 weather = '\"it\'s sunny\"'
 print(weather)
"it's sunny"
 weather = 'hello!\n\t\"it\'s sunny\"'
 print(weather)hello!
        "it's sunny"
```

#### formatting strings 

add f at the beginning and tell python, this is going to be a formatted string 

print(f'{variable1} {variable2} {variable3}'.format(variable1,variable2,variable3))


print(f'{0} {1} {2}'.format(variable1,variable2,variable3))
always counting starting from 0 

```python

 variable1 = 1
 variable2 = 2
 variable3 = 3
 print(f'{variable1} {variable2} {variable3}'.format(variable1,variable2,variable3))
1 2 3

 print(f'{1} {0} {2}'.format(variable1,variable2,variable3))1 0 2

 name = 'Eddie'
 age = 28
 print('hi, {1}, you are {0}'.format(name,age))
hi, 28, you are Eddie
 print('hi, {1}, you are {0}'.format(name='Sally',age))
  File "<stdin>", line 1
SyntaxError: positional argument follows keyword argument
 print('hi, {1}, you are {0}'.format('Sally',age))
hi, 28, you are Sally

```

#### builtin functions & methods 

functions: len() 

```python
 hello = "hello"
 hello[0:len(hello)]
'hello'

```

method: string.method()

```python 
 hello = "hello"
 hello.capitalize() 
'Hello'
 hello = "hello"
 hello.capitalize() 
'Hello'
 hello.find('a') 
-1
 hello.find('o') 
4
 hello = "hello"
 print(hello.replace('l','a'))
heaao
```


 
##### changing case in a string with methods

title() didsplay each word in titlecase, where ach word begins with a capital letter. 


str_variable.title() 

a method is an action that python can perform on a piece of data. the dot variable.method() after it tells python to make the method act on the variable 

you can chagne a string to all uppercase or all lowercase letters like this, the lower(() method is particularly useful for storing data. Many time you won't want to trust the capitalization that your user provide, so you will convert strings to lowercase before storing them 
str_variable.upper() 
str_variable.lower() 


##### Stripping Whitespace 

extra whitespace can be confusing in our program. it is important to think about whitespace, because often you want to compare two strings to determine whether they are the same 
python can look for extra whitespace on the right and left sides of a string.

str_variable.rstrip() 
str_variable.lstrip()
str_variable.strip()

python makes it easy to elminate extraneous whitespace from data that people enter 

to ensure that no whitespace exists at the right end of a string, use the 
rstrip() method. To remove the whitespace from the string, you strip the whitespace from the right side of the string and then store that value back in the original variable. 

you can also stripe whitespace from the left side of a string using the lstrip() method or strip whitespace both sides at once using strip()

```python
>>> string_with_space = "\npython\tlanguage"
>>> print(string_with_space)

python	language
>>> print(string_with_space.lstrip())
python	language
>>> string_with_space = "\npython\tlanguage\t\t\t hahah"
>>> print(string_with_space)

python	language			 hahah
>>> print(string_with_space.rstrip())

python	language			 hahah
>>> print(string_with_space.strip())
python	language			 hahah
>>> 


```



### The str(), int(), and float() functions 

if you want to concatenate an ineger with a string to pass to a print, you will need the string form of it. The str() function can be passed an integer value and will evalauted to a string value version of it. a type error means python cannot recognize the kind of information you are using. python knows that the variable could represent either the numerical value or characters. 

the str(), int(), float() function will evalute to the string, integer, and floating-point forms of the value you pass, respectively. 

the str() funciton is handy when you have an integer or float that you want to concatenate to a string. the int() function is also helpful if you have a number as a string value that you want to use in some mathematics. 


```python


>>> str(9)
'9'
>>> str(1.9)
'1.9'
>>> int('-999')
-999
>>> int(1.222)
1
>>> float('1.222')
1.222
>>> float('1')
1.0
>>> float('1.00')
1.0

```


#### note
1. the int() function is also useful if you need to round a floating point number down  
2. if you pass a float value to int() or float() that it cannot evalaute as integer or float(), python will display an error message 
```python
>>> int('99.9999')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '99.9999'
>>> int(99.99)
99
>>> int("hello")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'hello'
>>> 
>>> float("hello")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: could not convert string to float: 'hello'


```



## input() function

python provides a built-in function called input that gets input from the keyboard. When this function is called, the program stops and waits for the user to type something. when the user presses Return or Enter, the program resumes and input returns what the user typed as a strig 


```python
>>> name = input("what is your name?\n")
what is your name?
>>> eddie 
>>> print("name")
name
>>> 


```

if you expect the user to type an integer, you can try to convert teh return value to int using the int() function 

```python

>>> age = int(input("what is your age?\n"))
what is your age?
28
>>> print("your age is:" + str(age))
your age is:28
>>> 


```



### Expressions versus statements 

expression is a piece of code that produces a value 

a statement, on the other hand, is an entire line of code, not this entire thing but an entire line of performs sort of actions 



### list 
a list is an ordered sequence of objects that can be of any type 

list is a data structure, data structure is a way for us to organize information and data into, a folder or a cupboard of a box, that container has different pros and cons of accessing that data, removing data, writing data 

the key here is that the square brackets allow us to contain information and data like strings, integers. I can access it again with square brackets and simply say, I want item zero 

```python

 li = [1, 2, 3, 5, 6, ]
 print(li)
[1, 2, 3, 5, 6]
 li = ['a','b','c','d']
 print(li)
['a', 'b', 'c', 'd']
 li = ['a','b','c','d']
 print(li)
['a', 'b', 'c', 'd']
 li[1]
'b'
 li[2]
'c'
 li[3]
'd'
 li[4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
 
 amazon = ["notebooks","sunglass","wireless"] amzon[1]
 amazon[1]
'sunglass'

```
### list slicing and matrix

strings are immutable, that means we cannot change them. When we use list, we are able to change the element. In that sense, lists are mutable, we simpy replace on the memory 

```python
 amazon = ["notebooks","sunglass","wireless", "toys", "grapes"]
 amazon[0:2]
['notebooks', 'sunglass']
 amazon[0:4]
['notebooks', 'sunglass', 'wireless', 'toys']
 amazon[2:4]
['wireless', 'toys']
 amazon[2:4:2]
['wireless']
 amazon[0:4:2]
['notebooks', 'wireless']
 amazon[2] = "changed"
 amazon
['notebooks', 'sunglass', 'changed', 'toys', 'grapes']
```

matrix is an array of another array, or array of arrays. this comes a lot with machine learning 

using matrices, we can do a lot of heavy computation underneath the hood

when you want to access a matrix 


```python
 matrix = [
... [1,2,3],
... [[1,2,3],[1,2,3]],
... [1,2,3,4,5],
... ]
 matrix
[[1, 2, 3], [[1, 2, 3], [1, 2, 3]], [1, 2, 3, 4, 5]]

 matrix[1][1]
[1, 2, 3]
```
### list methods 
list_object.append(value) appends the list element at the end 
```python
 li.append(6)
 li
[1, 2, 3, 4, 5, 6]

```


list_object.pop(index) pop off whatever in the end of the list 

```python 

 li.pop() 
6
 new_l.pop(3)
4
```

list_object.insert(index,value) insert element inplace does not modify the whole list 

```python 

 new_l
[1, 3, 100, 5, 10, 101, 20]
 new_l = li 
 new_l
[1, 2, 3, 4, 5]
 new_l.insert(3,100)
 new_l
[1, 2, 3, 100, 4, 5]
 li
[1, 2, 3, 100, 4, 5]
```


list_object.remove(value), remove only working in place, it just simply changes whatever list you give it. it returns None. 

```python 
 new_l.remove(20)
 new_l
[1, 3, 5, 10, 101]

 new_l.remove(2)
 new_l
[1, 3, 100, 4, 5, 10, 101, 20]
```

list_object.clear() clears up the whole list 

```python 

 new_l.clear() 
 new_l
[]
```

list_object.index(value) a nifty way thta returns the index of the value in the list 

```python 
 new_l = ['a','b','c','d','e','f']
 new_l.index(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 3 is not in list
 new_l.index()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: index expected at least 1 argument, got 0
 
 new_l.index('c')
2
```

extend([a list]) extend the list with another list 

```python

 new_l.extend([10,101,20]) 
 new_l
[1, 2, 3, 100, 4, 5, 10, 101, 20]

```


in keyword: check if the element in a list_object. 

```python 


 print('d' in new_l)
True

```

list_object.count(value): how many times this value occur in the list 

```python 

 new_l.count('c')
1

```

list_object.sort() sort the list, and it modifies the list  

sorted(whole_list) does not modify the list, instead it returns the list 

```python 

 new_l = [6,3,2,1,8]
 new_l.sort() 
 new_l
[1, 2, 3, 6, 8]
 new_l = [6,3,2,1,8]
 sorted(new_l) 
[1, 2, 3, 6, 8]
 new_l
[6, 3, 2, 1, 8]
```

list_object.reverse() it reverses the order not reverse same as list_object[::-1]

```python
 new_list = [1,2,3,4,5,6]
 new_list.reverse()
 new_list
[6, 5, 4, 3, 2, 1]
 new_list = [1,2,3,4,5,6]
 new_list[::-1]
[6, 5, 4, 3, 2, 1]
 

```

new_list = old_list, you references to the list 
new_lst = old_list[:] you copy the whole list. 
new_list = old_list.copy() you copy the whole list.

```python
 old_list = [6,3,2,1,8]
 new_list = old_list
 new_list[1] = 123213
 old_list
[6, 123213, 2, 1, 8]
 new_list
[6, 123213, 2, 1, 8]
 new_list = old_list[:]
 new_list[1] = 123213
 old_list
[6, 123213, 2, 1, 8]
 new_list[1] = 654643
 old_list
[6, 123213, 2, 1, 8]
 new_list
[6, 654643, 2, 1, 8]
 new_list = old_list.copy(
... )
 new_list = old_list.copy()
 new_list
[6, 123213, 2, 1, 8]
 old_list
[6, 123213, 2, 1, 8]
 old_list
[6, 123213, 2, 1, 8]

```

if you want the array to be in ascending order, you use list_object.sort(). but if you want the array to be in descending order, you use list_object.sort().reverse() 

```python

 old_list.reverse() 
 old_list
[8, 1, 2, 123213, 6]
```


to generate a list of numbers quickly use list(range(start, end)) function:

```python 
 list_of_one_hundred
[range(1, 101)]
 list_of_one_hundred = list(range(1,101))

```

list_object.join(), join actually works on strings, it is a string method. we have an empty string, we take an iterable, this combines a list into a string 



```python
 something = ''
 something.join(['a','b'])
'ab'
 something
''
 print(something)

 another = something.join(['a','b'])
 another
'ab'
 something = ''
 another = ''
 another = someting.join(['hi','this','is','eddie'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'someting' is not defined
 another = something.join(['hi','this','is','eddie'])
 another
'hithisiseddie'
 

```
### list unpacking 

assign list to each item in a variable 
variable1, variable2, variable3, *other = [ list_of_elements ]

```python 

 a,b,c,*other = [1,2,3,4,5,6,7,8,9,10]
 a
1
 b
2
 c
3
 other
[4, 5, 6, 7, 8, 9, 10]
```



### Dictionary 

in other languages it may call hastable or maps 

dict() is a data structure, it is an unrodered key and value pair, unordered means that they are not right next to each other in memory. these data are all scattered in the memory, so a dictionary is an unordered key value pair 

 the way for us to oragnize the data 

 dictionary = {
  'key1':'value1',
  'key2':'value2',
  'key3':'value3',
  }


```python
 dictionary = {
... 'key1':'value1',
... 'key2':'value2',
... 'key3':'value3',
... }
 dictionary
{'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

 list_of_dict = [
... { 'a':1,
... 'b':2,
... 'c':3,
... 'd':4,
... },
... { 'a':3,
... 'b':4,
... 'c':5,
... 'd':6,
... }
... ]

```

### Dictionary keys 
we can use any values to denote a key 
1. we cannot use a list to denote it, it is an unhasable type 
dictionary keys need to have a special property, a key needs to be immutable, that is a key, cannot change .  numbers , str, boleans are mutable 

2. a key in a dictionary must be unique, anytime I add a duplicate key, it will overwrite it 

3. dictionary_object = dict(key='value',key='value',key='value')

```python 

 dictionary = {
... 1:1
... }
 dictionary = {
... 'a' : 1
... }
 dictionary = {
... 1.2 : 1
... }
 dictionary = {
... 'this is ' : 1
... }
 dictionary = {
... [1,2,3] : 1
... }
 dictionary = {
... True : 1,
... }
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'


 new_dict = dict(name='eddie')
 new_dict
{'name': 'eddie'}
 new_dict = dict(name='eddie',1=2)
  File "<stdin>", line 1
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
 new_dict = dict(1=2)
  File "<stdin>", line 1
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
 new_dict = dict(name='eddie',age=28)
 new_dict
{'name': 'eddie', 'age': 28}
 
 

 dictionary = {
... 1 : 1,
... 1 : 1,
... 1 : 1,
... 1 : 1,
... 1 : 1,
... 1 : 1,
... 1 : 1,
... }
 dictionary[1]
1

```

### dictionray methods 

dictionary_object.get() find a key 

dictionary_object[ key ] may not find the key and results in an error 


 dictionary 
{'age': 20, 'name': 'Eddie'}
 dictionary.get("something")
 dictionary.get("age")
20
 dictionary["age"]
20
 dictionary["something"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'something'
 

in keyword: 

```python
 new_dict = dict(name='eddie',age=28)
 print('eddie' in new_dict)
False
 print('name' in new_dict)
True
 print('age' in new_dict)
True

```

dictionary.keys() check keys in a dictionary 
'keys' in dictionary.keys() 

dictionary.values() check vlaues in a dictionary 
'value' in dictionary.values() 


```python

 new_dict = dict(name='eddie',age=28)
 'name' in new_dict.keys() 
True
 'eddie' in new_dict.values() 
True
 'ed' in new_dict.values() 
False

```

dictionary.items() grabs the entire item key and value pair 

```python
 new_dict.items() 
dict_items([('name', 'eddie'), ('age', 28)])
```

dictionary.clear() clears out the dictionary 

```python
 new_dict.clear() 
 new_dict
{}

```


dictionary.copy() allows us to copy a dictionary 


```python 
 new_dict = dict(name='ed',age=23,gender='m') another_dict = new_dict.copy() 
 

```

dictionary.pop(key) removes an element from the dictionary 

dictionary.popitem() randomly pops up something 

```python
 new_dict = dict(name='ed',age=23,gender='m') another_dict = new_dict.copy() 
 another_dict
{'name': 'ed', 'age': 23, 'gender': 'm'}
 another_dict.pop(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
 another_dict.pop('age')
23
 another_dict
{'name': 'ed', 'gender': 'm'}

```

dictionary.update() which updates a key value pair


```python 
 another_dict
{'name': 'ed', 'gender': 'm'}
 another_dict.update('gender':'f')
  File "<stdin>", line 1
    another_dict.update('gender':'f')
                                ^
SyntaxError: invalid syntax
 another_dict.update({'gender':'f'})
 another_dict
{'name': 'ed', 'gender': 'f'}
```

### tuple 

a tuple is like lists, but unlike lists, we cannot modify them. they are immutable, you can access it and index it. tuple is a value key in dictionaries 


tuple_object = (values)


it is pretty much the same as the list but the difference is 

1. if you do not need to change the list, that makes things easiesr because it tells others programmers should stay away from this, 
2. make the code more predictable, they are less flexible and more efficient 

```python
 my_tuple = (1,2,3,4,5,) 
 my_tuple[2] = 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
 my_tuple[2] 
3

```

you can slice the tuple 

```python

 my_tuple = (1,2,3,4,5,) 
 my_tuple[3:5]
(4, 5)
 my_tuple[3:5:2]
(4,)

```

you can unpack the tuple: 

```python

 my_tuple = (1,2,3,4,5,) 
 a, b, *other = my_tuple
 a
1
 b
2
 other 
[3, 4, 5]
 

```

tuple has only len() , count() and index() we care about 

```python 

 my_tuple = (1,2,3,4,5,) 
 my_tuple.count(3)
1
 my_tuple.index(3)
2
 
 len(my_tuple)
5

```
I did not put your in sleep, you just started out. these are building foundations. 



### set 

set is an unordered collection unique objects, set is not subscriptable 

```python 

 myset[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not subscriptable
 myset[2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not subscriptable

```

```python

 myset = {1,2,3,4,5,1}
 myset
{1, 2, 3, 4, 5}
 myset = {1,2,3,4,5,1,2,3,4,5}
 myset
{1, 2, 3, 4, 5}
 
```

set_object.add(value) appends a unique value to the end of the set 

```python
 myset
{1, 2, 3, 4, 5}
 myset.add(1000)
 myset
{1, 2, 3, 4, 5, 1000}

```

form a set from a list and remove all the duplicate values 

list_object = [ values ]
set(list_object)

in keyword to find if an element exists in a set 

```python
 set_object = set([1,2,3,4,1,2,3,4])
 set_object
{1, 2, 3, 4}

 1 in set_object
True
 

```
alternatively you can convert a set to a list 

```python
 set_object = set([1,2,3,4,1,2,3,4])
 list_object = list(set_object)
 list_object
[1, 2, 3, 4]

```

set_object.copy() will create a copy of the original set 


```python
 set_object = set([1,2,3,4,1,2,3,4])
 another_set = set_object.copy() 
 another_set.clear() 
 another_set
set()
```

my_set.difference(your_set): find the different elements in a set 

```python
 my_set = {1,2,3,4,5,5}
 your_set = {7,4,2} 
 my_set.difference(your_set) 
{1, 3, 5}

```


set_object.discard() removes an element from a set if it is a member 

```python
 my_set = {1,2,3,4,5,5}
 my_set.discard(3)
 my_set 
{1, 2, 4, 5}

```


set_object.difference_update(your_set), removes the overlapped items in two sets 

this returns none and it just modifies my set 

```python
 my_set = {1,2,3,4,5,5}
 your_set = {7,4,2} 
 my_set.difference_update(your_set) 
 my_set
{1, 3, 5}
 

```

set_object.intersection(another_set) gives the intersection of these two sets have 

you can also do 

##### myset & yourset 

```python

 my_set = {1,2,3,4,5,5}
 your_set = {7,4,2} 
 my_set.intersection(your_set) 
{2, 4}

```


set_object.disjoint(another_set), do they have anything in common? are they overlapping, if it has nothing in common then it returns True, False otherwise  

```python

 my_set = {1,2,3,4,5,5}
 your_set = {7,4,2} 
 my_set.isdisjoint(your_set) 
False
 my_set = {1,2,3,4,5}
 your_set = {1,2} 
 my_set.isdisjoint(your_set) 
False
 my_set = {1,2,3,4,5}
 your_set = {100} 
 my_set.isdisjoint(your_set) 
True
```


set_object.union(another_set) united two set together with no duplicate items in both and it returns a new set 
you can also do: 
##### myset | yourset 

```python 

 my_set = {1,2,3,4,5}
 your_set = {100} 
 my_set.union(your_set)
{1, 2, 3, 4, 5, 100}
 my_set = {1,2,3,4,5}
 your_set = {100,1,2,3,4} 
 my_set.union(your_set)
{1, 2, 3, 4, 5, 100}
 

```


set_object.issubset() is my set the subset of your set, the entirety is in another set 
set_object.issuperset(), it does not encompass your set 



```python 
 my_set = {1,2,3}
 your_set = {1,2,3,4} 
 my_set.issubset(your_set) 
True
 your_set.issubset(my_set) 
False
 your_set.issuperset(my_set) 
True
 

```

#### understanding data structure
when to use what, this takes experience and pratice 
when should you use a list or a list, a dictionary does not order, if you use users

dictionary uses more information than a list 
there is no way you can memorize all of them 






## Reference
[x] How to become a Python 3 Developer and get hired! Build 12+ projects, learn Web Development, Machine Learning + more!

[x] Second Edition of Automate the Boring Stuff with Python, 1 Python Basics

[x] Python for everybody 


[x] Python Crash Course



##  Appendix A terminology: Intepreter and compiler (Optional)
Python is a high-level language intended to be relatively straightfoward for humans to read and write and for computers to read and processs 
other high level languages include Java, C=+ and more. 

The actual hardware inside the CPU does not understand any of these high level languages. 

The CPU understands a language we call machine language. Machine language is very simple and frankly very tiresome to write because it is represented all in zeros and ones 


Machine languages seems quite simple on the surface, given that there are only zeros and ones, but its syntax is even more complex and far more intricate than Python 

Instead we build various translators to allow programmers to write in high-level languages like Python or JavaScript and these translators convert the programs to machine language for actual execution by the CPU 


Machine language is not portable across different types of hardware. Programs written in high level languages can be moved between different computers by using a different interpreter on the new machine or recompiling the code to create a machine language version of the program for the new machine 


an **interpreter** reads the source code of the program as written by the programmer, parses the source code, and interprets the instructions on the fly. Python is an interpreter and when we are running python interactively, we can type a line of python and python processes it immediately and is ready for us to type another line. 



Even though we are typing these commands into python one line at a time. python is treating them as an ordered sequence of statements with later statements able to retrieve data creaed in earlier statement. 

it is the nature of an interpreter to be able to have an interactive conversion. a compiler needs to be handed the entire program in a file, andthen it runs a process to translate the high level source code into machine language and then the compiler puts the resulting machine language into a file for later execution 





##  Appendix B Errors 
programs will crash if they contain code the computer cannot understand, which will cause python to show an error message. An error message won't break your computer, though, so do not be afraid to make mistakes

A *crash* just means the program stopped running unexpectedly 


as your programs become increasing sophisticated, you will encounter three general types of errors

* syntax errors: a syntax error means that you have violated the grammar rules of python. python does its best to point right at the line and character where it noticed it was confuse. So the line and character that python indicates in a syntax error may just be a starting point for your investigation. Basically syntax errors indciates that the interpreter does not recognize something in the code as valid python code. Errors can come from a vareity of sources. Syntax errors are also the least specific kind of error, so they can be difficult and frustrating to identify and correct 



* logic error: a logic error is when your program ahs good sytax but there is a mistake in order of the statements or perphas a msitake in how the statements relate to one another. 


* semantic errors: a semantic error is when your description of the steps to take is syntactically perfect and in the right order, bu there is simply a msitake in the program. the program is perfectly correct but it does not do what you intended for it to do. Your instructions were syntactically correct, they sadly contained a small but undetected semantic error.  

As your progress through the rest of the tutorial, do not be afraid if the concepts do not seem to fit together well the first time. It takes time to absorb before it feels natural. That leads to some confusion as we visist and revisit topics to try to get you to see the big picture while we are defining the tiny fragment that make up the big picture. Look forward and backwards and read with a light touch. By skimming through more advanced material without fully understanding the dtails, by reviewing previous material and even redoing earlier exercises, you will realize that you actually learned a lot of materials. When you look up from pounding away at some rock with a hammer and chisel and step away and see that you are indeed building a beautiful sculpture, elegant. 




## Exercise: Write and Disecting a program 
with your new program open in the file editor, let us take a quick tour of the instructions it uses by looking at each line of code 


