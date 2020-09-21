--- property 'esCero::Int->Bool' ---
prop_esCero :: Int -> Bool
prop_esCero n = ( esCero n ) == ( n == 0 )


--- property 'esPositivo::Int->Bool' ---
prop_esPositivo :: Int -> Bool
prop_esPositivo n = ( esPositivo n ) == ( n>=0 )


--- property 'esVocal::Char->Bool' ---
prop_esVocal :: Char -> Bool
prop_esVocal c = ( esVocal c ) == ( c `elem` "aeiou" )


--- property 'paratodo::[Bool]->Bool' ---
prop_paratodo :: [Bool] -> Bool
prop_paratodo xs = ( paratodo xs ) == ( sum [1 |x<-xs, x == True] == length xs)


--- property 'sumatoria::[Int]->Int' ---
prop_sumatoria :: [Int] -> Bool
prop_sumatoria xs = ( sumatoria xs ) == ( sum xs )


--- property 'productoria::[Int]->Int' ---
prop_productoria :: [Int] -> Bool
prop_productoria xs = ( productoria xs ) == ( product xs )


--- property 'factorial::Int->Int' OJO porque explota---
prop_factorial :: Int -> Bool
prop_factorial 6 = ( factorial 6 ) == ( myfac 6)
    where myfac n   | n==0 = 1
                    |otherwise = n * myfac n-1


--- property 'promedio::[Int]->Int' ---
prop_promedio :: [Int] -> Bool
prop_promedio xs = ( promedio xs ) == (if length xs == 0 then 0 else sum xs `div` length xs)


--- property 'pertenece::Int->[Int]->Bool' ---
prop_pertenece :: Int -> [Int] -> Bool
prop_pertenece n xs = ( pertenece n xs ) == ( n `elem` xs )
