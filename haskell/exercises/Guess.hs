-- Guess.hs

module Main
    where
import System.Random

main = do
    num <- randomRIO (1::Int, 10)
    putStrLn "I'm thinding of a number between 1 and 10"
    doGuessing num

doGuessing num = do
    putStrLn "Enter you guess:"
    guess <- getLine
    let guessNum = read guess
    if guessNum < num
        then do
            putStrLn "Too low!"
            doGuessing num
        else if read guess > num
            then do
                putStrLn "Too high!"
                doGuessing num
            else do
                putStrLn "You Win!"
