--- property 'esCero::Int->Bool' ---
prop_esCero :: Int -> Bool
prop_esCero n = ( esCero n ) == ( n==0 )


--- property 'esPositivo::Int->Bool' ---
prop_esPositivo :: Int -> Bool
prop_esPositivo n = ( esPositivo n ) == ( n>=0 )


--- property 'esVocal::Char->Bool' ---
prop_esVocal :: Char -> Bool
prop_esVocal c = ( esVocal c ) == ( c `elem` "aeiou" )


--- property 'paratodo::[Bool]->Bool' ---
prop_paratodo :: [Bool] -> Bool
prop_paratodo xs = ( paratodo xs ) == ( sum [1|x<-xs, x==True] == length xs )


--- property 'sumatoria::[Int]->Int' ---
prop_sumatoria :: [Int] -> Bool
prop_sumatoria xs = ( sumatoria xs ) == ( sum xs )
