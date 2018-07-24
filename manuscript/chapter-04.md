# Classes and Subclasses: NGrams for German

In this project, you will learn

* How to organize your program by using classes and subclasses
* How to organize your program by using modules and packages
* When to use classes as opposed to modules to organize your program
* How to avoid global variables by using classes

## Project: What Is the Distribution of Pairs of Letters in the German Language?

In the last project, you built a program that can find the distribution of pairs of letters in the English language. You may have found, for example, that the letters "t" and "h" are very likely to appear together in English text, whereas the letters "q" and "x" are not. But what about other languages, such as German? Obviously, the same code should work, but there are a few minor differences:

* The letters in German are not the same as the English letters.
* A different corpus is needed to learn the distribution of letter pairs in German.
* It should be possible to process both English and German letter pairs in the same program.

Your task is to reorganize your solution to the last project, so that the code is in a Python `class`. The class should be called `ngram`, and it should have the following methods:

1. An instance variable called `_PAIR_COUNTS`.
2. An initializer `__init__(self, letters="...")` that initializes the instance variable `_PAIR_COUNTS`. This method should accept an optional argument called `letters` that is a string containing all possible letters (and punctuation marks) in the language. By default, `letters` should have the letters in the English language.
3. A method called `count_pairs(self, s)` that counts the letter pairs in the string `s` and updates the instance variable `_PAIR_COUNTS` accordingly.
4. A method called `get_all_frequencies(self)` that creates a Python dictionary with the frequencies of the letter pairs encountered. This uses the information in `_PAIR_COUNTS`, but scales it by the number of pairs seen, so that the results are comparable across different corpora.
5. A method called `process_file(self, filename)` that reads a corpus and uses it to update the information in `_PAIR_COUNTS`.

As you can see, you have already written all the pieces for this assignment, so what is left to do is to reorganize your solution so that it uses a Python class. In particular, you should be able to use your new class as follows:

{title="Listing 4.1: Using the ngram class", lang=python, line-numbers=on, starting-line-number=1}
~~~~~
english = ngram()
english.process_file('english-corpus.txt')
english_freqs = english.get_all_frequencies()

german = ngram()
german.process_file('german-corpus.txt')
german_freqs = german.get_all_frequencies()
~~~~~

As always, if you know enough Python to be able to do this, feel free to write your code and move on to the next project. If you need some help, or if you need to learn about classes in Python, read through the rest of this chapter.

## Python Classes

Classes offer the most popular foundation for "object-oriented programming", and they are available in most programming languages, such as Java, C++, JavaScript, and so on. There are three main motivations for classes:

1. Classes help you organize your code
2. Classes encourage good design habits
3. Classes are a popular mechanism for supporting code reuse

In this chapter, we will focus on the first motivation, and we will defer classes in the context of design and code reuse to later chapters.

Listing 4.2 shows the outline of a class in Python. As you can see, the class contains definitions for various functions, called ``methods'' in object-oriented terminology. The methods provide the functionality offered by the class, and the special method `__init__(...)` is used to initialize each instance of the class.

{title="Listing 4.2: A Python class", lang=python, line-numbers=on, starting-line-number=1}
~~~~~
class Turtle:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.dir = 0

    def forward(self, steps):
        self.x, self.y = self.calculate_position(steps)

    def left(self, angle):
        self.dir = self.dir + angle

    def right(self, angle):
        self.dir = self.dir - angle

    def calculate_position(self, steps):
        ...
~~~~~

The `Turtle` class in Listing 4.2 has the essential code to implement a drawing sprite in a "Turtle-graphics" fashion. In Turtle graphics, the sprite (aka turtle) obeys some simple commands, such as "move forward", "turn left", or "turn right". These commands are exposed as methods of the Turtle class above.

At any given point in time, each turtle knows where it is and in which direction it is headed. This information is initialized in the `__init__()` method, which is automatically called whenever a new turtle is created. Line 1 in Listing 4.3 demonstrates how a turtle is created by calling the global `Turtle` function, which Python defines automatically when the class `Turtle` is defined as in Listing 4.2. The `Turtle` function calls `__init__()` automatically, so all turtles start at position `(0, 0)` and pointing in the direction 0, which is traditionally East in turtle graphics.

{title="Listing 4.3: Drawing a square in turtle graphics", lang=python, line-numbers=on, starting-line-number=1}
~~~~~
t = Turtle()
t.forward(150)
t.left(90)
t.forward(150)
t.left(90)
t.forward(150)
t.left(90)
t.forward(150)
t.left(90)
~~~~~

The key takeaways from Listings 4.2 and 4.3 are how we define new classes in Python, and how we can use Python classes in other parts of the code. E.g., looking closely at Listing 4.3, you can see that the commands `forward(150)` and `left(90)` are repeated four times to guide the turtle around a square. Listing 4.2 shows the definitions of those commands.

Taking a close look at Listing 4.2, you will see that the command `forward()` has two arguments: `self` and `steps`. And yet, it's called with only one argument, e.g., `t.forward(150)`. What you are seeing is the special place that the first argument, `self`, has in object-oriented programming. In this perspective, `forward()` is not really a function, but a method *of a specific instance of the Turtle class*. In line 1 of Listing 4.3, we call the `Turtle` method to create a new instance of the Turtle class. This instance has its own position and direction, and when this instance is told to move `forward()`, it will change its position appropriately. The method argument `steps` tells the turtle how many steps to go forward. But which turtle is supposed to move? The specific instance of the Turtle class is identified by using the dot notation. By saying `t.forward(150)`, we are specifying that it is the instance `t` that should move forward. Think about that: There could be many turtles, but it is only `t` that will move.

And that is how classes help you to organize your code. First, you can identify an important abstraction, or concept, in your code. In this case, you are saying that `Turtle` is an important concept in turtle graphics. That makes sense, doesn't it? And by building a class called `Turtle`, this concept is made explicit. Without the class, you would have to point to several variables (e.g., `x`, `y`) and functions (e.g., `forward()`, `left()`) and keep in mind that these variables and functions implement a turtle, and that the rest of the code does something else. The `class` declaration marks the box around the implementation of the `Turtle` concept, so you don't have to keep this boundary in mind.

Second, by building a box around the abstraction, you are explicitly saying what is and is not involved in the abstraction. In this case, you can read the `Turtle` class, and immediately know that the `Turtle` abstraction depends on the variables `x`, `y`, and `dir`. Those variables will be used by the methods of the `Turtle` class, and you can see how they are used in `forward()`, for example. Here is the crucial part. Those variables should *not* be used outside of the `Turtle` class. Not only does the class specify what is inside and outside of the class, it also defines the protocol that is used at the boundary so that code outside of the class can interact with an instance of the class. In this particular case, the class states that outside code can call the methods `forward()`, `left()`, and `right()`. That's it. Code outside of the class cannot look directly at `x`, `y`, or `dir`, for example.

At the risk of muddying the waters, we have to discuss an important difference between object-oriented programming in languages like Python, as opposed to languages like C++ or Java. As we've seen, an important benefit of object-orientation is that it allows you to keep separate parts of your code separate. The code that *uses* Turtle graphics to create a square does not need to know *how* Turtle graphics is implemented. This reduces the overall complexity of the code, because you (the programmer) do not need to be aware of the Turtle implementation when writing the code for a square, or more complex geometric shapes. Conversely, when implementing the Turtle graphics, you will not need to worry about how other code uses variables like `x`, `y`, or `dir`. In fact, if you conceive of a better implementation of Turtle graphics, say one based on polar coordinates instead of Cartesian coordinates, you are completely free to change your code using this new insight, so long as you keep the **public** interface of the methods `forward()`, `left()`, and `right()` in place. This is a huge benefit, because it allows you (the programmer) to keep your focus on the code that you are currently working on, instead of having to consider all the possible interconnections between the entire code at all times. I.e., if you're working on class `A`, you can to think about class `A` and not all the other classes up to `Z`.

In languages like C++ and Java, this separation of the code via classes is enforced by the language. What this means is that it is simply impossible for code that is not in class `A` to access the "private" variables of class `A`. For instance, it would be impossible for code outside of the `Turtle` class to access the variables `x` or `y`. In Python, however, this separation is **not** enforced by the language. It is simply a convention. Listing 4.4 shows how a foolish programmer could intrude inside a Turtle to change its `x` coordinate.

{title="Listing 4.4: Bad Practice: Accessing private variables", lang=python, line-numbers=on, starting-line-number=1}
~~~~~
t = Turtle()
t.x = 100
~~~~~

The problem with code such as in Listing 4.4 is that the programmer violates the boundaries around the `Turtle` class, thus losing one of the main benefits of object orientation. So it makes sense that this practice is prohibited in languages such as Java, where the variables in a class can be kept private to that class. However, there are times when it is useful for code outside of the class to at least be able to look at internal variables. For example, what is the harm of letting code outside of the `Turtle` class to **see** the value of `x`? In languages like Java, this situation can be resolved by either making the variable `x` public, or providing special "getter" and "setter" methods, like `t.getX()` and `t.setX(new_x)`. In Python, this situation is addressed by a naming convention on the variables. The programmer of a class is in the best position to decide whether a variable should be visible or out outside of the class. The Python language does not enforce this visibility, but the programmer can make it clear by naming the variables appropriately. By convention, private variables are named with two underscores at the beginning. So to keep the variables `x` and `y` private, you should call them `__x` and `__y` instead, as seen in Listing 4.5.

{title="Listing 4.5: A Python class with private variables", lang=python, line-numbers=on, starting-line-number=1}
~~~~~
class Turtle:

    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__dir = 0

    def forward(self, steps):
        self.__x, self.__y = self.__calculate_position(steps)

    def left(self, angle):
        self.dir = self.dir + angle

    def right(self, angle):
        self.dir = self.dir - angle

    def __calculate_position(self, steps):
        ...
~~~~~

Notice that the convention to use leading double underscores (sometimes called "dunders") to indicate private variables also applies to naming methods. The method `__calculate_position()` is explicitly marked as private, so we do not consider it to be a part of the public interface, namely `forward()`, `left()`, and `right()`. Using private names outside of the class is still possible in Python, since it really doesn't **enforce** private names, but it is difficult for two reasons. First, the programmer who accesses `__x` outside of the `Turtle` class *knows* that he is violating the protocol, since he has to type that leading underscore. By acknowledging that he is violating the intent of the class author, he is essentially taking responsibility if something breaks. Second, Python actually renames the variable `__x`, so `t.__x` does **not** work. What Python does with the name is predictable (and you can look that up elsewhere if you really want to), so a programmer who really wants access to these "private" variables can get at them, but why would anybody go to that much trouble?

Finally, do not confuse the convention of using a double underscore to indicate "private" with the use of leading *and* trailing double underscores, as in `__init__()`. The use of both leading and trailing underscores in a name denotes that it has special significance to Python. E.g., `__init__()` is the name of a constructor method, which is used to create new instances of the class. Other object-oriented languages also have constructor methods, though they vary on the specific naming conventions to identify the constructors.

Before wrapping up this discussion about classes, let's take one more look at the constructor method `__init__()`. As seen in Listing 4.5, the constructor initializes a turtle to start at the origin and pointing in the direction 0, which is typically taken to be the direction of the positive x-axis. But what if we wanted to create a new turtle that is in another location or pointing in a different direction? The way to do this is to provide extra arguments to the constructor. Python lets you declare as many arguments as you want in the constructor, but there can only be one constructor in a class, and it must be called `__init__()`. For example, Listing 4.6 shows how the position and direction of the turtle can be specified at creating time using optional arguments in the constructor.

{title="Listing 4.6: A Python class with private variables", lang=python, line-numbers=on, starting-line-number=1}
~~~~~
class Turtle:

    def __init__(self, x=0, y=0, dir=0):
        self.__x = x
        self.__y = y
        self.__dir = dir

    ...

t1 = Turtle()
t2 = Turtle(100, 200)
t3 = Turtle(dir=90)
~~~~~

In Listing 4.6, the turtle `t1` is initialized at the default position and direction, i.e., at the origin and pointing along the positive x-axis. But `t2` is initialized at a specific location of `(100, 200)`, and `t3` is the default origin location, but is pointing in direciton 90, corresponding to the positive y-axis.

Finally, classes should always be documented with docstrings. A single docstring for the entire class should be placed immediately after the `class` statement. The format of the class doctring is very similar to what we've been doing for functions, although it does not include `Parameters` or `Returns` sections, since classes do neither. On the other hand, it can include a section called `Attributes` that describes any instance variables of the class. Generally speaking, avoid documenting private attributes in the class docstring. Methods should be documented in the same way as regular functions, but do not document the `self` parameter, which is simply assumed to be the first argument of any method. Listing 4.7 shows a fully documented version of the `Turtle` class.

{title="Listing 4.7: A Python class", lang=python, line-numbers=on, starting-line-number=1}
~~~~~
class Turtle:
    """A virtual sprite that can move in a 2-dimensional world.

    A turtle is a virtual creature that lives in a 2-dimensional world.
    At any given time, it knows its position and direction, and it can
    move forwards by any amount, as well as turn left or right from its
    current direction.

    Attributes
    ----------
    x : int
        x-coordinate of current position
    y : int
        y-coordinate of current position
    dir : float
        current direction in degrees, where 0=East, 90=North, etc.
    """

    def __init__(self, x=0, y=0, dir=0):
        """Initialize a turtle at the given position and direction.

        Parameters
        ----------
        x : int
            x-coordinate of initial position
        y : int
            y-coordinate of initial position
        dir : float
            initial direction in degrees, where 0=East, 90=North, etc.

        Returns
        -------
        Turtle
            A new turtle

        Examples
        --------
        >>> t = Turtle(x=0, y=0, dir=0)
        >>> t.x
        0
        >>> t.y
        0
        >>> t.dir
        0
        >>> t = Turtle(x=100, y=200, dir=90)
        >>> t.x
        100
        >>> t.y
        200
        >>> t.dir
        90
        """
        self.x = x
        self.y = y
        self.dir = dir

    def forward(self, steps):
        """Move the turtle forward along the current direction.

        Parameters
        ----------
        steps : int
            The number of steps to move

        Examples
        --------
        >>> t = Turtle(x=0, y=0, dir=0)
        >>> t.forward(100)
        >>> t.x
        100
        >>> t.y
        0
        >>> t.dir
        0
        >>> t.forward(50)
        >>> t.x
        150
        >>> t.y
        0
        >>> t.dir
        0
        """
        self.x, self.y = self.__calculate_position(steps)

    def left(self, angle):
        """Turn the turtle direction a number of degrees to the left.

        Parameters
        ----------
        angle : float
            The number of degrees to turn

        Examples
        --------
        >>> t = Turtle(x=0, y=0, dir=0)
        >>> t.left(45)
        >>> t.x
        0
        >>> t.y
        0
        >>> t.dir
        45
        >>> t.left(30)
        >>> t.x
        0
        >>> t.y
        0
        >>> t.dir
        75
        """
        self.dir = self.dir + angle

    def right(self, angle):
        """Turn the turtle direction a number of degrees to the right.

        Parameters
        ----------
        angle : float
            The number of degrees to turn

        Examples
        --------
        >>> t = Turtle(x=0, y=0, dir=0)
        >>> t.right(45)
        >>> t.x
        0
        >>> t.y
        0
        >>> t.dir
        -45
        >>> t.right(30)
        >>> t.x
        0
        >>> t.y
        0
        >>> t.dir
        -75
        """
        self.dir = self.dir - angle

    def __calculate_position(self, steps):
        """Calculate the new position after moving given number of steps in current direction.

        Parameters
        ----------
        steps : int
            The number of steps to move

        Examples
        --------
        >>> t = Turtle(x=0, y=0, dir=30)
        >>> t.__calculate_position(100)
        (87, 50)
        """
        import math
        theta = math.radians(self.dir)
        dx = round(steps*math.cos(theta))
        dy = round(steps*math.sin(theta))
        return self.x+dx, self.y+dy
~~~~~

## Python Modules and Packages

Python **modules** and **packages** offer a different way to organize code. 
In essence, a **module** is simply a file with a `.py` extension that contains some Python code. It may define functions, classes, variables, and even include Python statements. In other words, a module is a simple Python file. What makes it special is that it can be **imported** from another Python file.

For example, in the previous section we defined the class `Turtle`. Let's say we did this in the file `turtle.py`. Now we can create another file, say `polygon.py`, that **uses** the `Turtle` class, by issuing an `import` statement. As you can see, this is just like all of the other libraries we have been using, e.g., `random`. These libraries were Python modules that were integrated with your Python environment. What we are doing now is to write our own modules.

Listing 4.8 shows how the `Turtle` class can be used from the Python program in the file `polygon.py`. As you can see, any names defined in the file `turtle.py` are available using "dot notation". For example, the `Turtle` class defined in `turtle.py` has the name `turtle.Turtle` in the file `polygon.py`, as seen in Line 4 of Listing 4.8. Similarly, if the file `turtle.py` defines the global variables `NORTH` and `SOUTH`, they would be available as `turtle.NORTH` and `turtle.SOUTH` in `polygon.py`.

{title="Listing 4.8: Using a Python module", lang=python, line-numbers=on, starting-line-number=1}
~~~~~
import turtle

def polygon(sides, length):
    t = turtle.Turtle()
    for i in range(sides):
        t.forward(length)
        t.left(360/sides)

polygon(4, 100)
~~~~~

Using your own modules is completely consistent with the way the built-in modules, e.g. `math`, are used. But there is one important difference. How does Python know where to find modules? The answer is that the Python system keeps track of a list of directories (also called folders) where it should look for modules, and it finds modules by looking for the right file at each of these directories in turn. That's why the code in the file `polygon.py` can find the `turtle` module. The file `turtle.py` is in the same directory as `polygon.py` and that base directory is one of the ones in the list that Python uses to look for modules.

So Python uses both modules and classes to help you organize your code. When do you use one or the other? The answer is that the two approaches are completely complimentary. Modules make the most sense to organize code, especially in large projects, because they use the file system to keep code separate. I.e., each module is in its own file, and it helps to organize the code in this way, so that you know what code is relevant when editing any given file. So you'll be using modules extensively in Python, especially if you plan to work in large Python projects, if for no other reason than it is simply impractical to keep a large code base in just one file.

But classes have a considerable advantage in many cases. In Python, each module exists only once. If you import a module multiple times, you still have only one version of the module, so if the module defines a particular global variable, there is only one version of this global variable, and it is shared wherever the module is imported. However, classes can have many instances, and each instance can have its own copy of its attributes. For example, each `Turtle` has its own values of `x`, `y`, and `dir`. Similarly, you can have multiple instances of the ngram code, one instance for English and the other for German. That is precisely the point of the project in this chapter! 

So that's how you know that you should be using classes. The code that you want to organize consists of some data that is shared by several functions, e.g., in turtle graphics, you have position and direction data shared by movement and rotation functions. Moreover, you want to have multiple instances that have the same code, but different versions of the data. E.g., each turtle has its own notion of position and direction, but all turtles share the code that moves and rotates them. That's why turtle graphics is a natural setting for object-oriented programming.

That leaves just one question. What exactly are Python packages? If you think of a Python module as a file, then a Python package is simply a directory that can store Python modules (files) and other packages (sub-directories). There is only one additional twist. A directory can be a Python package only if it contains a file called `__init__.py`. This restriction is there so that the Python interpreter does not waste time looking for modules and packages inside just any random directory that it finds. In most cases, you will find that the `__init__.py` file can be empty; it's just there to mark its parent directory as a Python package. In some cases, however, the `__init__.py` file will contain code that is required to initialize the package, e.g., to set up some global variables or open a network connection.

Now that you know the tools commonly used to organize Python code, be sure to keep your code neatly organized, especially as the projects become larger and more complex.

