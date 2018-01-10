-- yaht_5_1.hs

module Main
    where

{-

Exercise 5.1 Write a program that asks the user for his or her name. If the
name is one of Simon, John or Phil, tell the user that you think Haskell is
a great programming language. If the name is Koen, tell them that you think
debugging Haskell is fun (Koen Classen is one of the people who works on
Haskell debugging); otherwise, tell the user that you don’t know who he or
she is. Write two different versions of this program, one using if
statements, the other using a case statement.


main = do
    putStrLn "Please tell me your name:"
    name <- getLine
    if elem name ["Simon", "John", "Phil"]
        then putStrLn "Haskell is a great programming language."
        else if name == "Koen"
            then putStrLn "debugging Haskell is fun"
            else putStrLn "I know who are you."

-}
main = do
    putStrLn "Please tell me your name:"
    name <- getLine
    case name of
        "Koen" -> putStrLn "debugging Haskell is fun"
        "Simon" -> putStrLn "Haskell is a great programming language."
        "John" -> putStrLn "Haskell is a great programming language."
        "Phil" -> putStrLn "Haskell is a great programming language."
        _ -> putStrLn "I know who are you."
