-- ejercicio 1
esCero :: Int -> Bool
esCero a = (a==0)

esPositivo :: Int->Bool
esPositivo a = (a > 0)

esVocal :: Char->Bool
esVocal c = (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')

-- ejercicio 2
paratodo :: [Bool] -> Bool
paratodo []     = True
paratodo (x:xs) = x && paratodo xs

sumatoria :: [Int] -> Int
sumatoria []    = 0
sumatoria (x:xs)    = x + sumatoria xs

productoria :: [Int] -> Int
productoria []      = 1
productoria (x:xs)  = x * productoria xs

factorial :: Int -> Int
factorial 0    = 1
factorial e    = e * factorial (e-1)

promedio :: [Int] -> Int
promedio xs = sumatoria xs `div` length xs

-- ejercicio 3
pertenece :: Int -> [Int] -> Bool
pertenece _ []  = False
pertenece e (x:xs)  = (e==x) || pertenece e xs

-- ejercicio 4
paratodo' :: [a] -> (a->Bool) -> Bool
paratodo' [] _      = True
paratodo' (x:xs) p  = p x && paratodo' xs p

    -- equivalencia de cuantificador existe y paratodo
existe' :: [a] -> (a->Bool) -> Bool
existe' xs p  = not (paratodo' xs (not .p))

existe'' :: [a] -> (a->Bool) -> Bool
existe'' [] _      = False
existe'' (x:xs) p  = p x || existe'' xs p

sumatoria' :: [a] -> (a->Int) -> Int
sumatoria' [] _     = 0
sumatoria' (x:xs) f = f x + sumatoria' xs f

largo :: [Int] -> Int
largo [] = 0
largo (_:xs) = 1 + largo xs

productoria' :: [a] -> (a->Int) -> Int
productoria' [] _ = 1
productoria' (x:xs) f = f x * productoria' xs f

-- ejercicio 5
paratodo'' :: [Bool] -> Bool
paratodo'' xs  = paratodo' xs id

-- ejercicio 6
todosPares :: [Int] -> Bool
todosPares [] = True
todosPares (x:xs) = (x `mod` 2 == 0) && todosPares xs

todosPares' :: [Int] -> Bool
todosPares' xs = paratodo' xs even

hayMultiplo :: Int -> [Int] -> Bool
hayMultiplo _ [] = False
hayMultiplo a (x:xs) = (x `mod` a == 0) || hayMultiplo a xs

hayMultiplo' :: Int -> [Int] -> Bool
hayMultiplo' a xs = existe' xs (\x -> x `mod` a == 0)

sumaCuadrados :: Int -> Int
sumaCuadrados a = sumatoria' [0..a] (\x -> x*x)

factorial' :: Int -> Int
factorial' a = productoria' [1..a] id

factorial'' :: Int -> Int
factorial'' a = productoria [1..a]

multiplicaPares :: [Int] -> Int
multiplicaPares xs = productoria (filter even xs)

-- ejercicio 8
duplicar :: [Int] -> [Int]
duplicar [] = []
duplicar (x:xs) = x*2 : duplicar xs

duplicar' :: [Int] -> [Int]
duplicar' xs = map (* 2) xs

-- ejercicio 9
solopares :: [Int] -> Int
solopares [] = 1
solopares (x:xs)    | (x `mod` 2 == 0) = x * solopares xs
                    | otherwise = solopares xs

solopares' :: [Int] -> Int
solopares' xs = multiplicaPares xs

-- ejercicio  10
primIgualesA :: (Eq a) => a -> [a] -> [a]
primIgualesA _ [] = []
primIgualesA a (x:xs)   | (a==x) = x : primIgualesA a xs
                        | otherwise = []

primIgualesA' :: (Eq a) => a -> [a] -> [a]
primIgualesA' a xs = takeWhile (==a) xs


-- ejercicio 11
primIguales :: (Show a, Eq a) => [a] -> [a]
primIguales [] = []::[a]
primIguales [x] = [x]
primIguales (x:xs)  | (x == head xs) = x : primIguales xs
                    | otherwise = [x]
