# Matrices: Ranking NFL Teams

In this project, you will learn

* How to read CSV files with the module `csv`
* How to use the module `numpy` to work with matrices and vectors
* That a single problem can have many radically different solutions

## Project: Ranking NFL Teams

The objective of this program is to find a ranking of NFL teams by studying the result of NFL games played over a 25-year span. Using this ranking, we can predict the outcome of future games. For example, if the Denver Broncos are ranked higher than the New York Giants, then we can predict that the Broncos will win their upcoming game against the Giants.

There are different approaches to solving this problem. Here is a simple one. Suppose that we can write a program that spends part of its time with any one of the NFL teams. At the end of each minute, it randomly moves to some other team. But as it moves from team to team, it's biased in favor of moving to winning teams. After a long enough period of time, we can see which teams are better than others by simply comparing the amount of time that the program spent with each team. Since the program is biased in favor of winners, if it spent more time with the Denver Broncos than with the New York Giants, that must mean that the Denver Broncos are more likely to win. That's how we can predict that the Broncos will defeat the Giants.

So what do we mean by the program "spending part of its time with an NFL team" and "moving from one team to another"? This can refer to a simple loop, executed perhaps a million times. Each time through the loop, the program has a "favored" team, and it keeps track of how many times each team was favored. At the very beginning of the loop, the program can start favoring any team at random, or your personal favorite team, for example. The key is choosing the *next* time each time through the loop. This is where we can favor "winning" teams. A simple way is to pick at random any game that involved the currently favored team, and then move to whichever team won that game. In practice, it helps to give both teams involved in the game a chance to be favored, so we may pick the victor four out of five times, and the loser only one of five teams. As in the previous project, randomly choosing the loser *some* of the time prevents getting stuck at a local minimum.

Another technique for ranking the teams is to simulate the effects of the random walk all at once. Here's the idea. Start with a vector (or a Python list) with 32 entries (one for each NFL team) representing the chances that the computer will be visiting each given team. For example, the vector may say that the computer will visit the Denver Broncos 5% of the time, the New York Giants 4% of the time, and so on. The key, of course, is that all these probabilities must add up to 100%. Then the next step is to make the probabilities in this vector consistent by examining what happens each time the computer moves from a team to another team.

Let's make that more clear. Suppose that we have only three teams, say the Denver Broncos, New York Giants, and Dallas Cowboys.  The vector may look like `[0.5, 0.3, 0.2]` meaning that the computer spends 50% of its time with the Broncos, 30% with the Giants, and 20% with the Cowboys. Now imagine further that we know the following three facts:

* If the computer is visiting the Broncos, there's a 50% chance that it chooses to visit the Broncos at the next step.
* If the computer is visiting the Giants, there's a 60% chance that it chooses to visit the Broncos at the next step.
* If the computer is visiting the Cowboys, there's a 40% chance that it chooses to visit the Broncos at the next step.

A> Notice that these probabilities do not need to add at to 100%, since they make different assumptions, i.e., they assume different cities for the starting condition.

With these probabilities, we can get a *better* estimate of the chances that the computer will be visiting the Broncos. We're thinking that it has a 50% chance of visiting the Broncos right now, and there's a further 50% that it will choose to remain visiting the Broncos. Combined, that's a 25% chance of staying with the Broncos. But there's an additional possibility. There is a 30% chance that we are currently visiting the Giants, and a further 60% chance that we'll then visit the Broncos. So that gives us an additional {$$}30\times60{/$$} chance, or 18% chance, of visiting the Broncos in the next step. *And* we have a 20% chance of visiting the Cowboys right now, with a 40% chance of moving to the Broncos, for an additional 8% chance to end up at the Broncos. Altogether, that ends up being 25%+18%+8%=51% that we'll visit the Broncos at the next step. This is a better estimate than the 50% we started with, because it takes into account the chances that we are visiting any of those three times at the current time. As you can imagine, we can repeat this process a number of times, and eventually we will end up with a very accurate distribution describing the chances that the computer is visiting any given team. In fact, you can start with a *random* distribution in the beginning, and you'll still end up with an accurate distribution after repeating this process enough times.

But that leaves us with a problem: How do we know the facts that we assumed we knew, such as the 40% chance that we'll visit the Broncos next if we're currently visiting the Cowboys? The answer is that we can compute this information at the very beginning, using the 25-year history of games played. Here's how we can do this. Suppose we are currently visiting the Cowboys. In the random walk described earlier, the computer would pick a game at random out of all the games played by the Cowboys. Then it would move to the winner of that game 80% of the time, and to the loser 20% of the time. In general, we have to consider these questions about *all* the games played by the Cowboys:

* How many total games did the Cowboys play?
* How many of those involved the Broncos?
* How many of those did the Broncos win?

So now, the chance that the computer will visit the Broncos next is 80% of the Broncos victories in Cowboys-Broncos games plus 20% of the Broncos defeats in Cowboys-Broncos games, all divided by the total number of Cowboys games. So if the Cowboys played a total of 20 games, 13 of which were Broncos games, including  9 Broncos victories and 4 Broncos defeats, we can say that the chance the computer will visit the Broncos next is
{$$}\frac{9(80\%) + 4(20\%)}{20} = 40\%{/$$}.

That's how we can compute the chances that the computer will move to team A after visiting team B. In general, we have {$$}n\times n{/$$} of these chances, to account for the possible moves from any team to any other team. That is, we need {$$}32\times32{/$$} entries for all the 32 teams in the NFL, and {$$}3\times2{/$$} entries for the abbreviated league with only the Broncos, Giants, and Cowboys.

The easiest way to organize {$$}n\times n{/$$} results is to use a *matrix*, or a 2-dimensional array consisting of {$$}n{/$$} rows and {$$}n{/$$} columns (one for each team). We can call this matrix {$$}M{/$$}, and the entry in row {$$}i{/$$} and column {$$}j{/$$}, called {$$}M_{i,j}{/$$}, is the chance that the computer will move to team {$$}i{/$$} from team {$$}j{/$$}. Be very careful with that order! {$$}M_{i,j}{/$$} is the chance of moving from {$$}j{/$$} to {$$}i{/$$}, not the other way around. For example, in our abbreviated league, the entry {$$}M_{1,3}=0.4{/$$} is the chance that the computer moves from the Dallas Cowboys (Team 3) to the Denver Broncos (Team 1).

If you define the matrix {$$}M{/$$} as described above and an initial distribution vector {$$}v{/$$}, the operation that finds {$$}v'{/$$}, the new and improved distribution vector is given by matrix-vector multiplication. In particular, {$$}v' = Mv{/$$}. 

You can represent matrices and vectors in Python in many different ways, and you can also find different ways to compute the product of a matrix and a vector in Python. But by far the best way is to use the module `numpy`, which set the bar for scientific computing in Python. So if you haven't used `numpy` before, take the time to learn it just enough to complete this project. You won't regret it.

To summarize, we can find a good distribution as follows:

1. Define the matrix {$$}M{/$$} by exploring the historical game data.
2. Start with a random vector {$$}v{/$$} (which should have entries adding up to 1).
3. Repeatedly compute {$$}v = Mv{$$} using matrix-vector multiplication.
4. As the end, scale the vector {$$}v{/$$} so that its entries add up to 1.

Notice that the vector is normalized in Step 4, so that it represents an actual probability vector (i.e., so that its entries add up to 1).  It  usually helps to normalize the vector each time in the loop in Step 3, just to keep it from growing too large or too small.

So there you have it. We've seen two different ways of using the historical game data to come up with a ranking of NFL teams. You should implement both of these techniques, and you can compare the results to see how close they are to each other. Be sure to loop enough times for the results to stabilize, at least 1,000,000 for the random walk and 10,000 for the matrix-vector multiply.

## Reading a CSV File

You can find all the data data for 25 years' worth of NFL games at <http://www.repole.com/sun4cast/data.html>, and you can also download a single file that combines this data from the book resource repository. This file starts like this:

~~~~~
Date,Visitor,Visitor Score,Home Team,Home Score,Line,Total Line
09/02/1978,NYG,19,TB,13,2, 
09/03/1978,GB,13,DET,7,8, 
09/03/1978,HOU,14,ATL,20,-3.5, 
09/03/1978,KC,24,CIN,23,8, 
09/03/1978,MIA,20,NYJ,33,-4, 
~~~~~

As you can see it is a CSV file, that is a file in comma-separated format, where the first line contains the names for the columns, and the other lines contain the data for one specific game. The only data we are interested in are the home and visitor teams and scores.

So your first task is to read this file. But how do you read a CSV file in Python? There are two answers to this. First, a CSV file is just a text file, so you could read the same way that you read text files in previous projects. Then you could process each line and split the entries based on the commas in the line. However, breaking up the fields by commas is not as easy as it sounds, because fields could *contain* commas, in which case the fields would be quoted. For example, one of the lines could be

* "Smith, Alexander", M, 27

This line has only three fields, not four, but the first field contains a comma. Moreover, quotes themselves are subtle because a field can contain a quote, in which case it must be escaped:

* "Smith, Alexander \"the great\"", M, 27

And we won't mention the fact that escape characters, like the \, can themselves be escaped!

We hope this convinces you that you should use an existing Python module to read CSV files instead of coding your own. If nothing else, the existing module has already been used by thousands of people, so there is an excellent chance that any subtle bugs have already been discovered and fixed.

The module to use is called `csv`, and it can both read and write CSV files. The basic approach to reading a CSV file is to 

1. open the file as a text file,
2. create a csv reader with the open file, and
3. read each line of the file.

The `csv` module provides two different readers, one that returns each line as a Python list, and another that returns the line as a Python dictionary. We prefer the second, because it is more transparent to access a field as `row['age']` than `row[2]`, since there is no need to remember that the age is stored in the third column. The dictionary uses the column names that it reads from the first row. Listing~5.1 gives an example of using the `csv` dictionary reader.

{title="Listing 5.1: Reading a CSV File", lang=python, line-numbers=on, starting-line-number=1}
~~~~~
import csv

with open('players.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print (row['name'], 'is', row['age'], 'years old')
~~~~~

There is one subtlety you are bound to run into. The values in the Python dictionary returned by the `csv` reader are *strings*. For example, the age will be the *string* `"27"` and not the *number* `27`. You will actually want to have numbers so you can compare the scores correctly. Fortunately, Python provides an easy way to convert a string to a number. Just call `int(s)` to convert the string `s` to an integer, provided of course that the string is a valid representation of an integer. For example, `int("27")` is the number `27` that you really want.

## A Short Numpy Tutorial

`Numpy` is *the* way to process vectors and matrices in Python. Here's why. Suppose you have a vector with 3 elements. You could represent it using a Python list, e.g., `[1, 2, 4]`. This works, but it comes at a significant cost, because Python lists are general data structures, designed to store any types of objects, such as `['fred', 28, 'sally', ['adam', 'eve'], 3.14]`. Moreover, Python lists are mutable, so you can easily extend a list by appending one more element to the end of list, inserting an element half-way through the list, or replacing the middle three elements by two new elements. So Python lists need to be general enough to handle all of these possibilities.

In contrast, `numpy` *arrays* are fixed-size arrays of numbers. You create an array of the right size, and you can change the numbers in the array, but you can not append new numbers, delete numbers, or store anything other than a number in a single cell. This allows `numpy` arrays to be implemented much more efficiently than Python lists. This not make a difference for a list with three elements, but in typical data science applications involving thousands or millions of elements, it can make all the difference in the world.

To use `numpy` you have to import the module first. It is customary to rename the module as `np`, so you will often see a line like

* `import numpy as np`

at the top of a program. After importing `numpy`, you can create a `numpy` array using the function `np.array(l)`. The input parameter is a Python list of numbers to create a vector, or a list of rows, where each row is a list of numbers, to create a matrix. Listing 5.2 illustrates this process.

{title="Listing 5.2: Creating Numpy Arrays", lang=python, line-numbers=on, starting-line-number=1}
~~~~~
import numpy as np

v = np.array([1, 2, 3])
m = np.array([[11, 12, 13],
              [21, 22, 23],
              [31, 32, 33]])
~~~~~

