# NGrams: Frequency of Letter Pairs

In this project, you will learn

* How to use Python dictionaries to store information indexed by objects
* How to organize related functions 
* How and when to use global variables
* How to read files and process text files
* How to save Python objects in JSON files
* How to create word clouds using third-party Python libraries 

## Project: What Is the Distribution of Pairs of Letters in the English Language?

Suppose you examine a text written in the English language. You will soon be able to find some patterns, such as the fact that the letter "e" appears much more frequently than the letter "q". In this project, we are going to explore a more subtle pattern that captures the frequency of pairs of letters. For example, if you do find a letter "q", it is much more likely to be followed by the letter "u" than by the letter "e"!

Your task is to read a corpus[^corpus] of writings in English and count the number of times each pair of letters appears in the corpus. For example, you may determine that the pair "sr" occurs 278 times, and that "ux" appears only twice. The corpus is in the file "training-set.txt", and it has already been preprocessed for you. In particular, all letters are lowercased, and all punctuation marks except "." have been removed.

[^corpus]: The corpus consists of selected writings from the early years of the internet that were archived at <http://www.textfiles.com>.

In the next project, we will use this information to break an encryption scheme, so it's important to store the information regarding the pair frequencies in a way that can be used later. Originally developed in JavaScript, JSON is a popular and convenient format for storing objects in Python and other computer languages. So you should write the results of your frequency analysis in a JSON file.

T> Our approach to breaking encryption relies on the likelihood that a body of text is English by looking only at letter pairs. In order to deal with typos and texts that are nearly English, it will actually be useful to ensure that no pair of letters, no matter how infrequent, is considered totally impossible. To make sure that all pairs of letters are given non-zero probability, initialize the counts to one instead of zero before counting pairs.

Finally, it always helps to visualize the answer to make sure that it seems reasonable. One way to visualize words and their frequency is called a *word cloud*. This is a diagram that depicts each word in a canvas, where the size of each word represents the frequency of the word. For example, Figure 3.1 shows a word cloud generated from the Declaration of Independence, after removing short words such as "the" and "of". 

![Figure 3.1: Frequent, Large Words in the Declaration of Independence](images/indep-wordcloud.png)

You should generate a similar word cloud for the frequency of letter pairs that you found in this project. For example, your word cloud should show that "th" is a very common pair of letters in English. Figure 3.2 illustrates what the answer may look like.

![Figure 3.2: Frequency of Bigrams in English](images/bigram-wordcloud.png)

A> Pairs of letters are also called *bigrams*, and this idea can be easily extended to *trigrams* and so on. The general term is *ngram*, and it can be applied to analysis of contiguous letters and also words. Google has an interesting visualization of word ngrams over time, using the books that Google has digitized as the corpus. See the [Google Books Ngram Viewer](https://books.google.com/ngrams) for some interesting examples.

This project is considerably more complicated than the previous projects, so it is extremely important to organize the program properly. It is simply easier for humans to keep straight the relevant details of two small things than the details of one big thing. That's why we break programs down into small functions that do only one thing and do that thing well. In that spirit, we suggest that you follow this organization:

1. Managing the pair frequencies:
  * A global variable `_PAIR_COUNTS`.
  * `initialize_counts()` that initializes the variable `_PAIR_COUNTS`.
  * `count_pairs(s)` that counts the letter pairs in the string `s` and updates the variable `_PAIR_COUNTS` accordingly.
  * `get_all_frequencies()` that creates a Python dictionary with the frequencies of the letter pairs encountered. This uses the information in `_PAIR_COUNTS`, but scales it by the number of pairs seen, so that the results are comparable across different corpora.
2. Reading the corpus and calling `count_pairs(s)` on each line to compute the letter pair frequencies.
3. Getting the computed frequencies and generating the word cloud.

## Python Dictionaries

In the first project, we encountered Python *variables*, which allow us to store a single piece of information, for example `grade = 93`. We followed this up in the second project with Python *lists* that store several related pieces of information, such as `exams = [96, 82, 93]`. Using lists, we can refer to individual pieces of information with subscripts, such as `exams[2]` for the third exam.

In this project, we will meet Python *dictionaries* which store information that can be accessed using a name instead of a numeric index. E.g., instead of referring to the third exam, we can use Python dictionaries to access the grade in one of your classes, for example `grades["math"]` or `grades["english"]`. The word "dictionary" is meant to suggest this type of relationship. I.e., a real dictionary stores a definition for each word, so an entry may be modeled in Python as `definition["computer"]`.

Dictionaries are denoted in Python using curly braces, as in `d = {}`. Listing 3.1 shows how a dictionary may be initialized in Python.

{title="Listing 3.1: Initializing a Dictionary", lang=python, line-numbers=on, starting-line-number=1}
~~~~~
capitals = {}
capitals["Alabama"] = "Montgomery"
capitals["Alaska"] = "Juneau"
capitals["Wyoming"] = "Cheyenne"
~~~~~

Dictionaries can also be initialized in a single line by specifying a list of *keys* and *values*, as in Listing 3.2. The keys are the Python objects used to store and lookup information, and the values are the pieces of information associated with a key. In Listing 3.1, for example, `"Alabama"` is a key with the value `"Montgomery"`.

{title="Listing 3.2: Initializing a Dictionary Inline", lang=python, line-numbers=on, starting-line-number=1}
~~~~~
capitals = {"Alabama": "Montgomery",
            "Alaska": "Juneau",
            "Wyoming": "Cheyenne"
           }
~~~~~

It is sometimes useful to gather all the keys or all the values currently stored in a dictionary. A common use is to iterate over all entries in a dictionary. For instance, Listing 3.3 shows how you can increment each entry of a dictionary.

{title="Listing 3.3: Iterating over a Dictionary", lang=python, line-numbers=on, starting-line-number=1}
~~~~~
population = { "Alabama":4.863, ..., "Wyoming":0.586 }
total_pop = 0
for state in population.keys():
    total_pop = total_pop + population[state]
~~~~~

Iterating over the items in a dictionary is so common that Python provides a convenient shorthand to using `population.keys()` in the `for` loop of Listing 3.3. If you iterate over a dictionary, Python simply assumes that you wish to iterate over the keys, as seen in Listing 3.4.

{title="Listing 3.4: Iterating Implicitly over a Dictionary", lang=python, line-numbers=on, starting-line-number=1}
~~~~~
population = { "Alabama":4.863, ..., "Wyoming":0.586 }
for state in population:
    total_pop = total_pop + population[state]
~~~~~

Python dictionaries have a nasty surprise. Suppose we wish to find the population of Ontario, so we try `population["Ontario"]`. Unfortunately, the dictionary `population` has only information on the population of states in the U.S.A., not Canada, so there is no entry for `"Ontario"`. If you try to access this non-existent entry, Python will give an error and stop the execution of your program.

To avoid this, you can check to see whether the entry exists before accessing it. Python provides a simply way of doing this using the `in` operator. The expression `key in dictionary` is `True` if there is an entry for the given `key` in the `dictionary`. For example, the function in Listing 3.5 looks up the population of a state, and returns zero if the value is unknown.

{title="Listing 3.5: Checking if an Entry Exists", lang=python, line-numbers=on, starting-line-number=1}
~~~~~
def get_population(state):
    if state in population:
        return population[state]
    else:
        return 0
~~~~~

A> Looking at Listing 3.5, you may think that zero is a particularly bad value to return for the population of Toronto, just because we have no data for it. You'd be right! The problem of missing data comes up repeatedly in data science, and there are a number of ways of dealing with it. For instance, in some settings it makes sense for missing values to be replaced by an average value, so that the population of Toronto would appear to be the average population of states in the U.S.A. In this particular case, this is not really much better, so it's still not clear what would be a good value to return. For cases like this, Python offers a convenient object called `None` which is not equal to any other Python value. It is, in fact, a perfect stand-in for "We have no data for this." So more Pythonic way of writing the function in Listing 3.5 is to replace `return 0` with `return None`.

## Global Variables and Program Organization

## Reading and Writing Text Files

## JSON

## Creating Word Clouds