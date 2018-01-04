-- learn haskell 99 questions 21-28
-- website: https://wiki.haskell.org/99_questions/21_to_28

{-
 1 Problem 21


Insert an element at a given position into a list.

Example:

* (insert-at 'alfa '(a b c d) 2)
(A ALFA B C D)

Example in Haskell:

P21> insertAt 'X' "abcd" 2
"aXbcd"

Solution 1:

insertAt :: a -> [a] -> Int -> [a]
insertAt x xs n = take n xs ++ x:(drop n xs)
-}

insertAt :: a -> [a] -> Int -> [a]
insertAt x ys     1 = x:ys
insertAt x (y:ys) n = y:insertAt x ys (n-1)

{-
 2 Problem 22

Create a list containing all integers within a given range.

Example:

* (range 4 9)
(4 5 6 7 8 9)

Example in Haskell:

Prelude> range 4 9
[4,5,6,7,8,9]
-}

range :: Int -> Int -> [Int]
range x y
    | x == y = [x]
    | x < y = x:(range (x+1) y)
    | otherwise = x:(range (x-1) y)

{-
 3 Problem 23

Extract a given number of randomly selected elements from a list.

Example:

* (rnd-select '(a b c d e f g h) 3)
(E D A)

Example in Haskell:

Prelude System.Random>rnd_select "abcdefgh" 3 >>= putStrLn
eda
-}
