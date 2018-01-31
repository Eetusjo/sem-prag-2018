
# coding: utf-8

# # Semantics and pragmatics
# ## Lab session 1
# 
# The purpose of this lab is to learn the basics of Python programming. Some of the exercises will be general in nature (as in not directly related to language technology), but try to always relate the programming concepts to what we learned during the first LT lecture.
# 
# The following concepts will be introduced in this lab:
# 
# * [Variables and assignment](#vars)
# * [Conditionals and boolean logic](#conbo)
# * [Indentation](#indent)
# * [Strings](#string)
# * [Lists and sets](#lists)
# * [Indexing, slicing, and dicing](#slicedice)
# * [Functions](#fun)
# 
# Without further ado, let's get into it.

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
# Try out some calculations on the cell below. Write the expression you want to evaluate and press `Ctrl + Enter` to execute. You should see something like this:
# 
#     In []: 8/2
#     Out[]: 4.0
#     
# Note: When writing complex expressions, it is often helpful (and/or necessary) to include parentheses. These work exactly as in our regular mathematical notation: 
# 
#     In []: (8+2)/5
#     Out[]: 2.0
# 
# You can also include spaces between numbers and operators to make the expression more readable.

# In[ ]:

8/2


# You probably now feel confident in executing code cells in this notebook. In order to do something more substantial than calculating basic math expressions, we now dive into basic programming. The concepts introduced are really "Programming 101", and mostly independent of the language used. If you already have some background in programming, this lab should be a breeze. If you have never programmed before, Python with its simple and clean syntax is definitely a great way to get started.

# ### Section 1: Variables, assignment and strings <a name="vars"></a>
# ---
# #### 1.1. Variables and assignment
# 
# **TODO**
# 
# #### 1.2. Strings and data types
# 
# In the Preparation section we mentioned that you can consider a string as something akin to a piece of text. More accurately, a string (**`str`** in Python) is a *sequence of characters*. It is one of the basic *data types*, and for obvious reasons, one that we as students of LT are very interested in. Another basic data type would be **`int`**, representing integer numbers. You already worked with `ints` above when you did some math. We will introduce more data types along the way; for now, let's make sure the difference between `str` and `int` is clear.
# 
# As you saw above, `strs` are surrounded by double quotation marks (in fact single quotes work too):
# 
#     Option 1:    city = "Berlin"
#     Option 2:    city = 'Berlin'
#     
# `ints`, however, are written as plain numbers, without quotation marks, or anything else for that matter. 
# 
#     year = 2049
#     
# **Ex 1.2.1** Run the cell below and inspect the output. What went wrong? Correct the code and you might figure out the meaning of life (and see why it's important to keep in mind the distinction between `strs` and `ints`)

# In[ ]:

paradise = "1984"
(300 + 404 + paradise)/64


# Clearly the original addition didn't work out all too well. Though you can't add together a `str` and an `int`, confusingly enough, the "addition" (+) does actually work for two or more `strs`. 
# 
# **Ex 1.2.2** Try adding together some `strs` in the cell below and figure out what the operator does in this case.

# In[ ]:




# In the case of the `+` operator with strings we talk about **concatenation** and not addition.
# 
# Finally, to recap some of the things we learned in this section, let's put the ideas together. If you run the code cell below you will get some error messages again. The code is trying to print out the variable `'you'` but we forgot a piece of code. 
# 
# **Ex 1.2.3** Add a line of code where you initialize the variable with some (string) value and try again.

# In[ ]:

print("What's your name?")


print("I am talking to", you)


# As you see we can write multiple things inside the parentheses of the `print` function, separated by commas. We are allowed to use things other than strings in print statements as well. 
# 
# **Ex 1.2.4** Runs the first cell below. In the second code cell, change the variable '`abrahams_age`' from string to `int` and try to figure out how to print out the same text as in the first cell. You might have to discard the whole variable '`sentence`'.

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


# ### Conditionals and boolean logic <a name="conbo"></a>
# 
# * Indentation
# * basic string processing (case)
# 
# ---

# In[ ]:




# ### Lists and sets <a name="lists"></a>

# In[ ]:




# ### Indexing, slicing, and dicing <a name="slicedice"></a>

# In[ ]:




# ### Functions <a name="fun"></a>
