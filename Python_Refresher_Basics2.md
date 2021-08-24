# Python Basics Continued: Control Flow, Conditionals, Loops, Functions 


# Control flow 
we have learnt about basic python data types, we also learned a bit about some of the terms and best pratices to form actions on these data types 

we will discover the true power of programming and specifically programming for machines. The power comes when we start to incorporate the idea of maybe running multiple lines over and over. 


so you know the basics of individual instructions and that a program is just a series of instructions. BUt th real strength of programming is not just running or executing one instruction after another like a weekend errand list 

programming often involves examining a set of conditions and deciding which action to take based on those conditions. Based on how the expressions evaluate, the program can decide to skip instructions, repeat them or choose one of serveral instructions to run. In fact, you almost never want your programs to start from the first line of code and simply execute every line, straight to the end. 


Flow control statements can decide which python instructions to execute under which conditions 



## Boolean Expressions 

while the integer, floating point, and string data types have an unlimited number of possible values, the *boolean* data type has only two values: True and False

a *boolean* expression is an expression that is either true or false. (Boolean is capitalized because the data type is named after George boole). When typed as Python code, the boolean values TRue and False lack the quotes you place around strings, and they always start with a capital Tor F, with the rest of the word in lowercase. True and False are special values that belong to the class bool; they are not strings 

*Comparison operators* compare two values and evaluate down to a single Boolean value.These operators evaluate to True or False depending on the values you give them.  
the == operator is one of the comparison operators; the others are 



| Symbols    | Definition                      |
|------------|---------------------------------|
| x != y     | x is not equal to y             |
| x > y      | x is greater than y             |
| x < y      | x is less than y                |
| x >= y     | x is greater than or equal to y |
| x <= y     | x is less than or equal to y    |
| x is y     | x is the same as y              |
| % is not y | x is not the same as y          |


note: you might have noticed thta the == opreator equal to has two equal signs, while the = opreator assignment has one equal sign. it is easy to confuse these two operators with each other 
a common error is to use a single equal sign = instead of a double equal sign ==. remember that = is an assignment operator and == is a comaprison operator. there is no such thing as =< or =>
1. the == opreator equal to asks whether two values are the same as each other 
2. the = operator/assignment puts the value on the right into the variable on the left 




```python
>>> 1 == 2 
False
>>> 1 == 1
True
>>> 1 <= 2
True
>>> 1 <= 2 
True
>>> 1 >= 2
False
>>> 1 >= 1 
True
>>> 1 < 2 
True
>>> 1 > 2 
False
>>> 1 != 2 
True
>>> 1 is not 2 
<stdin>:1: SyntaxWarning: "is not" with a literal. Did you mean "!="?
True
>>> 1 is 2 
<stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
False
>>> x = 1 
>>> y = 1
>>> x is y
True
>>> z = 3 
>>> x is not z 
True
>>> 


```

## Logical/Boolean Operators 
there are three logical operators: *and*, *or*, *not*. The semantics meaning of these operators is similar to their meaning in English. Lke comparison operator, they evaluate these expressions down to a Boolean value. 


Finally, the *not* opertor negates a boolean expression 

strictly speaking, these operands of the logical operators should be boolean expressions, but python is not very strick 
any nonzero numbers is interpreter as true 

this flexibility can be useful, but there are some subtleties to it that might be confusing.


#### Binary Boolean Operators 
the *and* and *or* operators always take two Boolean values or expressions, so they are considered binary opreators. the *and* operator evaluates an expression to True if both boolean values are TRue; otherwise, it evaluates to False. 
On the other hand, the or operator evaluates an expression to True if either of the two Boolean values is True. if both are False, it evaluates to False 



#### the not operator 
unlike *and* and *or*, the not operator opreates on only one Boolean value or expression. The not operator simply evaluates to the opposite boolean value. 
much like using double negative in speech or writing, you can nest not operator, though there is never not no reason to do this in real programming 

| Expression       | Evaluation |
|------------------|------------|
| True and True    | True       |
| True and False   | False      |
| False and True   | False      |
| False and False  | False      |
| True or True     | True       |
| True or False    | True       |
| False or True    | True       |
| False or False   | False      |
| not False        | True       |
| not True         | False      |

####  TRuthy and Falsey values 
there are some values in other data types that conditions will consider equivalent to True and False. When used in condition, 0 and '' (the empty string) are considered False, while all other values are considered True 





#### Mixing boolean and comparison operators 
since the comparison operator evaluate to Boolean values, you can use them in expressions with the Boolean operators 
recall that the *and*, *not* operators are called boolean opreators because they always operate on the boolean values *True* and *False*


```python 

>>> True and True 
True
>>> True and False 
False
>>> False or True 
True
>>> False or False 
False
>>> False and False 
False
>>> not False 
True
>>> not True 
False
>>> 1 + 2 == 3 
True
>>> 1 + 2 == 3 and 1 + 2 == 4
False
>>> 1 + 2 == 3 or 1 + 2 == 4
True
>>> 1 + 2 == 3 and not 1 + 2 == 4
True
>>> 



```

### Short-circuit evaluation of logical expressions 
when python is processing a logical expression, it evaluates the expression from left to right. Because of the defintion of and, False and TRue, so the whole expression is False regardless of whether the rest evaluates to True or False

when python detects that there is nothing to be gained by evaluating the rest of a logical expression, it stops its evaluation and does not do the computations in the rest of the logical expression. When the evaluation of a logical exprseison stops because the overall valeu is already known, it is called short-circuiting the evaluation

While this may seem like a fine point, the short-circuit behaviour leads to a clever technique called the guardian pattern 

```python 
2 >= 2 and (2/0) > 0 and 0 != 0
```


in the logical expression, it is false so we never reach the next statement  

```python

2 >= 2 and (2/0) > 0 and 0 != 0
```
## Elements of flow control 
flow control statements often start with a part called the conditoin, and all are followed by a block of code called the clause. 

### conditions
the Boolean expression you have seen so far could all be considered conditions, which are the same things as expressions; condition is just a more specific name in the context of flow control statements. Conditions always evaluate down to a Boolean value, True or False. A flow control statement decides what to do based on whether its condition is True or False, and almost every flow control statement uses a condition 

### Blocks of Code 
lines of python code can be grouped together in *blocks*. you can tell when a block begins and ends from the indentaiton of the lines of code. there ar three rules for blocks
1. blocks begin when the indentation increases 
2. blocks can contain other blocks 
3. blocks end when the indentation decreases to zero or to a containing block's identation 

blocks are easier to understand by looking at some indented code. 



### Program & Conditional Execution 

python started executing instrucitons at the top of the program going down, one after another. The program execution or simply, execution is a term for the current instruction being executed. If you print the source code on papers and put your finger on each line as it is executed, you can think of your fingers as the program execution. 

Not all programs execute by simply going straight down, however. if you use your finger to trace through a program with flow control statements, you will likely find yourself jumping around the source code based on conditions, and you will probably skip entire clauses 






conditional statements give us this ability to check conditions and change the behaviour of the prorgam accordingly 

the boolean expression after the if statement is called condition. We end the if statement with a colon character : and the lines after the if statement are indented 

if the logical condition is true, then the indtened statement gets executed. if the logical condition is false, the indented statement is skipped 

the statement consists of a header line that ends with the colon character : followed by an indented block. Statements like this are called compound statements because they stretch across more than one line 

there is no limit on the number of statements that can appear in the body, but there must be at least one. Occassionally, it is useful to have a body with no statement usually as a place holder for code you have not written yet. in that case, you can use the pass statement, which does nothing 


### if statement 
the most common type o flow control statement is the if statement. An if statement's clause(that is, the block following the if statement) will execute if the statement's condition is True. The clause is skipped if the condition is false 
if statement allows you to examine the current state of a program and respond appropriately to that state 

in plain English, an if statement could be read as "if this condition is true, execute the code in the cluase"

if you enter an if statement in the python interpreter, the prompt will change from three cheverons to three dots to indicate you are in the middle of a block of statements 

in python, an if statement consists of the following:
1. the if keyword 
2. a condition
3. conlon
4. starting from the next line, an indented block of code 



```python
if <condition>:
    <statement> 

```



### else statements -- alernative execution 

an if clause can optionally be followed by an else statement. The else clause is executed only when the if statement's condition is false. In plain English an else statement could be read as, "if this condition is true, execute this code. Or else, execute the code". an else statement does not have a condition, and in code, an else statement always consists of the following 

1. the else keyword 
2. a colon 
3. starting on the next line, an indented block of code called the else clause 




a second form of the ifstatement is alternative execution, in which there are two possibilties and the condition determines which one gets executed. The syntax looks like:

```python
if <condition>:
    <statement>
else:
    <statement>
```


since the condition must either be true or false, exactly one of the alternatives will be executed. The alternatives are called branches, because they are branches in the flow of execution 


### elif statement - chained conditionals 
sometimes there are more than two possibiltie and we need more than two branches.while only one of the if or else clause will execute, you may have a case where yo uwant one of many possible clauses to execute. the elif statement is an else if statement that always follows an if or another elif statement. it provides another condition that is checked only if any of the previous conditions were False. in code, an elif statement always consits of the following 

1. the elif keyword 
2. a condition 
3. a colon
4. starting on the next line, an indented block of code called the elif 


 One way to express a computation like that is a chained conditional: 


```python
if <condition>:
    <statement>
elif:<condition>:
    <statement>
else:
    <statement> 
```


elif is an abbreviation of else if. again, exactly one branch will be executed. There is no limit on the number of elif statement. If there is an else clause, it has be at the end, but there does not have to be one 
each condition is checked in order. there the first is false, the next is checked, and so on. If one of them is true, the corresponding branch executes, and the statement ends. Even if more than one condition is true, only the first true branch executes 
however, if both of the conditions are false, then both of the clases are skipped. it is not guaranteed that at least one of the clauses will be executed. when there is a chain of elif statement, only one or none of the clauses will be executed. Once one of the statement's conditions is found to be True, the rest of the elif clauses are automatically skipped 


in plain English, this type of flow control structure would be, "if the first condition is true, do this. Else, if the second condition is true, do thta, toherwise, do something else". WHen you use all these staements together, remember these rules about how to order them to avoid bugs. First there is always exactly one if statement. Any elif statement you need should follow the if statement. Second, if you want to be sure that at least one clause is executed, close the structure with an else statement 



```python
>>> if name == 'Alice':
...     print("hello," + name)
... elif age < 12:
...     print("kiddo")
... else:
...     print("you are nothing")
... 
hello,Alice


```


### Nested conditionals 

one conditional can also be nested within another. we could have written branches like this: 
```python
if <condition>:
    <statement>
elif:<condition>:
    <statement>
else:
    <statement>
    if <condition>:
        <statement>
    else:
        <statement>
 
```

the outer conditional contains branches. 
Although the indentation of the statements makes the structure apparent, nested conditionals become difficult to read very quickly. In general, it is a good idea to avoid them when you can 
logical operators often provide a way to simplify nested conditional statements. 




## Iteration 
computers are often uesd to automate repetitive tasks. Repeating identical or similar tasks without making errors is something that comptuers do well and people do poorly. Because iteration is so common. Python provides several features to make it easier to blastoff. 

### the while statement 

one form of iteration in python is the while statement.  Yu can make a block of code execute 

you can almost read the while statement as if it were english. 
more formally, here is the flow of execution for a while statement 

1. evaluated the condition, yielding True or False 
2. if the condition is false, exit the while statement and continue execution at the next statement 
3. if the condition is true, execute the body and then go back to step 1

This type of flow is called a loop because the third step loops back around to the top. We call each time we execute the body of the loop an iteration. 
The body of the loop should change the value of one or more variables so that eventually the condition becomes false and the loop terminates. We call the variable that changes each time the loop executes and controls when the loop finishes the iteration variable. if there is no iteration variable, the loop will repeat forever, resuling in an infinite loop 

in code, a while statement always consists of the following:
1. the while keyword 
2. a condition 
3. a colon
4. starting on the next line, an idented block of code called the while clause 


you can see that a while statement looks similar to an if statement. the difference is how they behave. At the end of an if clause, the program execution continues after the if statement. but at the end of a while clause, the program execution jumps back to the start of the while statement. the while clause is often called the while loop or just hte loop 




### infinite loops 
an endless source of amusement for programmers is the observation that the directions and lather, rinse, repeat are an infinite loop because there is no iteraiton variable telling you how many times to execute the loop 

if you make the mistake, you will learn quickly how to stop a runway python process on your computer or find where the power off button is on your computer. this program will run forever or until you batter runs out because the logical expression at the top of the loop is always true by virtue of the fact that the expression is the constant value True. While this is a dysfunctional infinite loop, we can still use htis pattern to build uesful loops as long as we carefully add code to the body of hte loop to explicitly exit the loop using break when we have reached the exit condition

```python 
counter = 0
while counter < 1:
    print(counter)
```

```python
>>> counter = 0
>>> while counter <= 10: 
...     counter += 1
...     if counter == 5:
...             continue
...     print(counter)



```

if you ever run a program that has a bug causing it to get stuck in an infinite loop press CTRL+C. this will send a KeyboardInterrupt error to your program and cause it to stop immediately 


### break statement 
sometimes you do not know it is time to end a loop until you get half way through the body. In that case you can write an infinite loop on purpose and then use the break statement to jump out of the loop 

this loop is obviously an infinite loop because the logical expression on the while statement is simply the logical constant True 

there is a shortcut to getting the programming execution to break out of a whle loop's clause early. If the execution reaches a break statement, it immediately exits the while loop's clause. In code, a break statement simply contains the break keyword 





```python 
>>> counter = 0
>>> while counter <= 10: 
...     counter += 1
...     print(counter)
...     if counter == 5:
...             break
... 
1
2
3
4
5


```

### continue 
sometiems you are in an iteration of a loop and want to finish the current iteration and immediately jump to the next iteration. in that case you can use the continue statement to skip the next iteraiton without finishing the body of the loop for the current iteration 

line break statements, continue statements are used inside loops. when the program execution reaches a continue statement, the program execution immediately jumps back to the start of the loop and reevaluated the loop's condition 



```python
>>> counter = 0
>>> while counter <= 10: 
...     counter += 1
...     if counter == 5:
...             continue
...     print(counter)
... 
1
2
3
4
6
7
8
9
10
11

```

### for loop and the range() function 

the while loop keeps looping while its condition is True(which is the reason for its name), but what if you want to execute a block of code only a certain number of times, you can do this with a for loop statement and the range() function 

somtimes we want to loop through a set of things, the lines in a file, or a list of numbers.

when we have a list of things to loop through, we can construct a definite loop using a for statement. we call the while statement an indefinite loop because it simply loops until some condition becomes False, whereas the for loop is looping through a known et of items so it runs through as many iterations as there are items in the set 

the syntax of a for loop is similar to the while loop in that there is a for statement and a loop body.

In particular, a list of item is the *iteration* variable for the for loop. the variable changes for each iteration of the loop and controls when for loop completes. the iteration variable steps successively through the items in the variable 




#### loop patterns 
often we use a for or while loop to go through a list of items or the contents of a file and we are looking for something such as the largest or smallest value of the data we scan through 

these loops are generally constructed by:
1. initializing one or more variables before the loop starts 

2. performing some computation on each ite in the loop body, possibly changing the variables in the body of the loop 

3. looking at the resulting variables when the loop completes 


we will use a list of numbers to demonstrate the concepts and construction of these loop patterns 



in the loop we do use the iteration variable/ 




### identation aka spacing 

python is, however, is unique becaues the identiation in spaces that we see
the interpreter would actually see the space and say necaues there are spaces here 
it knows there is a block 
in python, the rule is you can use spaces or tabs, if you use spaces you usually use four spaces with proper format 










### conditional logic 

python has boolean values True or False, this is verified. all values are considered truthy except for the following, which are falsy 
None
False 
0
0.0
0j 
Decimal(0)
Fraction(0,1)
[] empty list 
{} empty dict 
() empty tuple 

```python 
 is_true = True 
 is_False = False 

```

```python

 bool(1)
True
 bool(2)
True
 bool(-1)
True
 bool(0)
False
 bool(-0)
False
 bool(False)
False
 bool(True)
True
 bool("")
False
 bool("2")
True
 bool("1.1")
True
 bool("0.0")
True
 

```


### if statement 

if statements only evaluate the condition down to True or False 

```python 
if <condition>: 
    <statement>
```

if <condition> condition evaluates to true or false. if this is true, runs everything inside the identation. we are able to skip the lines 

```python 
if <condition>: 
    <statement>
else:
    <statement>
```


if it is not true, it will skip that if statement and run else otherwise it ignores the else block 

it controls the flow of our code 

```python 
if <condition>: 
    <statement>
elif:
    <statement>
else:
    <statement>
```

if it is true, jumps to elif, it goes through here, so I am going to ignore this and ignore this and then do it 
else is the backup statement, if all things failed, then just do this 

```python

 if variable < 10:
...     print("it is less than 10")
... elif variable >= 10 and variable < 20:
...     print("10 < variable < 20")
... else:
...     print("variable > 20")
... 
10 < variable < 20

```


### Ternary operators 

you can only use these on certain conditional logics, it is evalauted to a value based on a condition to be True or False. a nice shorthand way if condition is true or false 


condition_if_true if condition else conditoin_if_else

the ordering is a bit confusing 

```python 

 x ** 2 if x > 2 else x ** 3
100

```

### Logical operators 

equal to "="
not equal "!="
greater ">"
less than "<"
greater and equal to ">="
less than and equal to "<="


or keyword, if either one of these conditions one, it executes the first condition 

and keyword, if either one of these conditions are false, it does not care the rest. others will be a waste of work  

not keyword, it negates the condition and get the opposite and it evaluates to the opposite 

it is to develop the skills to become an employable programmer 

```python 
 1 <  2 < 3 < 5 < 6 < 7 < 8
True

```
 
 is keyword versus == 

== checks the equality 


 ```python 
 True == 1
True
 '' == 1
False
 [] == 1
False
 () == 1
False
 {} == 1
False
 10 == 10.0 
True
 [] == []
True
 True == bool(1)
True
 ```

 == does not check in different types and do type conversion 
 is keyword checks the type in memory location 

 everytime I create a list, it creates a new chunk in memory 

 ```python
 '1' == 1
False
 print(True is True)
True
 print(variable is int)
False
 print(type(variable) is int)
True
 [] is []
False
 ```



### Short circuiting 


condition1 or condition2 
condition1 and condition2

```python

 True and False 
False
 False and True and True and True 
False
 True or True or False 
True

```



### for loops 

loops gets to a new power of our programming, it allows us to run things over and over this is where the machine excels 
it iterate over antyhing that has a collection of items

what is a iterable?  iterable simply means a collection or object that can iterate over, it is a collection of items, because they can be iterated such as list, tuple. you are looping 

for item in iterables:
    <statement>

```python 

 for item in 'string is here':
...     print(item)
... 
 for item in (1,2,3,4,5,6):
...     for x in ['a','b','c','d']:
...             print(item , " ", x)

```

you can iterate through the items of a dictionary 

```python
 dictionary = {
... 'name' : 'Eddie',
... 'age' : 29,
... 'gender' : 'm',
... }
 for item in dictionary.items():
...     print(item)
... 
 for item in dictionary.keys():
...     print(item)
... 
name
age
gender
 for item in dictionary.values():
...     print(item)
... 
Eddie
29
m
 

 for item in dictionary.items():
...     key, value = item 
...     print(key, value)
... 
name Eddie
age 29
gender m
```



### range() function 

we get out of the box with python that produces a sequence of integers from start inclusive to stop exclusive 

you can give it like a default of zero to whatever you give it 

construct: 
for number in range(start,finish,stepover): 

start and stepovers are optional 

range creates a special type of object that we can iterate over 


```python
 for index in range(0,10):
...     print(index)
... 

```


###### another neat trick, if you do not use a variable just use _ 

```python

 for _ in range(0,10):
...     print(_)
... 
 for _ in range(10):
...     print(_)
... 
0
1
2
3
4
5
6
7
8
9
 

 for _ in range(10, 0, -1):
...     print(_)
... 
10
9
8
7
6
5
4
3
2
1

```


##### a new trick list_object = list(range(start,finish,stepover)) is the quickest way to build a list 

```python

 list_object = list(range(10))
 list_object
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 

```



### enumerate() 

enumerate() we wrap around something we can emuerate 
it takes an iterable object 

```python

 for item, char in enumerate("hello this is me"):
...     print(item, char)
... 
0 h
1 e
2 l
3 l
4 o
5  
6 t
7 h
8 i
9 s
10  
11 i
12 s
13  
14 m
15 e
 

```


### while loop 

a while loop is a little different, we say while a condition is happening. if you do not have saveguard, it will keep running forever. infinite loop is dangerous. you can use break keyword to break out the loop or use the condition to jump out of the loop  

```python 
while <condition>:
    <statement>
    <update_condition>
```


```python
 while counter < 10:
...     print(counter)
...     counter += 1
... 

 while counter < 10:
...     print(counter)
...     counter += 1
... else:
...     print(counter)
... 
1
2
3
4
5
6
7
8
9
10
 

```

##### you can also use a else statement 

```python 

while <condition>:
    <statement>
    <update_condition>
else: 
    <statement>
```

##### the most efficient way to ues while loop is 

```python 
while True:
    <input statement>
    <update_condition>
    if <condition>:
        break
```


### break, continue, pass 

1. break, we breaks out of the current loo right way 

```python 
while True:
     
    if <condition>:
        break

```

2. continue, we skip the current statement if condition is true, it continues on the top 

```python 
while True:
     
    if <condition>:
        continue
```

3. pass, pass does not do absolutely antyhing, it just essentially passes to the next line. pass is a good way to be a placehold!!! for example you want to loop through the for loop, but we do not know what we want to do yet. i will place it for now, it is not for production code  

while True:
     
    pass



#### what is good code 

1. not using unncesessarly ugly spaces, make things more readable, make compact code. make things predictable  

2. do not repeat yourself!!!!



### good exercise, find duplicate 

```python 
 for item in list_duplciate:...     if list_duplciate.count(item) > 1:
...             if item not in list_result:
...                     list_result.append(item)
...  list_result['a', 'b', 'c', 'd', 'e']

```



### functions 

we are not limited whatever python gives us 

def short for defition 

```python 
def function_name(parameters):
    < statement >

function_name(argument)
```

this statement is where we are taking actions for 

functions allows you to not repeat yourself, check this out 

```python
 def function_name(parameter):
...     print(parameter)
... 
 function_name(1)
1

```


### scopes 

scopes simply means what variables do we have access to 

scope in python has function scope or functional scope. 

the only time we create a scope is to use the indentation, that is the new universe we spawn, anything indented is not accessible






```python 
global_scope = value # this has the scope that everybody in the file has access to the variable 

def function_name():
    local_scope = value 
    # this has only scope inside the function 

if True:
    local_scope = value # this has only scope inside the if statement 


```




we never left the local scope to the global scope 

```python 
scope_variable = 1 # this has the scope that everybody in the file has access to the variable 

def function_name():
    scope_variable = 2
    print(scope_variable) 
    # this has only scope inside the function 

print(scope_variable)


 a = 1 
 def parent():
...     a = 10
...     def child():
...             return a
...     return child
... 
 print(parent())
<function parent.<locals>.child at 0x7f545401b280>
 print(parent)
<function parent at 0x7f54548ced30>
 print(parent()())
10
 print(a)
1
 

```



### docstring 
whta does allows us to do is actually comment inside of our functions in a way that if another programmer uses this function 



```python 
'''
info: this function does what
param: value1, value2, value3
return: result  
'''
def function_name():
    statements 
    return value

```

we can also yse the help function to find what a function does 

```python
help(function_name)

```
or we can use object.__doc__ later one 
these docstrings are useful to add commetns and definitions to your functions 



### clean code on functions 

we get the same exact result but look how much cleaner that is, I can come in and see it right away, that allows you develop 


example: 

```python
 def is_one(number):
...     if number == 1:
...             return True 
...     else:
...             return False 
... 
 is_one(1) 
True
 is_one(2) 
False
 def is_one(number):
...     return number == 1
... 
 is_one(1) 
True
 is_one(2) 
False
 

```




### parameters versus arguments 


these paramters allow us to give the function when we call it 

```python 
def function_name(parameter1, parameter2):
    < statement >
```

arguments are used as the actual values we provide to a function, it is to invoke or call the function 

```python 
function_name(argument1,argument2)
```

### default parameters and keyword arguments 


these are positional argument, they are required to be in proper position 


```python 
def function_name(parameter1, parameter2):
    < statement >


function_name(argument1,argument2)
```

keywords argument allows us to give keywords not worry about the position, it is confusing: 

```python 
def function_name(keyword1= parameter1, keyword2=parameter2):
    < statement >

```

function_name(argument1,argument2)


default parameters allows us to define function parameters with default value

```python 
def function_name(keyword1= "value", keyword2="value"):
    < statement >
```

function_name(argument1,argument2)

if you do not provide the value for parameters still have values even if it is called the wrong way 
so keyword arguments increaes the readability of your code because you know exactly how we are calling 

positional arguments are also nice and clean 

```python 
 def function_name(keyword1="parameter",keyword2="parameter2"):
...     print(keyword1)
...     print(keyword2)
... 
 function_name()
parameter
parameter2
 function_name(keyword="random thing")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: function_name() got an unexpected keyword argument 'keyword'
 function_name(keyword1="random thing")
random thing
parameter2
 function_name(keyword1="random thing",keyword2="hello")
random thing
hello

```



### return keyword 


functions alaways have to return something, if they do not reuturn something, it automatically returns None 

once we hit the point of return statement, we exit this function and return wahtever this expression gives us, 


```python 

def function_name(parameter1, parameter2):
    < statement >
    return expression

```


function returns does two things, it returns expression or return None

a good rule of thumb with function is this function should do one thing really well. the power of function return the result. 




```python
 def sum(parameter1, parameter2):
...     return parameter1 + parameter2
... 
 sum(10,20)
30

```


and what does this do? it is a nested function 



```python 

def function_name(parameter1, parameter2):
    def function_name(parameter1, parameter2):
        < statement >
        return expression

```


we are not getting the result as we want? because we did not return the inner function 


```python
 def function_name(parameter1, parameter2):
...     def another_function(pamameter1, parameter2):
...             return num1 + num2
... 
 outer_layer = function_name(10,20)
 print(outer_layer)
None
 print(outer_layer(10,20))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'NoneType' object is not callable
 

```



```python

 def function_name(parameter1, parameter2):
...     def another_function(pamameter1, parameter2):
...             return parameter1 + parameter2
...     return another_function... 
 outer_layer = function_name(10,20) print(outer_layer(10,20))30
 outer_layer = function_name(10,20) print(outer_layer(10,20))30
 outer_layer = function_name
 outer_layer(20,30)
<function function_name.<locals>.another_function at 0x7f8c17545e50>
 inner_layer = outer_layer(20,30)
 inner_layer
<function function_name.<locals>.another_function at 0x7f8c17545dc0>
 print(inner_layer)
<function function_name.<locals>.another_function at 0x7f8c17545dc0>
 print(inner_layer(10,20))
40
 
```

this does stretch your mind a little bit 


```python

 def function_name(parameter1, parameter2):
...     def another_function(pamameter1, parameter2):
...             return parameter1 + parameter2
...     return another_function... 
 outer_layer = function_name(10,20) print(outer_layer(10,20))30
 outer_layer = function_name
 outer_layer(20,30)
<function function_name.<locals>.another_function at 0x7f8c17545e50>
 inner_layer = outer_layer(20,30)
 inner_layer
<function function_name.<locals>.another_function at 0x7f8c17545dc0>
 print(inner_layer)
<function function_name.<locals>.another_function at 0x7f8c17545dc0>
 print(inner_layer(10,20))
40
 def outer_most_layer(outer_most_param1,outer_most_param2):
...     def middle_layer(middle_param1, middle_param2):
...             def inner_layer(inner_param1,inner_param2):
...                     return inner_param1 + inner_param2
...             return inner_layer
...     return middle_layer
... 
 outer_function = outer_most_layer(10,20)
 outer_function
<function outer_most_layer.<locals>.middle_layer at 0x7f8c15d328b0>
 outer_function(10,20)
<function outer_most_layer.<locals>.middle_layer.<locals>.inner_layer at 0x7f8c15d32940>
 outer_function(10,20)(10,20)
30

```

because return automatically exit the function, if you add another piece of code, it will never be executed



### *args and **kwargs 

*args and **kwargs 

wrong way of doing multiple arguments, there are many ways to go about this 

```python

# compliation error 
def function_name(args):
    return sum(args)

function_name(1,2,3,4,5,6,7)
 function_name(1,2,3,4,5,)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: function_name() takes 1 positional argument but 5 were given
```

###### *args is a tuple of arguments, *args can technically be anything, the standard is to make it args 

```python
def function_name(*whatever):
    <statements>

```

therefore, the right way of doing this: 

```python 
 def function_name(*args):
...     return sum(args)
... 
 function_name(1,2,3,4,5,)
15

```

##### **kwargs 
with kwargs stands for keywords arguments, I can add keywords. this saves as a dictionary 

 def function_name(*args,**kwargs):
...     print(kwargs)
...     print(args)
... 
 function_name(1,2,3,4,5,6, key1 = 'value1', key2 = 'value2')
{'key1': 'value1', 'key2': 'value2'}
(1, 2, 3, 4, 5, 6)
```python
def function_name(*whatever, **something):
    <statements>

function_name(argument1,argument2,argument3, keyword1=value1,keyword2=value2)

```


```python 
 def function_name(*args,**kwargs):
...     print(kwargs)
...     print(args)
... 
 function_name(1,2,3,4,5,6, key1 = 'value1', key2 = 'value2')
{'key1': 'value1', 'key2': 'value2'}
(1, 2, 3, 4, 5, 6)

 def function_name(*args, **kwargs):
...     print(args)
...     print(kwargs)
...     return sum(sum(args),sum(kwargs.values()))
... 
 function_name(1,2,3,4,5,keyword1=1,keyword2=2)
(1, 2, 3, 4, 5)
{'keyword1': 1, 'keyword2': 2}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in function_name
TypeError: 'int' object is not iterable
 def function_name(*args, **kwargs):
...     print(args)
...     print(kwargs)
...     result = 0
...     for item in kwargs.values():
...             result += item
...     return sum(sum(args),result)
... 
 function_name(1,2,3,4,5,keyword1=1,keyword2=2)
(1, 2, 3, 4, 5)
{'keyword1': 1, 'keyword2': 2}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 7, in function_name
TypeError: 'int' object is not iterable
 
 def function_name(*args, **kwargs):
...     result = 0
...     for item in kwargs.values():
...             result += item
...     return sum(args) + result
... 
 function_name(1,2,3,4,5,keyword1=1,keyword2=2)
18
```

##### Rules: params, *args, defualt paramters, **kwargs, usually you just use one of these 

```python 
def function_name(params, *args, defualt paramters, **kwargs):
    statements

```


### method and function 

glad you still hang in there, both functions and methods allow us to take actions on our data types, the difference is minimal 


the way we call functions are just invoke the function names 

```python 
def function_name(parameters):
    statement
    return value/expression

function_name(parameters)
```

methods has to be owned by something!!
they have built in methods inside the method 
```python
object.method() 

```


### walrus operator

##### walrus operator := python3.8 is evolving. := assigns values to variables part of a larger expression. it affectionately. not repeating our function invocation, it is a way for us to minimize doing calculations that are similar, let's say inside of an if statement or a while statement that based on a condition and do calculation, handful resources 


```python
 a = 'helloooo this is me'
 if((len(a)) > 0):
...     print(f"{len(a)} is too long")
... 
19 is too long
 if((n := len(a)) > 0):
...     print(f"{n} is too long")
... 
19 is too long

 function_name := sum(1,2)
  File "<stdin>", line 1
    function_name := sum(1,2)
                  ^
SyntaxError: invalid syntax
 (function_name := sum(1,2))
3
 (function_name := sum(1,2))
3
 print(f"{function_name}")
3

```


### global keyword 

```python 
global variable 
variable = value

```
or 

```python 
variable = value
def function_name():
    global variable += 1
    return variable 

```


without gloabl keyword 

```python

 total = 0 
 def count():
...     total += 1
...     return total 
... 
 print(count())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in count
UnboundLocalError: local variable 'total' referenced before assignment
 

```

the idea is instead accessing the variable outsides, it really gets complicated as files get bigger and bigger to do so 


with global keyword: 

```python 
 global total = 0 
  File "<stdin>", line 1
    global total = 0 
                 ^
SyntaxError: invalid syntax
 global total 
 total = 0
 def count():
...     return total 
... 
 print(count())
0



 variable = 100 
 def function_name():
...     global variable  
...     variable += 1
...     return variable
... 
 function_name() 
101
 
```

we should be able to detach the dependency or the effect of global variable. 

```python 

 total = 0
 def count(total):
...     total += 1
...     return total 
... 
 print(count(count(count(total))))
3
```



### nonlocal variable 

this is convoluted and confusing code 

the nonlocal keyword is used to refer to the inner part of nested functions 


```python
 def outer():
...     x = "local variable" 
...     def inner():
...             nonlocal x
...             x = "nonlocal variable"
...             print("inner:", x)
...     inner()
...     print("outer:",x)
... 
 outer() 
inner: nonlocal variable
outer: nonlocal variable
 



```

I will argue this makes your code more complicated than it should be, so there are special cases where you might want to use htis, but you can try to make your code predictable, but global and nonlocal are useful in some situations 




### summary of scope 

global variable would make all the headaches go away but machines do not have inifnite power, memory, nor CPUs, they all have limited resources 

as programmers, we have to be conscious of what resources we use because sometiems that can cost us money, sometimes that can crash our computers 

scope allows us to create one location in the memory , the computer and python interpreter specifically destroys all this memory 

the garbage collector will say we are done with this function, it collect that garbage and throw it out 

the program does not hog up a lot of memories 





## Reference
[x] How to become a Python 3 Developer and get hired! Build 12+ projects, learn Web Development, Machine Learning + more!