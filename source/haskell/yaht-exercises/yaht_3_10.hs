-- yaht_3_10.hs

{-

Exercise 3.10 Write a program that will repeatedly ask the user for numbers
until she types in zero, at which point it will tell her the sum of all the
numbers, the product of all the numbers, and, for each number, its
factorial. For instance, a session might look like:

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

Hint: write an IO action that reads a number and, if it’s zero, returns the
empty list. If it’s not zero, it recurses itself and then makes a list out
of the number it just read and the result of the recursive call.

-}

module Main
    where
import System.Random

my_factorial :: Int -> Int
my_factorial 1 = 1
my_factorial x = x * my_factorial (x - 1)

my_product :: [Int] -> Int
my_product [] = 1
my_product (x:xs) = x * my_product xs

main = do
    nums <- askForNum
    putStrLn ("The sum is " ++ show(sum nums))
    putStrLn ("The product is " ++ show(my_product nums))
    showFactorial nums

askForNum = do
    putStrLn "Give me a number (or 0 to stop):"
    lineNum <- getLine
    let num = read lineNum
    if num == 0
        then return []
        else do
            rest <- askForNum
            return (num : rest)

showFactorial (x:xs) = do
    putStrLn (show(x) ++ " factorial is " ++ show(my_factorial x))
    if xs /= []
        then showFactorial xs
        else putStrLn ""

