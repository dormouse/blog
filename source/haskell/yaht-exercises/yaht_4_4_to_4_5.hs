-- yaht_4_4_to_4_5.hs

module Main
    where

{-
Exercise 4.4 Write a data type declaration for Triple, a type which
contains three elements, all of different types. Write functions tripleFst,
tripleSnd and tripleThr to extract respectively the first, second and third
elements.
-}
data Triple a b c = Triple a b c
tripleFst (Triple a b c) = a
tripleSnd (Triple a b c) = b
tripleThr (Triple a b c) = c

{-
Exercise 4.5 Write a datatype Quadruple which holds four
elements. However, the first two elements must be the same type and the
last two elements must be the same type. Write a function firstTwo which
returns a list containing the first two elements and a function lastTwo
which returns a list containing the last two elements. Write type
signatures for these functions
-}
data Quadruple a b = Quadruple a a b b

firstTwo:: Quadruple a b -> [a]
firstTwo (Quadruple a b c d) = [a, b]

lastTwo:: Quadruple a b -> [b]
lastTwo (Quadruple a b c d) = [c, d]

main = do
    let tNum = Triple 1 2 3
    putStrLn ("tripleFst is:" ++ show(tripleFst tNum))
    putStrLn ("tripleSnd is:" ++ show(tripleSnd tNum))
    putStrLn ("tripleThr is:" ++ show(tripleThr tNum))

    let qNum = Quadruple 1 2 3 4
    putStrLn ("Quadruple firstTwo is:" ++ show(firstTwo qNum))
    putStrLn ("Quadruple lastTwo is:" ++ show(lastTwo qNum))

