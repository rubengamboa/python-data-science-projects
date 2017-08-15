# Python Basics

In this project, you will learn

* How to work with Python variables
* Different Python types, e.g., integers, Booleans, and strings
* Conditionals (if statements)
* Loops and range
* Formatting strings

## Project: How Many Primes Are There between 1 and 100?

Prime numbers are beautiful and mysterious, and they also have many practical applications, such as cryptography. An interesting question is how many prime numbers there are, and we will explore this question in this chapter and the next.

A prime number is an integer greater than or equal to 2 that is divisible only by 1 and itself. For example, 5 is a prime number, because only 1 and 5 can divide it. However, 6 is not a prime number, because 2 divides 6 evenly.

There are 4 primes between 1 and 10, namely 2, 3, 5, and 7. In this project, you will find the prime numbers between 1 and 100 and report how many there are. For instance, if there are 42 primes in this range, your program may print the following:

> There are 42 primes from 1 to 100.

If you know enough Python to complete this project, that's great! Go ahead and write the code, then move on to the next project! If not, don't worry. Take a look at the remainder of this chapter to learn what you need to know to do this project, then come back and do it.

## Variables and Expressions

Programming involves identifying some relevant set of data and manipulating
this data in order to achieve the intended results. For instance, if your
program is intended to analyze the relationship between movies' critical
score and their box-office revenue, then the relevant set of data involves
(1) the critical score, and (2) the box-office revenue of each movie. You
will see in a later project how you may manipulate this data to find the
relationship (if any) between these facts.

In code, all data is stored in *variables*, which you can think of as
a data point that has a name. For example, some of my favorite football 
player's stats may be stored in the variables `height`, `weight`, 
`arm_length`, `hand_size`, and `dash_40`. I chose those names carefully. 
Each is descriptive, so that you have a good chance to guess what data
may be stored in the respective variable. I.e., you can probably guess
that whatever is stored in the variable `height` is in fact the heigth
of my favorite football player. I also followed the standard **naming
conventions** when I chose those names.  All of them are in lower case,
and a single underscore separates multiple words, as in `arm_length`.
Moreover, I had to make some sacrifices due the **naming rules** of
Python. According to these rules, variables names may contain letters,
digits, and underscores, and the name must start with either a letter
or an underscore. That explains why I settled for `dash_40` instead of
the more descriptive name `40_yard_dash`, which isn't a valid name.

The variables can be *assigned* values as follows:

{title="Variable Assignment", lang=python}
~~~~~
    height = 75
    weight = 246
    arm_length = 33.5
    hand_size = 9.25
    dash_40 = 4.42
~~~~~

The first line assigns the value 75 to the variable `height`, so when
`height` is used further down in the program, its value will be 75.

These assignments all used constant values, like 75 or 33.5, on the 
right-hand side, but more generally we can use mathematical expressions,
such as `2*height` or `weight/3`. Python supports all common mathematical
expressions, including addition, subtraction, multiplication, division,
exponentiation, and parentheses. For example, the Body Mass Index (BMI)
is defined as a person's weight divided by the square of his or her
height. To calculate my favorite player's BMI, you could use the following 
Python expression:

{title="Arithmetic Expression", lang=python, line-numbers=on, starting-line-number=6}
~~~~~
    bmi = (0.45 * weight) / (0.025 * height)**2
~~~~~

The example shows how `*` is used for multiplication and `**` for 
exponentiation. (The other arithmetic operators just use their familiar
symbols from algebra, e.g., `+`.) Notice also that Python understands
the conventional order of operations, so it squares the height before
dividing.

This all makes sense. But wait a minute! Shouldn't that just be 
`weight / height**2`? The reason we need to multiply the weight by
`0.45` and the height by `0.025` is that the equation for BMI uses
the units of kilograms and centimeters, but the player's information
is in pounds and inches, so these must be converted to kilograms and
centimeters first. But how, you may ask, are you supposed to know that
these values are in pounds and inches?

That is an excellent question. But before answering it, I want to
emphasize that *the computer does not care*. Suppose `weight` is in 
inches and `height` is in pounds, but you execute the following in
Python:

{title="Arithmetic Expression Fail", lang=python, line-numbers=on, starting-line-number=6}
~~~~~
    #leanpub-start-delete
    bmi = (0.45 * weight) / (0.025 * height)**2
    #leanpub-end-delete
    bmi = weight / height**2
~~~~~

If you do this, Python will not notice (or care) that the variables
are in the wrong units. Instead, it will compute the BMI using the
expression provided, so it will assign `0.437` to `bmi` instead of the
"correct" value of `31.49`. That's quite a difference!

Just in case you still think this is a trivial problem, let me tell
you about the Mars Polar Lander. The $110M lander was a robotic spacecraft 
that was part of the Mars Surveyor mission in 1998. It descended to
the Martian surface, but communications stopped at the end of the
descent. 
[NASA engineers determined](https://mars.nasa.gov/msp98/news/mco990930.html) 
that the problem was an error during the "transfer of information 
between the Mars Climate Orbiter spacecraft team in Colorado and the 
mission navigation team in California." You guessed it: One team used metric units and the other English units!

So if the computer doesn't care what units you're using, who does?
Obviously, it's the programmers who care, so there must be some way
to let another programmer (possibly your future self) what units your variables
are using. More generally, it's important to let the other programmers
(again, possibly your future self) exactly what each variable holds.
Python offers a mechanism for just this programmer-to-programmer
communication, and it's called a *comment*. Many beginning programmers
underestimate the importance of comments, but experienced programmers
know the value of proper commends and documentation. So you should get
in the habit early to document your variables, so that other programmers
find it easier to understand your program. I bet those NASA engineers
(and the scientists who depended on that mission) wish they had done 
just that!

To write a comment in Python, simply write the comment after the character 
`#`. Python will ignore the remainder of the line (starting with the
`#` and going all the way until the end of the line), but humans can read
the comment and use it to understand the program. Here is a better way to
write those variable assignments:

{title="Documented Variable Assignment", lang=python}
~~~~~
    height = 75         # Player's height in inches
    weight = 246        # Player's weight in pounds
    arm_length = 33.5   # Length of player's arm in inches
    hand_size = 9.25    # Size of player's hand in inches
    dash_40 = 4.42      # Player's 40-yard dash time in seconds
~~~~~

This illustrates an important *Rule of Style*.

    When you use a variable for the first time, **always** document
    exactly what the variable represents in your program.

This is important not only to communicate with other programmers,
but also as a first step to avoid computing errors (colloquially
known as "bugs".) Programmers are human and we make mistakes.  I
have seen even small programs where the same variable is used to
mean different concepts in different parts of the program. In one
place, for example, it may refer to the average temperature in
Denver, while in another place it refers to the temperature in Denver
during the AFC Championship Game. When a variable is used has two
distinct meanings, the programmer can hardly be faulted for becoming
confused, so the program is almost certainly wrong.

## Arithmetic and Logical Expressions

In the previous section, you learned about numbers in Python and
arithmetic expressions, but there are a few things that we left out
of the discussion. Now is the time to consider those issues.

First, you should know that Python includes two different types of
numbers. There are integers, like `1` and `-63`, and real numbers
like `3.125` and `1.0`. For historical reasons, real numbers are 
called floating-point numbers in computing.

You may have noticed something weird above. We have integers like
`1` and floating-point numbers like `1.0`. Aren't those the same?
Mathematically, they most certainly are, but in a computer they
are represented very differently. For the most part, Python treats
both types of numbers the same, but there are some important exceptions.
We will see in later projects that there are some contexts where only
integers are permitted. For example, you can ask for the third letter
in the word "hello", but in this context you have to use `3` instead
of `3.0` to refer to "third".

Things get more complicated when you consider arithmetic expressions.
What exactly is `2+3`, as opposed to `2+3.0`? The answer is that most
arithmetic expressions will return an integer value when operating on
integers. So if you add, subtract, or multiply two integers, the result 
is an integer, but if you combine an integer and a floating-point number,
the result will be floating-point.  The result of exponentiation is a 
little tricky.  If you raise an integer to zero or a positive power, the 
result is an integer.  But if you raise an integer to a negative power, the result is a floating-point number.

Another tricky operation is division.  If you divide two integers,
the result is *always* a floating-point number. For example, `3/2` results 
in `1.5`, which is not too surprising. But keep in mind that `4/2` is `2.0`,
not the **integer** `2`. The rule for division is different than for 
exponentiation, but it's the way Python does it.

Rarely, you will find cases where you want division to mean integer division,
as in elementary school where `7 / 2` is "3 with remainder 1". Python
uses two arithmetic operators to perform division in this way. The `//`
operator returns the integer quotient, so that `7 // 2` is 3, for example.
And the `%` operator returns the remainder, so that `7 % 2` is 1.

Python supports other types of objects besides numbers, such as logical
values (i.e., true and false) and strings (words or phrases such as
"hello" and "programming is fun"). Let's discuss logical values now and
leave strings for a later section.

The main way to create a logical expression is to compare two values.
Comparisons in Python are made with the comparison operators `<`, `<=`,
`==`, '>', and `>=`. The result of a comparison is always a logical
value, i.e., either `True` or `False`. For example, you are considered
obese if your BMI is 30 or higher, and you can check for that with the
Python expression `BMI >= 30`. This is a logical expression, so the value
will be either `True` or `False`, depending on the value of BMI.

Logical values can be combined using *logical operators*. Logical
operators are also called *Boolean operators* after George Boole,
the English mathematician who wrote *The Laws of Thought* in which
he explored logical values and operators.

There are three logical operators, `and`, `or`, and `not`. The meaning
of `and` and `not` are straightforward. `x and y` is true only when
both `x` and `y` are true, just as in ordinary language. Similarly,
`not x` is true precisely when `x` is false, and `not x` is false
when `x` is true. Again, this follows the ordinary meaning of "not"
in English. But you must be careful with `or`. `x or y` is true
precisely when `x` is true, `y` is true, or both `x` and `y` are
true. In ordinary English, the word "or" usually implies a choice,
so that "x or y" is usually taken to mean that "x" may be true or
"y" may be true, but certainly not both. In computing (and in logic),
the logical operator `or` is more inclusive, in that it does not
force us to choose which one of "x" or "y" is true.

We can use logical expressions in Python, in just the same way we
use arithmetic expressions. For example, we can use logical expressions
to assign values to these new expressions:

{title="Logical Expressions", lang=python, line-numbers=on, starting-line-number=7}
~~~~~
    obese = bmi >= 30           # True if player is considered obese
    overweight = bmi >= 25 and bmi < 30
                                # True if player is considered overweight
    underweight = bmi < 18.5    # True if player is considered underweight
    healthy = not (obese or overweight or underweight)
                                # True if player's weight is in normal range
~~~~~

In the next sections, we will see the most common way that logical
expressions are used in Python.

## Conditionals



## Loops

## Strings (and Formatting)
