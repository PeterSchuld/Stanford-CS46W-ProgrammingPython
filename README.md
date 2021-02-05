# Stanford CS 46 W — Beginning Programming in Python: An Online Course -
Final Project of the Stanford Continuing Studies course. The eight-Week online course explores the world of programming by teaching students the fundamental syntax and meaning of the Python programming language.

Instructor:  Eli Lev, Technology Manager, Stanford Continuing Studies

### Final Assignment ###
Practical Python Programming for Automation of Repetitive Tasks. 
The goal of this project is to automate a manual process of budget categorization
of the Costco credit card.  

#### 1.2 Backstory ####
Your sibling Bob Smith heard that you were taking a programming course in Python
(you might have mentioned it on Twitter or something). So Bob emails you asking for
help on a budgeting problem. Here is a snippet of that email:

Ok so as you know I don't trust Intuit and their Quicken finance software. A few years
back I was burned by their software in that I would download statements (as qif or qex
or whatever the damn format was at the time) and use Quicken to categorize it. Then
one day I did my usual monthly Costco credit card statement download and Quicken
didn't work. It said something like "You need to use latest version of Quicken to do your
budget". I was so pissed that I swore to never use Quicken or any other proprietary
budgeting software (and don't get me started about Intuit and simplified tax forms).
Anyway, I love downloading those simple credit card CSVs of my monthly bill but
categorizing them is becoming a bear. Can you use your new found programming
knowledge to make the budget categorization process easier on me?

#### 1.3 Overview ####
The following section define the specification of the project as follow:

"Bob's current (manual) process of budget categorization" section: describes how Bob
does his budgeting categorization now. This section is the "customer's use case". It
should help provide context and put you in the customer's "shoes".

"Summary of project requirements": describes the solution to Bob's process in the form
of your project. It also describes what you need to hand in.
Note: you can find all files and folders mentioned in this document at the following
box.com address: https://app.box.com/s/up19papd1ec60vfqcp4yl7ss92q99xcd


#### 2. Bob's current (manual) process of budget categorization ####

2.1 Go to citi.com website and download latest statement transactions as csv file

2.2 Make a copy of csv file and opens it up in excel

2.4 Insert category column and other column headings

2.5 Put a category name for each row

2.6 Sort by category and put a "total for category" column

2.7 Add totals for each category and put it in "total for category column"


#### 3. Summary of project requirements ####
3.1 The Goal
The goal of this project is to automate Bob's manual process of budget categorization
of the Costco credit card. So basically your program should accept "costco-citi-visadue-
soon - bob copy.csv" as input and ultimately generate "budget monthly totals and
tracking.csv" as output. The "Details and suggestions..." section (below) will go over
the approach.

#### Note ####
The Python file 'PeterSchuld-version2' needs access to the csv file 'costco-citi-visa-due-soon - bob copy - sorted - with sparse categories' in the working directory. The program creates the new csv file 'budget-monthly-totals-and-tracking.csv'in the same directory. The aggregated sums in the output file are denomiated in USD but do not include currency specific signs and negative values are indicated by a minus sign (i.e. no "$" sign or "()" for negative values).

#### Textbook ####
(Required) Al Sweigart (2015): "Automate the Boring Stuff with Python", San Francisco, ISBN 978-1-59327-599-0 
