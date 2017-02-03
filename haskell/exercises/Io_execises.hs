-- Io_execises.hs


askForNum = do
    putStrLn "Give me a number (or 0 to stop):"
    num <- getLine
    let number = read num :: Int
    if number == 0
        then return []
    else do
        rest <- askForNum
        return (number:rest)


my_product [] = 1
my_product (x:xs) = x * product(xs)


my_factorial 1 = 1
my_factorial n = n * my_factorial(n-1)


show_factorial x = putStrLn(show(x) ++ " factorial is " ++ show(my_factorial x))


main = do
    nums <- askForNum
    let a = head nums
    putStrLn("The sum is " ++ show(sum(nums)))
    putStrLn("The product is " ++ show(my_product nums))
    mapM show_factorial nums
