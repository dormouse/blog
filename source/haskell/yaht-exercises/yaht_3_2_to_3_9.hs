
-- Yet Another Haskell Tutorial Exercises
import Data.Char

myMax :: Int -> Int -> Int
myMax x y
    | x > y = x
    | otherwise = y

myMaximum :: [Int] -> Int
myMaximum [] = 0
myMaximum (x:xs) = foldl myMax 0 (x:xs)

myFab :: Int -> Int
myFab x
    | x <= 0    = 0
    | x < 3     = 1
    | otherwise = myFab (x - 1) + myFab (x - 2)

mult :: Int -> Int -> Int
mult 0 y = 0
mult x y = y + mult (x - 1) y

myMap :: (a -> b) -> [a] -> [b]
myMap f [] = []
myMap f (x:xs) = f x:myMap f xs

main = do

{-
Exercise 3.2 Use a combination of fst and snd to extract the character out
of the tuple ((1,’a’),"foo").
-}

    (putStrLn.show) (snd(fst ((1,'a'),"foo")))

{-
Exercise 3.3 Use map to convert a string into a list of booleans, each
element in the new list representing whether or not the original element
was a lower-case character. That is, it should take the string “aBCde” and
return [True,False,False,True,True].
-}

    (putStrLn.show) (map isUpper "aBCde")

{-
Exercise 3.4 Use the functions mentioned in this section (you will need two
of them) to compute the number of lower-case letters in a string. For
instance, on “aBCde” it should return 3.
-}

    (putStrLn.show) (length(filter isLower "aBCde"))

{-
Exercise 3.5 We’ve seen how to calculate sums and products using folding
functions. Given that the function max returns the maximum of two numbers,
write a function using a fold that will return the maximum value in a list
(and zero if the list is empty). So, when applied to [5,10,2,8,1] it will
return 10. Assume that the values in the list are always ≥ 0. Explain to
yourself why it works.
-}

    (putStrLn.show) (myMaximum [5,10,2,8,1])

{-
Exercise 3.6 Write a function that takes a list of pairs of length at least
2 and returns the first component of the second element in the list. So,
when provided with [(5,’b’),(1,’c’),(6,’a’)], it will return 1.

fst(last(take 2 [(5,'b'),(1,'c'),(6,'a')]))

-}
    (putStrLn.show) (fst(last(take 2 [(5,'b'),(1,'c'),(6,'a')])))

{-
Exercise 3.7 The fibonacci sequence is defined by: f =1 n = 1 or n = 2 F
n = F n−2 + F n−1 otherwise Write a recursive function fib that takes a
positive integer n as a parameter and calculates F n .
-}

    (putStrLn.show) (myFab 4)

{-
Exercise 3.8 Define a recursive function mult that takes two positive
integers a and b and returns a*b, but only uses addition (i.e., no fair
just using multiplication). Begin by making a mathematical definition in
the style of the previous exercise and the rest of this section.
-}

    (putStrLn.show) (mult 5 4)

{-
Exercise 3.9 Define a recursive function my map that behaves identically to
the standard function map.
-}

    (putStrLn.show) (myMap sqrt [4,16,25])
