# Simple Plots: How Many Primes between 1 and N?

In this project, you will learn

* How to define your own functions in Python
* How to use unit tests to make sure your code is working
* How design decisions can impact the performance of your code
* How to create basic line graphs using matplotlib

## Project: How Many Primes Are There between 1 and N?

In the last project, we wrote a program to discover how many primes there are between 1 and 100. In this project, we'll explore how the number of primes grows as we count them from 1 to 100, 1 to 1,000, 1 to 10,000, and so on.

To do this, we will start with refactoring the solution from the previous project so that it becomes a function that can be used to find the number of primes between 1 and N. Then we can use this function to count the primes in varying ranges (e.g., up to 100, 200, 300, and so on) and display them in a graph like the following.

![Figure 2.1: Number of Primes](images/number-of-primes.png)

Of course, instead of "Mystery Functions" you will plot some actual functions that you think may be similar to the number of primes. Part of doing data science is making such educated guesses, but here are some ideas to help you get started:

* {$$}\sqrt{N}{/$$},
* {$$}N^{0.9}{/$$},
* {$$}\ln{N}{/$$},
* {$$}N / \ln{N}{/$$}, or
* {$$}\sqrt{N} / \ln{N}{/$$}.

Remember, there are at most {$$}N/2{/$$} primes from 1 to N, so all candidate functions should be smaller than that.

## Defining Functions

Functions are absolutely fundamental in programming, because they are the main mechanism for

* writing a piece of program code that can be used in many different places, and
* reducing the complexity of a program by hiding implementation details.

In fact, we have been using functions for some time. In the previous project, we used the functions `range` which produces a list of numbers, and `len` which returns the length of a string. You can see that these functions embody the two points above. `range`, for example is an extremely useful function that is called in the definition of many `for` loops. Moreover, `len` returns the length of a list, but you can use it without knowing how it is actually implemented.

What we'll do now is to define our own functions. For example, in Listing 1.17, we wrote a program that finds the sum of the numbers up to 100. It may be more useful to define a function once that can be used many times to find the numb of numbers up to `N`. Notice that by changing the limit from 100 to `N`, we are making it more likely that we can reuse this function in many different contexts.

Functions are defined using the keyword `def` as follows:

{title="Listing 2.1: Function To Find Sum of First N Positive Integers", lang=python, line-numbers=on, starting-line-number=1}
~~~~~
def sum_up_to(N):
    sum = 0                 # sum - Sum of positive integers up to i
    for i in range(1, N+1): # i - current integer to add
        sum = sum + i
    return sum
~~~~~

Line 1 of Listing 2.1 is used to define the function. Notice that the `def` keyword is followed by the name of the function, `sum_up_to` in this case, followed by the names of the function's arguments, just `N` in this case. If there are more than one arguments, they should be separated by commas.

The actual definition of the function follows in Lines 2-5. Notice that this is almost identical to Listing 1.17, except that the number 100 has been replaced by the parameter `N`. The remaining new concept is in Line 5. Most functions return a value, just like mathematical functions such as sine or square root. Line 5 specifies that the value returned by the function `sum_up_to` is the value of the variable `sum`.

Once it is defined, you can use the function `sum_up_to` just like any of the built-in Python functions. For example, you can now compute the sum of the positive integers up to 100 as follows:

{title="Listing 2.2: Sum of First 100 Positive Integers", lang=python, line-numbers=on, starting-line-number=1}
~~~~~
sum100 = sum_up_to(N)     # sum100 - Sum of positive integers up to 100
~~~~~

Let's emphasize one of the benefits of using functions. The code in Listing 2.1 is relatively simple, but it is not the fastest way to compute the value of {$$}1 + 2 + \cdots + N{/$$}. A much faster way to compute this sum was discovered by the great mathematician Gauss, who found that {$$}1 + 2 + \cdots + N = \frac{N(N+1)}{2}{/$$}. Using Gauss's trick, we can define a more efficient version of `sum_up_to` as follows:

{title="Listing 2.3: Efficient Function To Find Sum of First N Positive Integers", lang=python, line-numbers=on, starting-line-number=1}
~~~~~
def sum_up_to(N):
    return N*(N+1)//2
~~~~~

You may have noticed, however, that I can't have told you the whole story. For example, the function `range` can be called as `range(10)` or `range(2,10)`, so how can we possibly have a different number of arguments for the same function? The answer is that you can specify default values for some arguments, in which case you are allowed to leave them out when you call the function. For example, consider the function defined as follows:

{title="Listing 2.4: Function To Find Sum of Positive Integers Between M and N", lang=python, line-numbers=on, starting-line-number=1}
~~~~~
def sum_pos_ints(M, N=-1):
    if N < 0:
        N = M
        M = 1
    return sum_up_to(N) - sum_up_to(M-1)
~~~~~

With this definition, we can ask for the value of `sum_pos_ints(10)` or `sum_pos_ints(10, 15)`. The first asks for the sum of all positive integers up to 10, and notice how the `if` statement in Line 2 detects that N was not specified (since it has the default value of -1) and rearranges the parameters accordingly. When both parameters are specified, as in `sum_pos_ints(10, 15)`, the `if` statements leaves the parameters as is. In either case, the `return` statement calculates the sum of the positive integers between `M` and `N`, whether they are specified explicitly or implicitly in the function call.

When a function has optional arguments, it can be confusing to determine what values in a function call correspond to what parameters. This can be a problem even without optional arguments, e.g., when a function has many parameters so it isn't clear what the values in a function call are supposed to be. That's why Python allows you to explicitly set parameters by giving them their name. For example, all of the following will return the same value:

* `sum_pos_ints(10, 15)`
* `sum_pos_ints(10, N=15)`
* `sum_pos_ints(M=10, N=15)`

Generally speaking, I prefer the third alternative in this case because it makes it painfully clear what the arguments mean. (It would be even better if the arguments had better names, like `n_start` and `n_end`.) In cases where the first argument is almost always relevant but the arguments with default values are rare, I may use either of the first two alternatives, though I favor the second.

Essentially, that is all there is to defining functions in Python, but there is one remaining concept that can be confusing. Variables in one function are completely separate from variables in other functions. So just because you defined the variable `sum` in the function `sum_up_to` does not mean that you can use `sum` in any other function. In a sense, this variable **belongs to** the function `sum_up_to`, so it doesn't exist outside of this function.

This is actually not as strange as it may appear at first. For example, consider the built-in function `len`. We don't know how it's implemented, but suppose it is done with a loop that counts each letter in its string argument. The number of letters may be stored in the variable `count` which is returned at the end of the function. That would be fine, unless you also have a variable called `count` in one of your functions, in which case the value of *your* variable `count` could change when you call `len`. Obviously, this would be totally unacceptable. If nothing else, how are you even supposed to know what variable names `len` uses? That's why Python treats variables in different functions as distinct, even if they have the same name.

Things are a little more complicated when you use a variable in a function *and* in the same file but outside of any function definitions, what's referred to as *global scope*. In that case, the variable in the function is the same as the one used in the file, although Python prevents you from *modifying* that variable in the function unless you explicitly mark the variable for updates. (See `global` if you're interested in doing that, but I recommend against writing code that changes global variables.) This is normally not a problem, because we generally avoid using code outside of function definitions.

## Documenting and Testing Functions

## Lists in Python

## Simple Line Graphs with Matplotlib
