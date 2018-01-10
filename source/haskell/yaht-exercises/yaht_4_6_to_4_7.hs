-- yaht_4_6_to_4_7.hs

module Main
    where

{-

Exercise 4.6 Write a datatype Tuple which can hold one, two, three or four
elements, depending on the constructor (that is, there should be four
constructors, one for each number of arguments). Also provide functions
tuple1 through tuple4 which take a tuple and return Just the value in that
position, or Nothing if the number is invalid (i.e., you ask for the tuple4
on a tuple holding only two elements).

-}

data Tuple a b c d = One a
                    |Two a b
                    |Three a b c
                    |Four a b c d

tuple1 (One a) = Just a
tuple1 (Two a b) = Just a
tuple1 (Three a b c) = Just a
tuple1 (Four a b c d) = Just a

tuple2 (One a) = Nothing
tuple2 (Two a b) = Just b
tuple2 (Three a b c) = Just b
tuple2 (Four a b c d) = Just b

{-

Exercise 4.7 Based on our definition of Tuple from the previous exercise,
write a function which takes a Tuple and returns either the value (if it’s
a one-tuple), a Haskell-pair (i.e., (’a’,5)) if it’s a two-tuple, a
Haskell-triple if it’s a three-tuple or a Haskell-quadruple if it’s a four-
tuple. You will need to use the Either type to represent this.

-}

main = do
    let tNum1 = One 1
    let tNum2 = Two 1 2
    let tNum3 = Three 1 2 3
    let tNum4 = Four 1 2 3 4
    putStrLn ("tuple1 is:" ++ show(tuple1 tNum1))
    -- todo why the follow line is error?

    -- putStrLn ("tuple2 is:" ++ show(tuple2 tNum1))
