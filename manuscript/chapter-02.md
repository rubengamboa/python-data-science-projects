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

* {$$}\sqrt{N}{/$$}
* {$$}N^{0.9}{/$$}
* {$$}\ln{N}{/$$}
* {$$}N / \ln{N}{$$}
* {$$}\sqrt{N} / \ln{N}{/$$}

Remember, there are at most {$$}N/2{/$$} primes from 1 to N, so all candidate functions should be smaller than that.
