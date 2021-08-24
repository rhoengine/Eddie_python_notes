# python_crash_note


## Preface 

software is at core of so many of the tools we use today: nearly everyone uses social networks to communicate, and most office jobs involve ineracting with a computer to get work done. As a result, the demand for people who can code has skyrocketed. Countless tutorials and bootcamps promise to turn ambitious beginners into engineers. 


python is an intepreted high-level general-purpose verstatile and powerful programming language. Python's design philosophy emphasizes code readability with its notable use of significant identation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for large-scale projects 


python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured particuarly procedural, object-oriented and functional programming. Python is often described as batteries included language due to its comprehensive standard library 


## Disclaimer

with every occurrence of name, you are resgistering the names only in an editorial fashion and to the benefit of owner, with no intention of infrigement of the trademark. The information in this repo is distributed on an as is basis. While every precaution has been taken in the preparation of this writing, neither the author nor reader shall have any liability to any entity with respect tto any loss or damage caused or alleged to be caused directly or indirectly by the information contained in it. Nevertheless, it is inevitable that some mistakes have crept in. If you do spot a mistake, I'd really appreciate it if you let me know so I can make amends and deploy a new versions. There is an excitment that we are turning the corner. 

This note is made for people to write throwaway code, so there is no much time spent on style and elegance. Sophisticated programming concepts -  list comprenehsion, generators, and oop - are covered because of the complexity they add. Veteran programmers point out ways the code could be changed to improve effficiency 

This note is designed for software programmers who need to learn python from scratch.





This tutorial will get you caught up to speed with the basics so thta you feel comfortable programming 

we will have a fully professional developer environment, we then get into some advanced python, your head might hurt by the end of the seciton, but trust me, it is going to be fun, we will talk about how we apply our newfound language to common use cases for something useful. I am biased, this will all going to fit in together and make sense from the very beginning to make sure that you all succeed with this. We are going to make you a fully fledged developer , before we dive into this, we need to be able to just have fun. 

On the right side, we have just ridden our very first python program, very exciting. First of all, if you are confused why my thing is dark and yours might be light. For us, it runs this piece of code, gives this source code may not apply to intepreter and runs it right here on our right side. 







## What is programming 

Program is a set of instructions that we give to translator 
computers speak 1s or 0s, human have developed programming languages in lower and higher level. We have these pieces, get your mind blown
the translator is a interpreter or a compiler goes line by line through our machine 

translator interprets line by line and compilers translate all lines of a program to a file usually called a binary and execute the whole file. the interpreter takes our python code CPYTHON VMand runs on the virtual machine. Thins we are gonna go over in detail  


## Python Intepreter 
most languages have similar or foundational principles. we download them and here we download python from distinct foundation, so bear with me: 
https://www.python.org/


## Python3 

it has layer because they have to work out some kinks, make sure it is integerated properly onto their site. These version will constantly upgrade 

it is unavoidable that the programming language is always evolving

I want you to be aware of the historical context and one thing to be careful of when 

python is slower than C# or even Java. Python is good at developer productivity. Every programming language excels at some things, it is all about tradeoffs 

python ZTM sheets: https://github.com/aneagoie/ztm-python-cheat-sheet


### Prequisite: 
You should have a basic understanding of computer. and follow the following link to get your python: https://realpython.com/installing-python/ 


```shell

python3 
Python 3.8.5 (default, May 27 2021, 13:30:53) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 

```

1. ues terminal to run python3 
2. text editor does not have syntax auto completiong, but they are lightweight: sublime 
3. IDEs are full fledged, it has code snnipet

##### there is no right way, not right tool that is better than all the rest!!!! just customzie the things to your likings


### terminal commands 
1. ls 
2. pwd 
3. cd directory 
4. cd / 
5. cd ~   user directory 
6. mkdir directory_name 
7. touch <file_name>
8. mv origin_file target_file 
9. rm file_name 
10. rm -r folder_name 



### Learning 
1. terms and defintions
2. language data types, different ways to represent data
3. actions, store and retrieve this data and perform actions 
4. best pratices and solid structure 



## Table of Content 

Our immense collection of linguistic information thta has gathered attention as a valuable resource for tasks below: 


### Fundamentals 

[Part1 Python Data types and Data Structure](Python_Refresher_Basics1.md)


[Part2 Python Control Flow, Conditionals, Loops, Functions ](Python_Refresher_Basics2.md)

### Advanced 

[Part3 Python Object Oriented Programming](Python_Refresher_Advanced1.md)


[Part4 Python Functional Programming](Python_Refresher_Advanced2.md)


[Part5 Python Decorator and Generator](Python_Refresher_Advanced3.md)


### PEP 8 

index of python enhancement proposal PEPs tells us the clean python code look like 

the code editor, run the command pallette 



# Chapter 0 Introduction

## Preface 

My motivation for writing this tutorial comes from a gap I saw in today's literature for my bro who interested in learning to prorgamming. The current crop of programming materials fell into two categories. First, a dumbed-down language to making programming easy. Or second, they taught programming like a mathematics textbool: all different principles and concepts with little application given to the reader. 

The goal of this python fundamental tutorial is to bring you up to speed with Python as quickly as possible so you can build programs that work - games, data visualization and web application - while developing a foundation in porgram that will serve you will for the rest of your life . I am super passinate about covering topics around Python and software development in general.  The python community has been a constant source of professional inspiration ever since. We go beyond simple fact-checking and review the tutorial with the goal of helping beginning programmers develop a solid understanding of the language and programming in general. That said, any inaccuracies that remain are completely my own. 


I am sure your head is spinning from all the new concepts you need to ingest, and the influx of info can feel overwhelming at times while you are looking into dive into this tutorial. You will be kept the breathe and briefed with this issue while moving the ball forward. I emphasize real-world programming techniques, which are illustrated through useful examples. No matter what your ultimate goals maybe, you will soon be finding endless ways to improve through programs that you create.  You should be ready to move on to more advanced techniques, and your next language will be even easier to grasp. 

**It seems stupidly obvious and socially unrest , but if you have a problem typing, you will unabimously have a problem learning to code. Especially if you have a problem typing the fairly odd characters in source. Without this simple skill you will be unable to learn even the most basic things about how software works. 
Typing the code samples and getting them to run will help you learn the names of the symbols, get familiar with typing them, and get you reading the language.**

*let me push it back, you MUST type each code, manually. You have to be loyal to this approach!!!! If you copy and paste them, you might as well jsut not even do them as I oppose to this extensive comment on only reading. It is to train your hands, your brain, and you mind in how to read, and see. You must shed your light on it!!!!*




## What is programming 
Programmers furiously typing cryptic stream of 1s abd 0s on glowing screen, but modern porgramming is not mysterious 

*Porgamming* is simply the act of entring instructiosn for the computer to perform. 

A computer *program* is just a bunch of instructions/ building blocks run by a computer, just like a storybook is just a whole bunch of sentences read by the reader. These instructiosn, called the *source code*, are like the turn by turn instructions you might get for walking into a house.  These instructiosn might crunch some numbers. modify text, look up info in files, or communicate with other computers over the internet. You can combine these building blocks to implement more intricate decisions. 

The defintion of *a python program* at its most basic is a sequence of python statements that have been crafted to do something.  So neither of us are talking to python, instead we are communicating with each other through python. 

In order to tell a comptuer what you want it to do, you write a program in a language that the computer understands. They are purposely simple so we can focus on learning to program 


## Why programming? 

writing programs or porgramming is a very creative and rewarding activity. You can write programs for many reason, ranging from making your living to solving a difficult data analysis problem to having fun to helping someone else to solve a program. W are surronded in our daily lives with computer ranging from laptops to cellphones. Put forward with these infrasctures that would invest in modernzing it and put people back to work in IT professional. Professional programming can be a very rewarding job both financially and personally. Each competing for your attention and interest. W try our best to meet our needs and give a great user experience in the process. For now, our primary motivation is not to make money or please end users, but instead for us to be more productive in handling the data and information taht we will encounter in our lives for reconciliation to address root causes. 

Programmin, you have all the raw materials you need in your computer. you do not need to buy an yadditional canvas, paint, film, yarn, bricks, or electronic computers. 


## Computer Hardware Archiecture 

the high-ldevel defition of these parts are as follows as we tune in: 
* The Central Pocess Unit or CPU is the part of the compuer that is built to be obssessed with instructoirs. You are going to have learn how to talk fast keep up with the CPU, it warrants your support and different interactions 


* The Main Memory is used to store information that the CPU needs in a hurry. THe main memory is nearly as fast as the CPU. But the information stored in the main memory vanishes when the computer is turned off as it does not have the readoff 


* the second memory is also used to store informatin, but it is much slower than the main memory. The advantage of the secondary memory is that it can store information even when there is no power to the computer. Examples of secondary memory are disks or flash memory typically fround in USB sticks and portable. 

* The input and Output Device are simply our screen, keybaord, mouse and microphone, speaker, touchpad. They are all of the weays we interact wit hthe computer. 

* A network connection to retrieve information over a network. That is our objective and priorities. 

there are some low-level conceptual patterns that we use to construct programs. 

* input: get data from the outside world. come from the user typing data on the keyboard, rading data from a file, or even some kind of sensor like a microphone or GPS 

* output: display the result of the program on a screen or store them in a file 





## What is Python? 

Simply put, Python is a programming language, it was initally developed by Guido Van Rossum in the Netherland. Python continues to be actively involved in guiding the development and evolution of the language. 



* Python is a general-purpose programming language. It is not intended for use in any particular domain or environment, but instead can be fruitfully used for a wide vareity of tasks. Python represents a philosophy of writing code. Principles of clarity and readability are part of what it means to write correct of pythonic code. It is not always clear what pythonic means in all circumstances, and sometimes there may be no single correct way to write something. But the fact that the community is concerned about issues like simplicity, readability, and explictness means that python code tends to be more beautiful than inflamtory. Python principes are embodies in the zen of python, a hard and fast set of rules ,but rather a set of guidelness or touchstones to keep in mind when coding. 





* Python is simple to use, but it is a real programming language, offering much more structure and support for large programs than shell script or batch files can offer. The synax of python is desitned to be clear, readable, and expressive. Unlike many popular languages, Python uses whitespace to delimit code blocks, and in the process does away with reams of unnecessary parentheses while enforcing a universal layout. This means that all python code looks alike in important ways. At the same time, Python's expressive syntax means that you can get a lot of meaning into a single line of code. This expressive, highly-readable code means that Python maintenance i relatively easy. Eventually you find that would like to automate a tedious taks, shell scripts are best at moving around files and changing text data, not well-suited for GUI applications or games. 


* Python allows you to split your program int omodules that can be reused in other programs. It comes with a large collection of standard modules that you can as the basis of your porgrams. Some of these modules provide things like file I/O, system calls, sockets, and even interfaces to graphical user interface toolkits 


* Python is extensible, once you are hooked, you can link the interpreter into an app and use it as an extension, it is easy to add a new built-in funciton or module to the interpreter, either to perform crticial operations at maxiums speed. The mechanics of using the interpreter are explained. This is rather mundate info, but essential for trying out the examples shown. 

* Python's intellectual property, plays a strong roles in prompting the language, and in som cases funds its development.  Python is open-source freeware , meaning you can download it for free and use it for any purpose. It also has a great support community that has built a number of additional free tools. One of the pioneering programming of the modern computing era. Having a well-connected and supportive community is critical in helping your solve problems.  


* Python is an interpreted language. This is a bit of misstatement, technically, because Python is normally complied into a form of byte code before it is executed. However, this compilation happens invisibly, and the experience of using python is normally one of immediately executing code with a noticeable compilation phase. This lack of an interruption between editing and running is one of the great joys of working with Python. 


* On a technical level, python is a strongly typed language. This means that every object in the language has a definite type, and there is generally no way to circumvent that type. At the same time, Python is dynamically typed, meaning that there is no type-checking of your code prior to running it. This is in contrast to statically typed languages like Java or C++ where a compiler does a lot of type-checking for you, rejecting programs which misuse object. Ultimately, the best description of the Python type system is that it uses duck typing where an object's suitability for a context is only determined at runtime 

* sidnote: python 2 and python3, every programming language evolves as new ideas and technologie emerge, the developers of python have continually made the language medalist more versatile and powerful. Most changes are incremental and hardly noticeable. But the sonner you upgrade to using Python 3 the better! It looks like scratch-off ticket, the ceasefire continues to be held, these versions represent changes in some key elements of the language, and code written for one will not generally work for the other unless you take special precautions, creed and incentives. But Python3 address some known shortcomings in the older version. Python3 is the definite future of python, and you should bring in it if at all possible. Most of the fundamentals of the two version are the same, most of what you know transfers cleanly to the other, pretty payless. 

so you will be working with the most recent version of python: https://www.python.org/downloads/. 

* many programming lanagues are at the center of a cultural movement. THey have their own commmuties, values, pratices, and philosophy, and Python is no exception. The development of Python language itself is managed through a series of documents called Python Enhancement Proposal, or PEP, explains how you should format your code, and we should follow its guidelines 


## Installing Python -- Big Picture 

Python differs slight on different operating systems, so you will need to keep a few considerations in mind. 

1 from the official website of the python programming language http://www.python.org

2 download link to go the download page, be sure to install python3. 

3 starting python 
in windows: choosing Start -> CMD -> type in "python3" 
in Mac OS: open terminal type in "python3"

```python3 

Eddies-MacBook-Pro-2:python_note eddiehuang$ python3 
Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello World")
Hello World
>>> 


``` 

this has helped you get started with the python software by showing you installing and starting the python software

Please refer to the Appendix if you need detailed Text Editor and Setup instructions. Keep shining, we will root for you. 


## Characters of Good Programmers 

In a sense, you primarily need two skills to be a programmer for an apparent purpose: 

1. First, you need to know the language - the vocabulary and the grammar even prior to any other things on the groud. You will need to be able to spell the words in this new language properly and how how to construct well-fromed sentences. It is hard to keep up with and it is busted up. 
2. Second, you combine words and sentences to convey an idea to the read to converse with python. There is an art in constructing the story is imprved by doing some writing and getting some feedbacks. Be patient as the simple samples remind you of when you started it and seeking supplimentary  support and response assumbly as possible. 



The apparent purpose of python is to make your a good program in general and a good python programmer in particular. You will learn efficiently and adpot good habits as I provide you with a solid fundation in general concept: 

1. Attention to detail. it is what separates the good from the bad in any profession, you will not miss key elements of what you create 

2. Spot difference -- that most programmers develop over time -- is the ability to visually notice difference between things. An experience programmer can take two pieces of code that are slightly different and immediately start pointing out the difference. 


3. Practice and persistence. Playing guitar, you play scales, chords, and arpeggios for hours, and learn music thoery, ear training, and songs. Maybe you were told that you are gifted so you never attempt anything that might make you so seem stupid or not a prodigy. Maybe you are competitive and unfairly compare yoruself to someone. You will struggle with words, and no know what symbols are, and it will confusing. Keep at it and force yourself! To me repetitive pracice is natural and just how to learn something. 

4. Empty before you fill. We fall in love with making visual programs and spending every day studying it in mushc the same way. The consession and balls are over the course of your hand. 

5. Do not worry about bothering experienced programmers. every porgrammer has been stuck at some point, and most programmers are happy to help you set up your system correctly. You should be closely engaged with this publicly and keep support this effort certainly. And you need elevate this to rebuild the trust and move this across the finish line. More importantly, you will have the fundation you need to go out and discover all the more advanced topics in the language.  




6. Last but not least, I advocate finding things and check on the internet  fundamentally, a major part of this tutorial is learning to reasearch programming topics online, and your job is to use a search engine to find the answer.  The reason we have you search instead of just giving you the answer is because I want you to be an **Independent** learner who does not need this when you are done with it and levarage the resources. If you run into a despicable act demanded transparent investigations and diplomacy in touch with partners bilaterally please see your proposal as well as markup to address it or open ladders for your. To prosecute it and speaking out about it. If you can find the answers to your questions online, then you are one step closer to no needing it, that is the goal: 
1 go to http://google.com 2 type python xxxx     3 read the website listed to find the best answers 4 https://docs.python.org/3/tutorial/

see appendix E for searching online, try asking people in a web forum such as Stach Overflow or learn programming subreddit. Be sure to read the FAQ section have about the proper way to post questions. 

Explain what you are trying to do, not just what you did. 
* This lets your helper know if you are on the wrong track 
* Specify the point at which the error happens. 
* Copy and paste the entire error message 
* If the error came up after you made a change to your code, explain exactly what you changed. 
* say whether you are able to reproduce the error every time you run the program or whether it happens only after you preform certain actions. Explain what those actions are, if so.
always follow good etitquette as well. Do not post your questions in all caps or make unreasonable demands of the people tryin to help you 



## the Zen of Python 
the approach was acceptable while working on your own project, but eventually people realized that the emphasis on flexibility made it difficult to maintain large projects over long period of time. it was difficult, tedious, and time consuming to review code and try to figure out what someone else was thinkiing when they wre solving a complex problem 


python programmers embrace the notion that code can be beauttiful and elegant. 
If you have a choice between a simple and a complex solution, and both work, use the simple solution. Your code will be easiser to maintain, and it will be easiser for otheres to build on that code later on. 

Real life is messy, sometimes a simple solution to a problem is unttainable. in that case, use the simplest solution that works 


you can spend the rest of your life learning all the intricacies of python and of programming in general, but then you would never compelte any porject. Do not try to write perfect code; write code that works, and then decide whether to improve your code for that project or move ontop something else. 


As you continue to start digging into more involved topics, try to keep this philosophy of simplicity and clarity in mind. Experinced prorgamemres will respect your code more and will be happy to give you feedback and collaborate with you on interesting projects.




[Let's Dive into the Basics of the Basics, the big focus for us to kick this off and put forward -- Chapter1](Chapter1.md)


# Appendix A: Installing a text editor 
use a text editor will let you run almost all of your program directly and transparently from the editor instead of through a terminal, uses syntax highlighting to color your code, and runs your code in a terminal session embedded in the window to make easy to see the ouput: https://www.techradar.com/best/best-text-editors




##  Appendix B: Python Setup (Optional)

### macOS
Do the following tasks to complete this exercise:
1. Go to https://www.python.org/downloads/release/python-360/ and
download the “macOS 64-bit/32-bit installer”. Install it like you would any
other software.
2. Go to https://atom.io/ with your browser, get the Atom text editor, and
install it. If Atom does not suite you, then see Alternative Text Editors at the
end of this exercise.
3. Put Atom (your text editor) in your dock, so you can reach it easily.
4. Find your Terminal program. Search for it. You will find it.
5. Put your Terminal in your dock as well.
6. Run your Terminal program. It won’t look like much.
7. In your Terminal program, run python3.6. You run things in Terminal by
just typing the name and hitting RETURN.
8. Type quit(), Enter, and get out of python3.6.
9. You should be back at a prompt similar to what you had before you typed
python. If not, find out why.
10. Learn how to make a directory in the Terminal.
11. Learn how to change into a directory in the Terminal.
12. Use your editor to create a file in this directory. You will make the file,
“Save” or “Save As...,” and pick this directory.
13. Go back to Terminal using just the keyboard to switch windows.
14. Back in Terminal, list the directory with ls to see your newly created file.

### Windows

1. Go to https://atom.io with your browser, get the Atom text editor, and 
install it. You do not need to be the administrator to do this.
2. Make sure you can get to Atom easily by putting it on your desktop and/or
in Quick Launch. Both options are available during setup.
(a) If you cannot run Atom because your computer is not fast enough, then see
Alternative Text Editors at the end of this exercise.
3. Run PowerShell from the Start menu. Search for it, and you can just press
Enter to run it.
4. Make a shortcut to it on your desktop and/or Quick Launch for your
convenience.
5. Run your PowerShell program (which I will call Terminal later). It won’t
look like much.
6. Download Python 3.6 from
https://www.python.org/downloads/release/python-360/ and install it. Be sure
to check the box that says to add Python 3.6 to your path.
7. In your PowerShell (Terminal) program, run python. You run things in
Terminal by just typing the name and pressing Enter.
(a) If you type python and it does not run, then you have to reinstall Python
and make sure you check the box for “Add python to the PATH.” It’s very
small so look carefully.
8. Type quit(), and press Enter to exit python.
9. You should be back at a prompt similar to what you had before you typed
python. If not, find out why.
10. Learn how to make a directory in the PowerShell (Terminal).
11. Learn how to change into a directory in the PowerShell (Terminal).
12. Use your editor to create a file in this directory. Make the file, Save or
Save As..., and pick this directory.
13. Go back to PowerShell (Terminal) using just the keyboard to switch
windows. Look it up if you can’t figure it out.
14. Back in PowerShell (Terminal), list the directory to see your newly
created file.
From now on, when I say “Terminal” or “shell” I mean PowerShell, and
that’s what you should use. When I run python3.6 you can just type python.


##  Appendix C running python programs from a terminal 

most of the programs you write in your text edtiro you will run directly from the dtiro, but sotmimes it's useful to run program from a terminal instead. 

### on Linux and MAC OS X
the termianl command cd, for change directory, is used to navgite through your file system in a temrianl session. The command ls, for
list, shows you all the nonhidden files that exist in the current directory.

```shell
cd folder_name_which_contains_python_file
python3 python_file_name.py

```


### on Windows 
the termimal command, cd for change directory, is used to navigate through your file system in a command window. The command dir, for direcotry, shows you all the files that exist in the currect directory. 
```shell
cd folder_name_which_contains_python_file
python3 python_file_name.py

```



## Appendix D: Python Interpreter (Optional)

the python interpreter is usually installed as /usr/local/bin/python on those machines where it is available
put python3 to the shell 


the interpreter's line-editing features include interactive editing, history substition and cde completion. when called with standard input connected to a tty device, it reads and executes command interactively; when called with a file name argument or with a file as standard input, it reads and executes a script from that file 

the second way of starting the interpreter is python -c command, which executes the statements in command, analohous to the shell's -c ooption 


when known to the intepreter, the script name and additional arguments thereafter are turned into a lsit of strings and assigned to the argv variables in the sys module. you can access this list by executing import sys. the length of the list is at least one 
optiosn found after -c command or -m module are not consumed by the intepreter's option processing but left with sys.argv for the command or module to handle 


```python
import sys

print(sys.argv[1])
```

```shell
Eddies-MacBook-Pro-2:python_note eddiehuang$ python3  python1.py "hello"
hello
```

when commands are read from a tty, the interpreter is said to be in interactive mode. in this mode it promtps for the next command with the primary prompt usually three greater than signs >>> for continuation lines it promtps with the secodnary prompt, by default three dots ..... 
continuation lines are needed when entering a multiline construct 


```shell

Eddies-MacBook-Pro-2:python_note eddiehuang$ python3 
Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 

```


by default, python source files are treated as encoded in UTF-8. in that encoding, characters of most languages can be used simultaneously in string literals, identifiers and comments - although the standard library only uses ASCII characters for identifiers, a covnention that any portable code should follow.







## Appendix E: Python Debugging(Optional)
solving programmng problems on your own is easier than you might think. If you are not convinced, then let us cause an error on purpose 


```python 
>>> 12 + "2"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 


```

the traceback part of the error message into your favoirate search engine, and you should see tons of links explaining what the error messsage means and what causes it 
the trackback python displays when an error occurs contains a lot of information, but it can be overwhelming. The most useful parts are usually:
* what kind of error it was, and 
* where it occured 


syntax errors are usually easy to find, but there are a few gotchas. Whitespace errors can be tricky when spaces and tabs are invisible and we are used to ignoring them 

in general, error messages indicate where the problem was discovered, but the actual error might be earlier in the code, sometimes on a previous line 

in general, error messages tell you where the problem was discovered, but that is often not where it was caused 




as you start writing bigger programs, you might find yourself spending more time debugging. More code means more chances to make an error and more places for bugs to hide

one way to cut your debugging time is debugging by bisection. 

instead, try to break the problem in half. look at the middle of the program, or near it, for an intermediate value you can check. add a print statement or something else that has a verifable effect and run the program 


if the midpoint check is incorrect, the problem must be in the first half of the program. if its is correct, the problem is in the second half

every time when you perform a check like this, you halve the number of lines you have to search 

in pratice it is not always clear what the middle of the program is and not always possible to check it. it does not make sense to count lines and find the exact mindpoint. instead, think about places in the program where there might be errors and places where it is easy to put a check. then choose a post where you think the chances are about the same that the bug is before or after the check 








## Reference 
1. [x] Eric. Matthes : Python Crash Course - a hands-on, project-based introduction to programming 
2. [x] AI Sweigart: Invent Your Own Computer Games with Python 
3. [x] Learn Python The Hard Way 3rd Edition 
4. [x]  https://docs.python.org/3/tutorial/
5. [x] Python for everybody Exploring data using python3  
6. [x] How to become a Python 3 Developer and get hired! Build 12+ projects, learn Web Development, Machine Learning + more!