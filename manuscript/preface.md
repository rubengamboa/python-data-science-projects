# Preface

## Who This Book Is For

This book grew out of an accelerated introduction to Python at the University of Wyoming. It is meant as an introduction to programming, so it does not assume any prior programming experience. But, unlike other introductory texts, its philosophy is that you will learn programming better by learning not just a computer language, but also related frameworks. In other words, it is better to learn how to build a chart with the use of a sophisticated charting package, than it is to learn how to loop through an array to find its maximum and minimum values.

In other words, this book is not intended to teach you the syntax of Python and a handful of simple algorithms that you can write in Python. Instead, my goal is to teach you how to write Python programs that are actually useful in the context of data science, and that means showing you some of the Python libraries that are popular in data science, such as `NumPy`, `pandas`, and `matplotlib`. With this goal in mind, I have chosen several different projects that are illustrative of data science goals. Some of the projects have surprising depth, e.g., Eigenvectors, Markov processes, hill climbing, etc., but I will not dive into these depths, choosing instead to keep the focus on programming and the conversation informal instead of mathematical.

If you are an experienced programmer who already knows Python, you may already know everything that this book can teach you. But this book may still be useful to you by suggesting some programming challenges related to data science that you may want to try. And if you're familiar with Python but not with `NumPy`, `pandas`, and `matplotlib`, this book will help you learn those.

Oh the other hand, if you are not an experienced programmer but would like to learn more about programming or how computers can be used to learn insights from raw data, then this book  is definitely for you. It will teach you  everything you need to know in order to build some useful data science applications.

## How to Use This Book

The first section in each chapter in this book introduces you to a new project. If you are confident that you can build that project, feel free to skip the chapter. But if you're not, then take a look at the rest of the chapter, where I will introduce you to the new programming concepts of library features that you need to learn in order to finish the project. For example, the project in Chapter 2 asks you to explore a function by plotting it along with other, more familiar functions, and use the results to guess how the original function actually grows. If you feel like that's something you can do, awesome! Take a look at Chapter 3. Otherwise, Chapter 2 will teach you about lists in Python and the features of `matplotlib` that allow you to create 2D plots.

## How This Book Is Organized

Each chapter in the book corresponds to a project that was chosen to illustrate a specific Python or data science technique. The first two chapters serve as a quick introduction to programming, describing variables and the basic Python control structures.  These chapters also introduce Python functions, the list data structure, and basic charting commands with `matplotlib`. Note that the project in Chapter 2 expands upon the project in Chapter 1, so there is a strong dependency between these two chapters.

Chapter 3 introduces file processing in Python, simple string processing, and also the dictionary data structure. Chapter 4 uses these results in the context of search and optimization. There is a slight dependency between these chapters, but it can be bypassed completely by downloading my solution to Chapter 3.

Chapter 5 introduces two new ideas, `NumPy` arrays and random walks. These are used to predict the outcome of future sports games. The ideas in this project are widely used in data science, although a full treatment of this approach involves advanced mathematics, which lie outside the scope of this book.

Chapter 6 introduces `pandas` data frames and uses them to explore a real-world data set. Descriptive statistics are used to summarize the information in the data frame.

Chapter 7 turns social! This chapter introduces methods of gathering data from the internet directly from Python. This leads to Chapter 8, which uses data from Twitter to demonstrate advanced visualization techniques and simple text processing. Then Chapter 9 introduces Python modules and classes, and expands the project in Chapter 8 to visualize Facebook data.

Finally, Chapter 10 introduces `pandas` time series data and the concept of linear regression. It also illustrates the place that models have in data science. In particular, the project is based on a simplified version of the the Capital Allocation Pricing Model from financial theory, and this model is what justifies the use of regression for this data set.
