Haskell Exercises
=================

:date: 2017-02-01
:slug: haskell-exercises
:tags: exerciese
:category: haskell
:author: Dormouse Young

Guess Number
------------
This module first set a random number, then get input number. If input
number is smaller than the random number, then show "Too low!". If input
number is bigger than the random number, then show "Too high". If input
number equal to the random number, then quit.

.. literalinclude:: exercises/Guess.hs
   :language: haskell


IO execises
-----------

A program that will repeatedly ask the user for numbers until she types in
zero, at which point it will tell her the sum of all the numbers, the product
of all the numbers, and, for each number, its factorial. For instance, a
session might look like::

    Give me a number (or 0 to stop):
    5
    Give me a number (or 0 to stop):
    8
    Give me a number (or 0 to stop):
    2
    Give me a number (or 0 to stop):
    0
    The sum is 15
    The product is 80
    5 factorial is 120
    8 factorial is 40320
    2 factorial is 2

Here is the code:

.. literalinclude:: exercises/Io_execises.hs
   :language: haskell



