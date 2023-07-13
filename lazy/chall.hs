import Data.Bits
import Data.Char
import System.IO

printAscii :: [Char] -> IO ()
printAscii [ch] = do
  putStr (show (ord ch))
  putStrLn ""
printAscii (ch:str) = do
  putStr (show (ord ch) ++ " ")
  printAscii str

rev :: String -> String
rev = reverse

cipher :: String -> String
cipher = map caesarChar
  where
    caesarChar c
      | isUpper c = chr ((ord c - ord 'A' + 10) `mod` 26 + ord 'A')
      | isLower c = chr ((ord c - ord 'a' + 10) `mod` 26 + ord 'a')
      | otherwise = c

rot13 :: String -> String
rot13 = map rot13Char
  where
    rot13Char c
      | isUpper c = chr ((ord c - ord 'A' + 13) `mod` 26 + ord 'A')
      | isLower c = chr ((ord c - ord 'a' + 13) `mod` 26 + ord 'a')
      | otherwise = c

enc_xor :: String -> String
enc_xor flag = map (\c -> chr (ord c `xor` key)) flag
  where key = 7

encrypt :: String -> String
encrypt = rev . cipher . rot13 . enc_xor 

main :: IO ()
main = do
  flag <- readFile "flag.txt"

  let encryptedText = encrypt flag
  putStr ("Enter your name: ")
  hFlush stdout 
  userInput <- getLine   
  putStrLn ("Hello " ++ userInput ++ ", this is your flag: ") 
  printAscii encryptedText