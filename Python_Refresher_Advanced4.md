
# error and debugging

## Error handling 

an error that crashes our program is called exception, python raises exceptions whenever interpreters say something is wrong 
error handling allows us to let python script continue running even if there are errors 


1 syntax error 

you can always set a reference to read them 

```python

>>> print('1)
  File "<stdin>", line 1
    print('1)
            ^
SyntaxError: EOL while scanning string literal
>>> print('1 + 1')
1 + 1
>>> print(1 + 'hello')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> print(1 + True)
2
>>> print(1 + False)
1

```


if we try to convert str to int

```python 
>>> age = int(input("what is your age?"))what is your age?
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: ''
>>> age = int(input("what is your age?"))what is your age?12
>>> print(age)
12

```


we can use the try keyword makes sure that we try the piece of code 


anything inside the try block, I am able to handle coming from the area except, if anything airs out, I am able to say something 


```python

try:
    statement

except: 
    statement 

```


```python




while True:
    try:
        age = int(input("please enter the age of yours:"))
        print(age)
        break
    except:
        print("this is not acceptable, please enter the oynumeric value:")

```


I am wrapping all my eorrs here in a try block, if anything happens. it catches it in here with the except block 


ideally I want to break out of this True statement, 

I can ues a else that works with try except block

```python




while True:
    try:
        age = int(input("please enter the age of yours:"))
        print(age)
        
    except:
        print("this is not acceptable, please enter the oynumeric value:")
    else:
        print("successfully done, thank you and that is a wrap")
        break

```

a buggy program, how do we handle different errors. one where it is a value error and another one is obviously a divided by 0 error 



```python



while True:
    try:
        age = int(input("please enter the age of yours:"))
        10 / age # please enter 0 
        
    except:
        print("this is not acceptable, please enter the oynumeric value:")
    else:
        print("successfully done, thank you and that is a wrap")
        break

```


1 except ValueError 

2 except ZeroDivisionError

```python




while True:
    try:
        age = int(input("please enter the age of yours:"))
        10 / age # please enter 0 
        
    except ValueError:
        print("this is a ValueError, please enter the oynumeric value:")
    except ZeroDivisionError:
        print("this is an zero division error, pleaes do the numbers without 0")
    else:
        print("successfully done, thank you and that is a wrap")
        break

```




if we were simply to do something 


```python

def sum(num1,num2):
    try:
        return num1 + num2
    except:
        print("I do not know what is wrong, it has to be descriptive ")
        print("please enter numbers")


print(sum(1,"2"))

```

we need to know what type of error: 



```python
def sum(num1,num2):
    try:
        return num1 + num2
    except TypeError as err:
        print("the error is " + err)

print(sum(1,"2"))

```


you cann add in here the way we have 

```python
def sum(num1,num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f"the error is {err}")

print(sum(1,"2"))

```

it is very useful when you want to get meaningful errors to your users 




we cam wrap multiple errors in except statement 

```python 
def sum(num1,num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError):
        print(f"opps")

print(sum(1,0))

```

it is useful to combine errors, 

```python
def sum(num1,num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(f"{err}")

print(sum(1,0))

```


#### finally runs at the end, after everything has been executed, 


try: 
except: 
else:
finally: 


```python


while True:
    try:
        age = int(input("I need a non zero numeric number:"))
        10 / age 
    except ValueError:
            print("please enter a number")
    except ZeroDivisionError:
            print("non zero")
    else:
            print("conditions met, good, bye")
            break
    finally:
            print("I will execute no matter it is a pass or fail")

```


sometimes errors and exceptions can be severe that we do want to stop our programs from running 




#### raies , it is rare you have to do this, there are some specific use cases, but here you just write a message. this is useful when you are creating your own library or tool and you want to let the user know what happened 


```python


while True:
    try:
        age = int(input("I need a non zero numeric number:"))
        10 / age 
        raise ValueError("hey cut it out")
    # except ValueError:
    #         print("this is a value error,please enter a number")
    except ZeroDivisionError:
            print("non zero")
    else:
            print("conditions met, good, bye")
            break
    finally:
            print("I will execute no matter it is a pass or fail")

```




they key thing to remember is that errors are unavoidable in programming, you should anticipate and handle it properly 

errors are bound to happen 


## how to debug code 

nobody writes perfect programs, we constantly improve our code as we find more and more mistakes becaues programs are full of errors 


you see the act of finding and removing these bugs or errors from our code is called debugging 


1 you use liniting, alloiwing us to detect errors in our code 

2 ide / editors specifically python, auto formatting to detect code highlighting

3 try to read errors. there is about 15 to 20 errors that are really common that show up 90% of the time 
you tend to remember 




### pdb is the builtin debugger, it allows us to interact with the code. although print is a quick way to debug code, pdb gives us an extra boost 


```python 
## print version 




def add (num1, num2):
        print(num1 + num2)
        return num1 + num2

add(4,"hello")


```


### we say pdb.set_trace() that is the most important feature of this output 

```python
### pdb version 

import pdb

def add (num1, num2):
        pdb.set_trace()
        return num1 + num2

add(4,"hello")

```

it now gives us an interactive python debugger that I can now type commands in here and actually test on my code 

I can test out what is going on 


```python
te/python_crash_note$ python3 hello.py 
> /home/edhuang/Desktop/note/python_crash_note/python_crash_note/hello.py(6)add()
-> return num1 + num2
(Pdb) num1
4
(Pdb) num2
'hello'
(Pdb) help

Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt      
alias  clear      disable  ignore    longlist  r        source   until    
args   commands   display  interact  n         restart  step     up       
b      condition  down     j         next      return   tbreak   w        
break  cont       enable   jump      p         retval   u        whatis   
bt     continue   exit     l         pp        run      unalias  where    

Miscellaneous help topics:
==========================
exec  pdb

```
I have a ton here like a list 

I can get a list 

```python 


(Pdb) list 
  1  
  2     import pdb
  3  
  4     def add (num1, num2):
  5             pdb.set_trace()
  6  ->         return num1 + num2
  7  
  8     add(4,"hello")
[EOF]
(Pdb) help list 
l(ist) [first [,last] | .]

        List source code for the current file.  Without arguments,
        list 11 lines around the current line or continue the previous
        listing.  With . as argument, list 11 lines around the current
        line.  With one argument, list 11 lines starting at that line.
        With two arguments, list the given range; if the second
        argument is less than the first, it is a count.

        The current line in the current frame is indicated by "->".
        If an exception is being debugged, the line where the
        exception was originally raised or propagated is indicated by
        ">>", if it differs from the current line.
(Pdb) 


(Pdb) step 
TypeError: unsupported operand type(s) for +: 'int' and 'str'
> /home/edhuang/Desktop/note/python_crash_note/python_crash_note/hello.py(6)add()
-> return num1 + num2
(Pdb) 

(Pdb) continue 
Traceback (most recent call last):
  File "hello.py", line 8, in <module>
    add(4,"hello")
  File "hello.py", line 6, in add
    return num1 + num2
TypeError: unsupported operand type(s) for +: 'int' and 'str'

```


### content 

1 step shows all the steps 
2 continue to continue the steps 
3 list shows all the statements
4 a shows all the arguments 
5 w shows me the context of the current line it is executing 
6 next shows the next statement 
7 variable_name = value, I am also able to change variables here 



```python
(Pdb) w
  /home/edhuang/Desktop/note/python_crash_note/python_crash_note/hello.py(8)<module>()
-> add(4,"hello")

```

they can step over and experiment with different comands using help and list to see what is going on 




## testing 
in the real world, you start getting millions of lines of code as the complexity and side of the code increases. harder and harder to tame and debug 

testing is a method in software development where individual units of source code such as function to be tested as you progress your career 

test is another python file 

usually you have a test file that never runs in production. we run to make sure thta before we release this main file to production 



testing is a higher level up 


```python 
import unitest

```
very descriptive, the way unittest works we want to test the function we want to test 


the way it works is we inherit the way that unnitest works and now we have that functionality available in our test main class 

```python 


## test.py 
import unittest 
import main 

class TestMain(unittest.TestCase):
    def test_some_function(self):
        variable = value
        result = main.function_name(variable_parameter)
        self.assertEqual(result,another_result)


```

this main.function_name line is the key part 


the way we run unittest is unittest.main()


```python
import unittest 
import hello 


class TestClass(unittest.TestCase):
    def testcase1(self):
        result = hello.test_function(10)
        self.assertEqual(result,15)
    def testcase2(self):
        result = hello.test_function(20)
        self.assertEqual(result,25)




unittest.main()

```


if I had type errors, i would add try except,we can return or raise an error such as ValueError 


```python

import unittest 
import hello 


class TestClass(unittest.TestCase):
    def testcase1(self):
        result = hello.test_function(10)
        self.assertEqual(result,15)
    def testcase2(self):
        result = hello.test_function("hello")
        self.assertEqual(result,25)




unittest.main()

def test_function(number):
        try:
                return int(number) + 5
        except ValueError as err:
                return err


```


now it is actually in assert error, there is a bit mismatch, because we are returning an error, it is an instance of value error 


```python
import unittest 
import hello 


class TestClass(unittest.TestCase):
    def testcase1(self):
        result = hello.test_function(10)
        self.assertEqual(result,15)
    def testcase2(self):
        result = hello.test_function("hello")
        self.assertTrue(isinstance(result,ValueError))




unittest.main()

```
can I trick this function and do the function 

```python 
import unittest 
import hello 


class TestClass(unittest.TestCase):
    def testcase1(self):
        result = hello.test_function(10)
        self.assertEqual(result,15)
    def testcase2(self):
        result = hello.test_function("hello")
        self.assertTrue(isinstance(result,ValueError))
    def testcase3(self):
        result = hello.test_function("world")
        self.assertIsInstance(result, ValueError)



unittest.main()

```


you really want to have tests that are easy to read when it comes to testing, readability is really important 
we started realizing how our function was too simplistic that if we reaceived a wrong input, as soon as we did that, it is more doable. 

unittest.main() has nothing to do with other function names 


there are individual files that should only be run hen we run our tests 


```python 

if __name__ == '__main__':
    unittest.main()

```




a few more neat things you can do with unittest 



### we can do python3 -m unittest -v which is called verbose we get more information, I can add docstring 

-m can run all tests under one directory 


```python 

edhuang@BB4287382437:~/Desktop/note/python_crash_note/python_crash_note$ python3 -m unittest...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
edhuang@BB4287382437:~/Desktop/note/python_crash_note/python_crash_note$ python3 -m unittest -v
testcase1 (test.TestClass) ... ok
testcase2 (test.TestClass) ... ok
testcase3 (test.TestClass) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK

```

```python 
$ python3 test.py  -vtestcase1 (__main__.TestClass) ... ok
testcase2 (__main__.TestClass) ... ok
testcase3 (__main__.TestClass) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK

```

another neat thing is setUp() which runs before all the test executes 

```python 

class TestClass(unittest.TestCase):
    def setUp(self):
        print("anything before that")


```

another thing is the tearDown()

as the name suggests, we run it at the end of each method that we call so in here 

```python 

class TestClass(unittest.TestCase):
    
    def tearDown(self):
        print("byte")

```

tearDown() we would not use that much, we usually use it to close a database 

at the end of the day, tests are logical testimonials to prove small things can go wrong in the code 


I hope you understand the principles of software development is testing 


