# Python Basics

In this project, you will learn

* How to work with Python variables
* Different Python types, e.g., integers, Booleans, and strings
* Selection (if statements)
* Iteration (loops) and range
* Strings and string formatting

## Project: How Many Primes Are There between 1 and 100?

Prime numbers are beautiful and mysterious, and they also have many practical applications, such as cryptography. An interesting question is how many prime numbers there are, and we will explore this question in this chapter and the next.

A prime number is an integer greater than or equal to 2 that is divisible only by 1 and itself. For example, 5 is a prime number, because only 1 and 5 can divide it. However, 6 is not a prime number, because 2 divides 6 evenly.

There are 4 primes between 1 and 10, namely 2, 3, 5, and 7. In this project, you will find the prime numbers between 1 and 100 and report how many there are. For instance, if there are 42 primes in this range, your program may print the following:

> There are 42 primes from 1 to 100.

If you know enough Python to complete this project, that's great! Go ahead and write the code, then move on to the next project! If not, don't worry. Take a look at the remainder of this chapter to learn what you need to know to do this project, then come back and do it.

## Variables and Expressions

Programming involves identifying some relevant set of data and manipulating this data in order to achieve the intended results. For instance, if your program is intended to analyze the relationship between movies' critical score and their box-office revenue, then the relevant set of data involves (1) the critical score, and (2) the box-office revenue of each movie. You will see in a later project how you may manipulate this data to find the relationship (if any) between these facts.

In code, all data is stored in *variables*, which you can think of as a data point that has a name. For example, some of my favorite football player's stats may be stored in the variables `height`, `weight`, `arm_length`, `hand_size`, and `dash_40`. I chose those names carefully. Each is descriptive, so that you have a good chance to guess what data may be stored in the respective variable. I.e., you can probably guess that whatever is stored in the variable `height` is in fact the heigth of my favorite football player. I also followed the standard **naming conventions** when I chose those names. All of them are in lower case, and a single underscore separates multiple words, as in `arm_length`. Moreover, I had to make some sacrifices due the **naming rules** of Python. According to these rules, variables names may contain letters, digits, and underscores, and the name must start with either a letter or an underscore. That explains why I settled for `dash_40` instead of the more descriptive name `40_yard_dash`, which isn't a valid name.

The variables can be *assigned* values as follows:

{title="Variable Assignment", lang=python}
~~~~~
    height = 75
    weight = 246
    arm_length = 33.5
    hand_size = 9.25
    dash_40 = 4.42
~~~~~

The first line assigns the value 75 to the variable `height`, so when `height` is used further down in the program, its value will be 75.

These assignments all used constant values, like 75 or 33.5, on the right-hand side, but more generally we can use mathematical expressions, such as `2*height` or `weight/3`. Python supports all common mathematical expressions, including addition, subtraction, multiplication, division, exponentiation, and parentheses. For example, the Body Mass Index (BMI) is defined as a person's weight divided by the square of his or her height. To calculate my favorite player's BMI, you could use the following Python expression:

{title="Arithmetic Expression", lang=python, line-numbers=on, starting-line-number=6}
~~~~~
    bmi = (0.45 * weight) / (0.025 * height)**2
~~~~~

The example shows how `*` is used for multiplication and `**` for exponentiation. (The other arithmetic operators just use their familiar symbols from algebra, e.g., `+`.) Notice also that Python understands the conventional order of operations, so it squares the height before dividing.

This all makes sense. But wait a minute! Shouldn't that just be `weight / height**2`? The reason we need to multiply the weight by `0.45` and the height by `0.025` is that the equation for BMI uses the units of kilograms and centimeters, but the player's information is in pounds and inches, so these must be converted to kilograms and centimeters first. But how, you may ask, are you supposed to know that these values are in pounds and inches?

That is an excellent question. But before answering it, I want to emphasize that *the computer does not care*. Suppose `weight` is in inches and `height` is in pounds, but you execute the following in Python:

{title="Arithmetic Expression Fail", lang=python, line-numbers=on, starting-line-number=6}
~~~~~
    #leanpub-start-delete
    bmi = (0.45 * weight) / (0.025 * height)**2
    #leanpub-end-delete
    bmi = weight / height**2
~~~~~

If you do this, Python will not notice (or care) that the variables are in the wrong units. Instead, it will compute the BMI using the expression provided, so it will assign `0.437` to `bmi` instead of the "correct" value of `31.49`. That's quite a difference!

Just in case you still think this is a trivial problem, let me tell you about the Mars Polar Lander. The $110M lander was a robotic spacecraft that was part of the Mars Surveyor mission in 1998. It descended to the Martian surface, but communications stopped at the end of the descent. NASA engineers determined that the problem was an error during the ["transfer of information between the Mars Climate Orbiter spacecraft team in Colorado and the mission navigation team in California"](https://mars.nasa.gov/msp98/news/mco990930.html). You guessed it: One team used metric units and the other English units!

So if the computer doesn't care what units you're using, who does? Obviously, it's the programmers who care, so there must be some way to let another programmer (possibly your future self) what units your variables are using. More generally, it's important to let the other programmers (again, possibly your future self) exactly what each variable holds. Python offers a mechanism for just this programmer-to-programmer communication, and it's called a *comment*. Many beginning programmers underestimate the importance of comments, but experienced programmers know the value of proper commends and documentation. So you should get in the habit early to document your variables, so that other programmers find it easier to understand your program. I bet those NASA engineers (and the scientists who depended on that mission) wish they had done just that!

To write a comment in Python, simply write the comment after the character `#`. Python will ignore the remainder of the line (starting with the `#` and going all the way until the end of the line), but humans can read the comment and use it to understand the program. Here is a better way to write those variable assignments:

{title="Documented Variable Assignment", lang=python}
~~~~~
    height = 75         # Player's height in inches
    weight = 246        # Player's weight in pounds
    arm_length = 33.5   # Length of player's arm in inches
    hand_size = 9.25    # Size of player's hand in inches
    dash_40 = 4.42      # Player's 40-yard dash time in seconds
~~~~~

This illustrates an important *Rule of Style*:

>    *Rule of Style #1:* When you use a variable for the first time, **always** document exactly what the variable represents in your program.

This is important not only to communicate with other programmers, but also as a first step to avoid computing errors (colloquially known as "bugs".) Programmers are human and we make mistakes. I have seen even small programs where the same variable is used to mean different concepts in different parts of the program. In one place, for example, it may refer to the average temperature in Denver, while in another place it refers to the temperature in Denver during the AFC Championship Game. When a variable is used has two distinct meanings, the programmer can hardly be faulted for becoming confused, so the program is almost certainly wrong.

## Arithmetic and Logical Expressions

In the previous section, you learned about numbers in Python and arithmetic expressions, but there are a few things that we left out of the discussion. Now is the time to consider those issues.

First, you should know that Python includes two different types of numbers. There are integers, like `1` and `-63`, and real numbers like `3.125` and `1.0`. For historical reasons, real numbers are called floating-point numbers in computing.

You may have noticed something weird above. We have integers like `1` and floating-point numbers like `1.0`. Aren't those the same? Mathematically, they most certainly are, but in a computer they are represented very differently. For the most part, Python treats both types of numbers the same, but there are some important exceptions. We will see in later projects that there are some contexts where only integers are permitted. For example, you can ask for the third letter in the word "hello", but in this context you have to use `3` instead of `3.0` to refer to "third".

Things get more complicated when you consider arithmetic expressions. What exactly is `2+3`, as opposed to `2+3.0`? The answer is that most arithmetic expressions will return an integer value when operating on integers. So if you add, subtract, or multiply two integers, the result is an integer, but if you combine an integer and a floating-point number, the result will be floating-point.  The result of exponentiation is a little tricky.  If you raise an integer to zero or a positive power, the result is an integer.  But if you raise an integer to a negative power, the result is a floating-point number.

Another tricky operation is division.  If you divide two integers, the result is *always* a floating-point number. For example, `3/2` results in `1.5`, which is not too surprising. But keep in mind that `4/2` is `2.0`, not the **integer** `2`. The rule for division is different than for exponentiation, but it's the way Python does it.

Rarely, you will find cases where you want division to mean integer division, as in elementary school where `7 / 2` is "3 with remainder 1". Python uses two arithmetic operators to perform division in this way. The `//` operator returns the integer quotient, so that `7 // 2` is 3, for example. And the `%` operator returns the remainder, so that `7 % 2` is 1.

Python supports other types of objects besides numbers, such as logical values (i.e., true and false) and strings (words or phrases such as "hello" and "programming is fun"). Let's discuss logical values now and leave strings for a later section.

The main way to create a logical expression is to compare two values. Comparisons in Python are made with the comparison operators `<`, `<=`, `==`, '>', and `>=`. The result of a comparison is always a logical value, i.e., either `True` or `False`. For example, you are considered obese if your BMI is 30 or higher, and you can check for that with the Python expression `BMI >= 30`. This is a logical expression, so the value will be either `True` or `False`, depending on the value of BMI.

Logical values can be combined using *logical operators*. Logical operators are also called *Boolean operators* after George Boole, the English mathematician who wrote *The Laws of Thought* in which he explored logical values and operators.

There are three logical operators, `and`, `or`, and `not`. The meaning of `and` and `not` are straightforward. `x and y` is true only when both `x` and `y` are true, just as in ordinary language. Similarly, `not x` is true precisely when `x` is false, and `not x` is false when `x` is true. Again, this follows the ordinary meaning of "not" in English. But you must be careful with `or`. `x or y` is true precisely when `x` is true, `y` is true, or both `x` and `y` are true. In ordinary English, the word "or" usually implies a choice, so that "x or y" is usually taken to mean that "x" may be true or "y" may be true, but certainly not both. In computing (and in logic), the logical operator `or` is more inclusive, in that it does not force us to choose which one of "x" or "y" is true.

We can use logical expressions in Python, in just the same way we use arithmetic expressions. For example, we can use logical expressions to assign values to these new expressions:

{title="Logical Expressions", lang=python, line-numbers=on, starting-line-number=7}
~~~~~
    obese = bmi >= 30           # True if player is considered obese
    overweight = bmi >= 25 and bmi < 30
                                # True if player is considered overweight
    underweight = bmi < 18.5    # True if player is considered underweight
    healthy = not (obese or overweight or underweight)
                                # True if player's weight is in normal range
~~~~~

In the next sections, we will see the most common way that logical expressions are used in Python.

## Selection

Up to this point, we've been using a very simple mental model of the way in which computers execute statements. Our programs have consisted of many statements, and the computer executes these statements in order, one immediately after the other. Naturally enough, this is called *sequencing* because the computer steps through each statement in a sequence.

Sequencing is great, but sometimes you will need to specify a different path through the statements in your program. *Selection* allows your program to execute different statements depending on a condition. If you're thinking that by "condition" we mean a logical expression, you're absolutely right. This is where logical expressions come into their own.

To illustrate selection, suppose we have two variables `a` and `b`, and we wish to compute the **rounded** value of `a` divided by `b`. Suppose `a` is 13 and `b` is 5. As we saw previously, `a/b` is `2.6` and `a//b` is `2`, but the value we want is `3`, which is `2.6` rounded up since the fractional part of `2.6` is at least `.5`.

Here's a way we could do that. Start with the quotient without remainder of `a` divided by `b`, which is `a // b` in Python. Then consider the fractional part of `a` divided by `b`. If the fractional part is at least `0.5`, then the answer is one more than the quotient; otherwise, the answer is just the quotient. Notice how this last step requires selection.

We can implement this strategy in Python as follows:

{title="Integer Division with Rounding", lang=python, line-numbers=on, starting-line-number=1}
~~~~~
    rq = a // b        # Quotient of a and b rounded to nearest integer
    if (a%b) / b >= 0.5:
        rq = rq + 1
~~~~~

While this code works correctly, there is something unsettling about it. If you haven't seen it before, you may be worried about line 3, `rq = rq + 1`. But actually, this is not a problem. It is just like any other assignment statement. First, the value on the right-hand side of the `=` is executed, namely `rq + 1`. This uses the original value of `rq`, which was assigned in Line 1. Then this value is assigned to `rq`, so it simply gets a new value (one more than its old value). If you find this unsettling, it's only because you recall from algebra that the equation {$$}x = x+1{/$$} does not have any solutions. But recall that the `=` symbol in Python means assignment, whereas  the symbol for equality comparison is `==`. Indeed, `rq == rq + 1` is always `False`, but the assignment statement `rq = rq + 1` is perfectly reasonable.

What is unsettling about this code is that the variable `rq` does not have a simple explanation. In fact, the comment on Line 1 is at best misleading; really, it's just plain wrong. It says that `rq` holds the quotient of `a` and `b` rounded to the nearest integer, but if `a` is 13 and `b` is 5, `rq` will be have the value `2` immediately after Line 1, which is wrong according to the description of the variable. Sure, Lines 2 and 3 "fix" the problem, but that only shows that the variable `rq` has a different meaning in Lines 1 and 3. This is the road to incomprehensible code. Just don't go there.

Even though the Python syntax allows you to assign to a variable multiple times, and even though you will find plenty of examples on the internet that do just that, I think this is a potentially serious mistake. So I urge you to adhere to the following *Rule of Style*:

>    *Rule of Style #2:* A variable should only be assigned once, though it may be used multiple times.

If you think about it, you will probably agree that this rule is simply a corollary of the first rule of style. After all, if a variable is assigned multiple times, how can its description possibly be right in **all assignments**?

This is how you can compute the integer division with rounding while obeying both rules of style:

{title="Improved Integer Division with Rounding", lang=python, line-numbers=on, starting-line-number=1}
~~~~~
    # rq - Quotient of a and b rounded to nearest integer
    if (a%b) / b >= 0.5:
        rq = a // b + 1
    else:
        rq = a // b
~~~~~

This example actually shows two things. First, I moved the comment that explains the variable `rq` above the `if` statement, simply because there are two places that initially assign `rq`. In fact, I do this often for "important" variables, and what makes a variable "important" or not just depends on the particular program. If you're worried that this is a violation of the second rule of style, don't be. It's just fine, because the `if` statement guarantees that only one of these assignment statements is executed.

The second new thing in this example is the extended version of the `if` statement. In the first example, the `if` was followed by a simple assignment statement, which was executed only when the condition `(a%b) / b >= 0.5` in the `if` was `True`. But in the new example, the `if` also has an associated `else`, so when the condition in the `if` is `False`, the statement(s) after the `else` are executed. Again, the `if` guarantees that either the statements immediately after the `if` or the statements immediately after the `else` are executed.

There is an even more extended version of the `if` statement, which is useful to differentiate between more than two possible cases.  For instance, recall the example where the Body Mass Index was examined to determine if a player was obese, overweight, etc. In total, there were four possible cases, so let's suppose that we want to define a single variable called `bmi_outcome` to store this classification. E.g., the variable should have the value 0 for underweight players, 1 for normal weight, 2 for overweight, and 3 for obese. This variable can be set in Python as follows:

{title="Selection with More Than Two Cases", lang=python, line-numbers=on, starting-line-number=1}
~~~~~
# bmi_outcome - 0 for underweight, 1 for normal, 2 for overweight, 3 for obese
if bmi >= 30:
    bmi_outcome = 3
elif bmi >= 25:
    bmi_outcome = 2
elif bmi >= 18.5:
    bmi_outcome = 1
else:
    bmi_outcome = 0
~~~~~

Notice that if `bmi` is 35, the first condition is true, so none of the other conditions is even tested. In particular, since the first condition is true, the variable `bmi_outcome` is set to `3`. Even though the second condition is also true (i.e, `bmi >= 25`), the value of `bmi_outcome` will **not** be set to `2`, since the relevant condition is not even tested. In reality, what the `elif` statements do is add the negation of the previous conditions, so the code above is equivalent to the following:

{title="Explicit Selection with More Than Two Cases", lang=python, line-numbers=on, starting-line-number=1}
~~~~~
# bmi_outcome - 0 for underweight, 1 for normal, 2 for overweight, 3 for obese
if bmi >= 30:
    bmi_outcome = 3
elif not (bmi >= 30) and bmi >= 25:
    bmi_outcome = 2
elif not (bmi >= 30 or bmi >= 25) and bmi >= 18.5:
    bmi_outcome = 1
else:
    bmi_outcome = 0
~~~~~

Of course, nobody would write the `elif` statements in this way, but it's important that you understand why the previous two examples are completely equivalent.

## Iteration

Iteration is the third of the main strategies that a computer can use to decide which statement to execute next in a program, what's called the *control flow* of the program. We started with *sequencing* where the control simply flows from one instruction to the next instruction in the program. In the last section, we discussed *selection*, in which the computer decides which instruction will be the next based on the value of a logical expression. Now we will discuss *iteration*, in which the computer can execute one or more instructions repeatedly.

The programming language feature that supports iteration is called a *loop*, and Python has a couple of different versions of loops.  The simplest is a `for` loop, which executes a statement a specific number of times. For example, the following loop executes the assignment statement precisely 10 times:

{title="Simple For Loop", lang=python, line-numbers=on, starting-line-number=1}
~~~~~
for i in range(10):
    x = i
~~~~~

The loop introduces the variable `i`, which is often called the *index variable* of the loop. Naturally, you can use any legal variable name instead of `i`, though it is common to use the names `i`, `j`, and `k` for index variables. The expression `range(10)` describes the sequence of numbers 0, 1, 2, ..., 9. The way the `for` loop works is that the index variable `i` takes on each of the values in the expression `range(10)` (which is to say, 0, 1, 2, ..., 9), and then it executes the statements inside the loop (called the *body* of the loop) for each of the possible values of the index variable. In other words, the body of the loop, which is this case is just the assignment statement `x = i` is executed ten times, first with `i` equal to 0, then with `i` equal to 1, and so on, until the tenth time when `i` is equal to 9. After the loop is complete, control will follow the sequencing rule, which is to say that the computer will execute whatever statement immediately follows the loop.

Quick question: What is the value of `x` after the loop? It was assigned 0 the first time through the loop, but then it was assigned 1 the second time through the loop, and so on.  At the very end, it is assigned the value of 9, so this is the value that the variable `x` has when the loop is finished.

Iteration is extremely important in programming, because we often have to compute a solution incrementally. For example, suppose we wish to find the sum of the first five positive integers. We can do so with the following statement:

{title="Sum of First 5 Integers", lang=python, line-numbers=on, starting-line-number=1}
~~~~~
sum5 = 1 + 2 + 3 + 4 + 5
~~~~~

That works, but what about the sum of the first 100 integers? I certainly wouldn't want to write that expression, and even if I did, I would probably make an error somewhere, e.g., writing 633 instead of 63. But it is easy to find this value with a loop:

{title="Sum of First 100 Positive Integers", lang=python, line-numbers=on, starting-line-number=1}
~~~~~
sum100 = 0              # sum100 - Sum of positive integers up to i
for i in range(100):    # i - current integer to add
    sum100 = sum100 + i
~~~~~

Wait a minute! This violates *Rule of Style #2*. The variable `sum100` is assigned multiple times, in lines 1 and 3.

It turns out that *Rule of Style #2* is very useful, but we must modify slightly when it comes to loops. What is important is the following:

1. Each variable is assigned only once in any given block of statements, e.g., only once before the loop, and only once inside the loop (if at all).
2. If a variable is assigned inside the loop, it is only to update its value so that it conforms to its description, as specified according to *Rule of Style #1*.

The next paragraph goes here.


## Strings (and Formatting)
