
# coding: utf-8

# # Semantics and pragmatics, KIK-LG103
# ## Lab session 1
# 
# The purpose of this lab is to learn the basics of Python programming. Some of the exercises will be general in nature (as in not directly related to language technology), but try to always relate the programming concepts to what we learned during the first LT lecture.
# 
# The following concepts will be introduced in this lab:
# 
# * [Variables and assignment](#vars)
# * [Strings](#string)
# * [Conditionals and boolean logic](#conbo)
# * [Lists and iteration](#list)
# * [Sets](#set)
# * [Indexing and slicing](#slice)
# * [Functions](#fun)
# 
# Without further ado, let's get into it.

# ---
# ### Preparation: Hello Calculator!
# ---
# 
# A classic introduction to computer programming in any language is the "Hello World!" program. Running the program prints the message *Hello World!* on the user's screen. Another entry point found in many Python programming tutorials and books is using the programming environment as a calculator. Saluting the traditions, let's try out the two exercises here.
# 
# The first code cell below consist of one line of code, the `print` function. Functions will be explained later in this lab, so don't worry about the terminology yet, but you can probably already guess what `print` does. Inside the parentheses that follow you see double quotes. Double quotes in Python indicate strings (for now, you can think 'text'). Write your message inside the quotes and press `Ctrl + Enter` to run the code cell.

# In[ ]:

print("")


# For the second exercise we will do some math. The basic math operators in Python are:
# 
#     +    Addition
#     -    Subtraction
#     *    Multiplication
#     /    Division
#     
# Try out some calculations in the cell below. Write the expression you want to evaluate and press `Ctrl + Enter` to execute. You should see something like this:
# 
#     In [1]: 8/2
#     Out[1]: 4.0
#     
# Note: When writing complex expressions, it is often helpful (and/or necessary) to include parentheses. These work exactly as in our regular mathematical notation: 
# 
#     In [2]: (8+2)/5
#     Out[2]: 2.0
# 
# You can also include spaces between numbers and operators to make the expression more readable.

# In[ ]:

(8 + 2)/5


# You probably now feel confident executing code cells in this notebook. In order to do something more substantial than calculating basic math expressions, we now dive into basic programming. The concepts introduced are really "Programming 101", and mostly independent of the language used. If you already have some background in programming, this lab should be a breeze. If you have never programmed before, Python with its simple and clean syntax is definitely a great way to get started.

# ---
# ### Section 1: Variables, assignment and strings <a name="vars"></a>
# ---
# #### 1.1.Variables and assignment
# 
# One of the most fundamental ideas in programming is the **variable**. A variable is simply a *piece of data* (for example text) that is linked to an *identifier*. Below we **assign** the value `"John"` to the identifier `'firstname'` and then print it. Assignment is done using the '**=**' symbol.

# In[ ]:

# The '#' symbols in code signal that whatever comes after is
# a comment. Comments are meant for humans and are simply
# ignored during the executiong of the code

firstname = "John"    # These two lines amount to what we did above:
print(firstname)      # print("John") would give equivalent output


# The link between the contents and the identifier is arbitrary, that is, the contents are not necessarily reflected in the form. Does this sound familiar to a linguist? 
# 
# Leäts illustrate variables with a familiar example. Think of the pronouns. In one context the pronoun 'it' might refer to a car ("Did you crash it?"), in others to a cat ("It's cute, isn't it?"). The form 'it' has nothing to do with what a car looks like or how it functions. The same is true of variables. The name of the variable can be almost anything (excluding most special characters and some reserved words like **if** and **and**). Also, we might first assign the variable one value ("Cathy") and later change it to another ("Newman").
# 
# ---
# 
# **Ex 1.1.1** In the code cell below, assign the name of your favorite person to some variable (for example `'favorite_person'`) and print it. This should be two lines of code. Then add two more lines where you change the value of the variable to something else and print the new value. The output of your code should look something like this:
#     
#     Cathy
#     Newman
#     
# See the code cell above for how assignment and printing was done.
#     
# ---

# In[ ]:




# When we tried some calculations in the previous section, we always used numbers explicitly: 
# 
#     in [ ]: 2 + 2
#     out[ ]: 4
# 
# We can also assign a numeric value to some variable and then use that in place of numbers in calculations:
# 
#     in [ ]: number = 2
#             number + 3
#     out[ ]: 5
#     
# ---
# 
# **Ex 1.1.2** Below you see a short exchange. Your task is to first assign the variable `'your_age'` some value (for example, your age). Then assign the variable `'my_age'` the correct value so that `'my_age'` is 10 years older. Do this second assignment using the variable  `'your_age'` and addition.
# 
# ---

# In[ ]:

print("What is your age?")

your_age = 0
print("Your age is", your_age)

# Assign the right value to the variable 
# 'my_age' using the variable 'your_age'
my_age = 0

print("I'm ten years older than you so my age is", my_age)


# What's the benefit of using the first variable in the assignment of the second variable? Why don't we just hard-code the right values? (For example, `your_age = 10` and `my_age = 20`) You might want to try changing the value of `'your_age'` to figure this out.

# #### 1.2 Strings and data types <a name="string"></a>
# 
# In the Preparation section we mentioned that you can consider a string as something akin to a piece of text. More accurately, a string is a *sequence of characters*. It is one of the basic *data types*, and for obvious reasons, one that we as students of LT are very interested in. Another basic data type would be **`int`**, representing integer numbers. You already worked with ints above when you tried calculating things. We will introduce more data types along the way; for now, let's make sure the difference between strings and ints is clear.
# 
# As you saw above, strings are surrounded by double quotation marks (in fact single quotes work too):
# 
#     Option 1:    in [ ]: city = "Berlin"
#     Option 2:    in [ ]: city = 'Berlin'
#     
# ints, however, are written as plain numbers, without quotation marks, or anything else for that matter. 
# 
#     year = 2049
#     
# ---
# 
# **Ex 1.2.1** Run the cell below and inspect the output. What went wrong? Correct the code and you might figure out the meaning of life (and see why it's important to keep in mind the distinction between strings and ints).
# 
# Note: **str** means the string type.
# 
# ---

# In[ ]:

year = "1984"
(300 + 404 + year)/64


# Clearly the original addition didn't work out all too well. Though you can't add together a string and an int, confusingly enough, the "addition" (+) does actually work for two or more strings. 
# 
# ---
# 
# **Ex 1.2.2** Try adding together some strings in the cell below and figure out what the operator does in this case.
# 
# ---

# In[ ]:

"a" + "b" + "c"


# In the case of the `+` operator with strings we talk about **concatenation** and not addition.
# 
# Finally, to recap some of the things we learned in this section, let's put the ideas together. If you run the code cell below you will get some error messages again. The code is trying to print out the variable `'you'` but we forgot a piece of code. 
# 
# ---
# 
# **Ex 1.2.3** Add a line of code where you initialize the variable with some (string) value and try again.
# 
# ---

# In[ ]:

print("What's your name?")


print("I am talking to", you)


# As you see we can write multiple things inside the parentheses of the `print` function, separated by commas. We are allowed to use things other than strings in print statements as well. 
# 
# ---
# 
# **Ex 1.2.4** Run the first cell below. In the second code cell, change the variable '`abrahams_age`' from string to int and try to figure out how to print out the same text as in the first cell. You might have to discard the whole variable '`sentence`' (or alternatively figure out what the function `str()` does if you feed it an integer).
# 
# ---

# In[ ]:

# One variable containing the person's age
abrahams_age = "175"

# Another variable containing the sentence,
# a concatenation of two strings
sentence = "Abraham died at age " + abrahams_age

# Here we print the variable containing the
# whole sentence
print(sentence)


# In[ ]:

# Change this to 'int'
abrahams_age = "175"

# Can we still do this?
sentence = "Abraham died at age " + abrahams_age

# Match the output of this print to 
# the output of the previous cell
print(sentence)


# ---
# 
# ### Section 2. Conditionals and boolean algebra <a name="conbo"></a>
# 
# ---
# 
# In programming, as in life, actions are often executed conditionally: 
# 
#     If the person looks at me and s/he's not my ex, say hello - otherwise ignore.
#     
#     If the password is correct, log in.
#     
# "Conditional execution of actions" sounds cumbersome and boring, though. Fortunately computer scientists have come up with a much cooler name for this concept: **Flow control**
# 
# Below you see a few lines of code illustrating basic flow control. Try to figure out what each part of the code does before reading forward. You can also try changing the value of `'person_is_ex'` to `False`, or `person_name` to something else and see what happens. If you find this hard, don't worry; we'll deconstruct the code in a minute.

# In[ ]:

person_name = "Uvuvwevwe"
person_is_ex = True

if person_name == "Uvuvwevwe" and person_is_ex:
    print("Ignoring.")
else:
    print("Hi Uvuvwevwe!")


# So what's unfamiliar here? There seems to be something fishy about the assignment of the variable `'person_is_ex'`. Below that, there are a few lines of code that seem like normal english with a few words highlighted (if, is, and, else). Also, what's with the whitespace in front of the print statements? Let's attack each of these points individually.
# 
# #### 2.1. Boolean values
# 
# As you might have guessed, the `'person_is_ex'` variable isn't a string, though it might at first glance look like one. Here we introduce a new data type: **boolean**. The boolean data type is a comfortingly simple one; it has two values, *True* and *False*. Notice the uppercase T and F. These two boolean values are the atomic elements of flow control. What separates the boolean values *True* and *False* from the strings *"True"* and *"False"* are the quotation marks around the strings.
# 
# The comparison operators that return boolean values are:
#     
#     a == b        a is equal to b
#     a != b        a is not equal to b
#     a < b         a is less than to b
#     a > b         a is greater than to b
#     a <= b        a is less than or equal to to b
#     a >= b        a is greater than or equal to b
#     
# ---
# 
# **Ex 2.1.1** Try evaluating some comparisons in the code cell below.
# 
# ---

# In[ ]:

print("John" != "Maggie")

print(3 < 2)


# #### 2.2 Boolean algebra 
# 
# Performing operations on the boolean values True and False is called **boolean algebra**. We have already encountered the basic operations of boolean algebra during the lecture in the form of first-order predicate logic. The basic operations are **and**, **or**, and **not**.
# 
# ---
# 
# **Ex 2.2.1** Evaluate your own expressions in the code cell below. You can use parentheses for clarity, and sometimes they are necessary for correct evaluation.
# 
# ---

# In[ ]:

("John" == "Maggie") or (not (3 <= 2) and ("a" != "b"))


# #### 2.3 Conditionals
# 
# Next we'll look at the following construction:
#     
#     if something is True:
#         do this
#     else:
#         do that
#         
# Written in this "pseudo-Python", the construction is probably clear to you. Imagine yourself being in control of the execution of the code. You get to the line starting with `if` and evaluate whatever expression comes after it. If the expression is `True`, you continue to the code between the `if` and the `else` lines, otherwise you skip that part and continue after `else`.
# 
# The whitespace (four spaces) is used to mark what block of code belongs under the `if` branch and which belongs under the `else` branch of the construction. This is called **block indentation**.
# 
# 
# Sometimes we need more flexibility in our actions instead of just a binary choice: *if this - do this, if that - do that, if that third thing - do something funny, otherwise - do whatever you want*. In Python this can be accomplished with **elif** (from else-if): 
# 
#     if this is True:
#         do this
#     elif that is True:
#         do that
#     elif one more thing is True:
#         do yet another thing
#     else:
#         do whatever
#         
# The program goes through the `if`s and `elif`s one by one until it finds a true case. If no true case is found, the program executes whatever code is in the `else` block.

# #### TODO: EX HERE ABOUT IF-ELIF-ELSE

# ### Section 3. Lists and sets <a name="list"></a>

# We'll now move on to two very useful data types: **lists** and **sets**. Let's start with a motivating example; again, run the cell and see if you can figure out what the code does before reading on.

# In[1]:

all_names = ["Raphael", "Leonardo", "Donatello", "Michelangelo", "Splinter"]
all_names_sorted = sorted(all_names)

for name in all_names_sorted:
    print(name, "is a good name, I like it!")
    
amount_of_names = len(all_names)
print("It looks like we had", amount_of_names, "names there.")


# #### 3.1. Lists and iteration
# 
# The very first line of code introduces the list data type. A list is nothing but an ordered collection of elements of any data type. In this case, it is a collection of strings. "Ordered" here means that two lists are equivalent only if they have the same elements in the same positions. Sometimes we want the set ordered in a different sense. In the code cell above, we assign to the variable `'all_names_sorted'` the original list in alphabetical order with the help of a function `'sorted'`. 
# 
# ---
# 
# **Ex 3.1.1** Experiment with sorting and the equivalence of lists in the code cell below.
# 
# ---

# In[ ]:

[1, 1, 2, 3, 5, 8] != sorted( [8, 3, 1, 2, 5, 1] ) 


# Next in the code (4-5) we print out a few compliments to the turtles, going through the names in alphabetical order. Going through all the elements in a list one by one is called **iteration**. The syntax for simple iteration is very intuitive in Python. This is called the for-loop:
# 
#     for thing in list:
#         do the thing
#         
# The for-loop above works in a simple way:
# 
#     1. Go to the start of the list
#     2. Assign the value of the element in current position to the variable 'thing'
#     3. Execute whatever code is in the body of the for-loop
#     4 a. If we are not at the end of the list, move to next position and go back to 2.
#       b. If we are in the final position, exit the for-loop
# 
# Here is an example of how we can define a variable outside the for-loop, and then use the loop to change the value of that variable:

# In[2]:

number = 0
print("Value of number at the start:", number)

list_of_numbers = [123, 456, 789, 432, 117]
for n in list_of_numbers:
    number = number + n
    
print("Value of number at the end:", number)


# ---
# 
# **Ex 3.1.2** Below you are given a list of characters that make up a magic word. Use a for-loop and string concatenation ("+" from section 1.2) to construct the word. In other words, find a way to go from a list of characters to a single string consisting of those characters: `["a", "b", "c"] ==> "abc"`. Look at how the number was incremented in the code cell above for inspiration (`number = number + n`).
# 
# ---

# In[ ]:

characters = ["c", "o", "v", "f", "e", "f", "e"]
word = ""

# Use a for-loop here
    
print(word)


# Finally, we used the function `len` to calculate the length of the list. `len` can also be used with string and sets:

# In[ ]:

word = "Capricciosa"
print("The length of the word is", len(word), "characters.")

pizzas = {"Quattro Stagioni", "Funghi", "Napolitana"}
print("It looks like there are", len(pizzas), "different pizzas in the set.")


# #### 3.2 Sets <a name="set"></a>
# 
# Moving on from lists, let's look at some code again. If this looks like a lot, don't worry. We will explain everything along the way.

# In[3]:

# This is one way of splitting a string into multiple lines for readability,
# '\' signals that the expression continues to the next line.
sentence = "Raphael, Leonardo, Donatello and Michelangelo "             "are a bunch of mutant ninja turtles training "             "under the mutant ninja rat Splinter."
        
sentence_as_list = sentence.split()
word_types = set(sentence_as_list)

print("A sentence (as list) about some turtles:")
print(sentence_as_list)

# '\n' inside the string is a newline character 
# (see that empty line in the output?)
print("\nThe set of words in the sentence:")
print(word_types)


# Line 7 above shows one way of turning a single string (`"alpha beta"`) to a list (`["alpha", "beta"]`) with the `split` method. By default, it splits the string at whitespace. You can do more complicated stuff with it but for our purposes, this is enough. 
# 
# The next line (8) introduces the *set* data type. We can turn a list (`sentence_as_list`) into a set (`word_types`) using the `set` function as shown. Examine the output carefully to figure out what the difference between a set and a list is. The variable name `'word_types'` could also be a good hint.
# 
# ---
# 
# As you probably figured out, the set is a collection of *unique* elements. Any duplicate elements in the list (*ninja, mutant*) only show up once in the set. In this case, the list can be thought of as representing the *word tokens* of the original sentence (in the original order), while the set represents the *word types* (in no particular order).
# 
# We can construct a set also without the `set` function. Below is an example of how to do this with curly brackets (in contrast to lists where we use square brackets). The set is also another example of an **iterable**, that is, we can go through the elements in the set using a for-loop like we did with lists.

# In[ ]:

nice_words = {"nice", "nicer", "nicest"}
for word in nice_words:
    print(word)


# A nice thing about the `set` funtion is that we can give it things other than lists as well. 
# 
# ---
# 
# **Ex 3.2.1** Try feeding the function a string and print the elements in the set using a for-loop to see what it does.
# 
# ---

# In[ ]:

example_string = "All those moments will be lost in time, "                  "like tears in rain. Time to die."

# Use the 'set' function properly here ...
something = set()

# ... and print the result out with a for loop here.
# 'pass' is simply a placeholder that does nothing;
# delete it and write the print statement instead.
for thing in something:
    pass


# ### Section 4: Indexing and slicing <a name="slice"></a>

# Above we saw that you can feed both strings and lists to the `set` function and you will get out the unique elements that make up what you fed in (characters in the case of a string, strings in the case of a list of strings). The similarities between strings and lists do not end there, however. Actually, strings and lists in python are variants of an underlying abstract type, **sequence**. As a result, they share many of the operations we have already seen (for-loop also works with strings, you can concatenate lists like strings etc.) In this section we introduce two more operations that work with both lists and strings: **indexing** and **slicing**. Again, see the example code in the next cell.

# In[ ]:

sentence = ["Louie", "I", "think", "this", "is", "the",
            "beginning", "of", "a", "beautiful", "friendship."]

print("The first word of the sentence is:", sentence[0])
print("The last word of the sentence is:", sentence[-1])


# #### 4.1 Indexing
# 
# Above we see an example of indexing, accessing a specific element of a list. A thing to keep in mind with Python is that indexing starts at **0**. Here is an illustration of the indexes of a list:
# 
#     ["Play", "it", "once", "Sam"]
#        0      1      2       3
#       -4     -3     -2      -1
#       
# As you can see, you can also access an element by starting the indexing from the end.
# 
# ---
# 
# **Ex 4.1.1** TODO
# 
# ---

# In[ ]:




# #### 4.2. Slicing

# In[ ]:

word = "Lazlo"

print("The second and third letters of the word are:", word[1:3])
print("The first four letters of the word are:", word[:4])
print("The last four letters of the word are:", word[-4:])


# With slicing, we can access a part longer than one element of a list or a string. For example, in the first print statement above we access the second and third letters of the word using `word[1:3]`. As you might notice, picking the right indices here is an error-prone process. First of all, we must remember that the indexing starts from 0, so the index of the second element is 1. Second, in the construction for slicing `[startindex:endindex]`, the `endindex` is **exclusive**, that is, the element in that index is not taken into account. The `startindex` is inclusive, however. In other words, `word[1:3]` means '*the substring of `word` from index 1 (inclusive) to index 3 (exclusive)*'.
# 
# In the second and third print statements we see that only the starting or ending index is given. If the starting index is missing, the slicing implicitly starts from the beginning of the string. If the ending index is missing, the slicing is inferred to extend to the end of the string. We can also use negative indices in slicing.

# ### Section 5: Functions <a name="fun"></a>
# 
# ---
# 
# We have already seen a few examples of **functions**: `len()`, `print()`, `set()`, and so on. These are so-called built-in functions, they are part of the Python stardard library. The standard library provides a wide range of basic functions, but virtually all non-trivial Python programs require the programmer to define her own functions.
# 
# The best way to think about functions is that they *encapsulate* a (small) task within the larger program. A stereotypical function 1) takes in data, 2) processes the data in some way, and 3) returns the desired result. 
# 
# Let's use the `len` function as an example. `len` takes in a sequence (a list or a string), calculates the amount of atomic elements in the sequence (i.e. its length) and returns the length. Not every function has to return anything, however. The `print` function prints out the data to standard output and doesn't return any value.
# 
# In the code cell below, we have implemented a function `ends_with`, which takes in two strings and returns `True` if `string1` ends in `string2`, and `False` if it doesn't. Look carefully at the syntax of defining a new function.

# In[ ]:

def ends_with(string1, string2):
    # Using len() and slicing we can get the
    # correct amount of letters from the end 
    # of the string
    string_end = string1[-len(string2):]

    return string_end == string2

print(ends_with("string", "ing"))


# Every function definition starts with the **def** statement. It consists of three parts:
# 
#     def ends_with(string1, string2):
#     (1)    (2)          (3)
#     
# 1. The keyword *def* signals the start of a function definition.
# 2. The second element is the function name
# 3. The parentheses after the name list the **arguments** the function takes in. In our example the function takes in two strings. 
# 
# The actual body of the function is indented with four spaces. This is where the task the function was designed to do is accomplished. The function body ends in a **return** statement. Whatever comes after return is the "result" we want to return to the function caller. In this case we return a boolean True/False depending on whether the condition was met or not.

# ---
# 
# **Ex 5.0.1** Define a function `starts_with(string, start)`, which returns `True` if the string starts with a specified substring and `False` otherwise. See the implementation of `ends_with` above for help. The `None` value is simply a placeholder return value.
# 
# ---

# In[ ]:

def starts_with(string1, string2):
    string_start = string1[:len(string2)]
    return string_start == string2

    # return None

print(starts_with("application", "app"))


# Below you see another example of a function. The function `is_son_of` returns `True` if `person1` is `person2`'s son. Notice how we can use other functions within a function (we call the functions `ends_with` and `starts_with` we defined above).

# In[ ]:

# The rule is: person1 is person2's son if person1's name 
# is person2's name plus "son": Peterson is the son of Peter
def is_son_of(person1, person2):
    condition1 = ends_with(person1, "son")
    condition2 = starts_with(person1, person2)
    
    # both conditions need to be met
    is_son = condition1 and condition2
    
    return is_son
    
is_son_of("Peterson", "Peter")


# ---
# 
# **Ex 5.0.2** Define two functions, `is_father_of(person1, person2)` and `is_daughter_of(person1, person2)`. `is_father_of` should return a boolean in a converse case to the function `is_son_of`. `is_daughter_of` should return a boolean similarly to the function `is_son_of` but the ending should be *dottir* instead of *son*.
# 
# ---

# In[ ]:

def is_father_of(person1, person2):
    return None

# Also define 'is_daughter_of' here


# ---
# 
# **Ex 5.0.3** Define a function `likes(person1, person2)` that returns `True` if `person1` likes `person2`. Feel free to invent your own rules. For example: `person1` likes `person2` only if `person2` is `person1`'s son. You can also define more functions that you can use as part of the `likes` function body.
# 
# ---

# In[ ]:



