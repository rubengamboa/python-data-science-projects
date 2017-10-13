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

So now, the chance that the computer will visit the Broncos next is 80% of the Broncos victories in Cowboys-Broncos games plus 20% of the Broncos defeats in Cowboys-Broncos games, all divided by the total number of Cowboys games. So if the Cowboys played a total of 20 games, 13 of which were Broncos games, including  9 Broncos victories and 4 Broncos defeats, we can say that the chance the computer will visit the Broncos next is {$$}\frac{9(80\%) + 4(20\%)}{20} = 40\%{/$$}.

That's how we can compute the chances that the computer will move to team A after visiting team B. In general, we have {$$}n\times n{/$$} of these chances, to account for the possible moves from any team to any other team. That is, we need {$$}32\times32{/$$} entries for all the 32 teams in the NFL, and {$$}3\times2{/$$} entries for the abbreviated league with only the Broncos, Giants, and Cowboys.


