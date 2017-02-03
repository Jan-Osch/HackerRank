module TextAlignJustify where
import           Test.Hspec

justify :: String -> Int -> String
justify text width = joinLines joined
  where
    worded = words text
    linesArray = splitLines "" width width worded
    separated = map words $ lines linesArray
    joined = adjustWidth separated width

joinLines :: [String] -> String
joinLines [] = []
joinLines  [candidate] = candidate
joinLines  (candidate:rest) = candidate ++ "\n" ++ joinLines rest

adjustWidth ::[[String]] -> Int -> [String]
adjustWidth [] _ = []
adjustWidth [candidate] _ = [unwords candidate]
adjustWidth (candidate:rest) width = addSpaces candidate width : adjustWidth rest width

splitLines :: String -> Int -> Int -> [String] -> String
splitLines result _ _ [] = result
splitLines "" _ width (candidate:rest) =
  splitLines candidate newRemaining width rest
  where
    newRemaining = width - (length candidate +1)
splitLines result remaining width (candidate:rest) =
  splitLines newResult newRemaining width rest
  where
    willFit = length candidate <= remaining
    newResult = if willFit
      then result ++ " "  ++ candidate
      else result ++ "\n" ++ candidate
    newRemaining = if willFit
      then remaining - (length candidate +1)
      else width - (length candidate +1)

characterLength :: [String] -> Int
characterLength = sum . map length

addSpaces :: [String] -> Int -> String
addSpaces results width = interSpace results regular bigger
  where
    missing = width - characterLength results
    regular = missing `div` (length results -1)
    bigger = missing `mod` (length results -1)

interSpace :: [String] -> Int -> Int -> String
interSpace [] _ _ = []
interSpace [x] _ _ = x
interSpace (first:rest) regular bigger
  | bigger > 0 = first ++ spaces (regular + 1) ++ interSpace rest regular (bigger-1)
  | otherwise = first ++ spaces regular ++ interSpace rest regular bigger
  where
    spaces n = replicate n ' ';

main :: IO ()
main = hspec $
  describe "justify" $ do
    it "justify #1"
      $ do justify "123 45 6" 6 `shouldBe` "123 45\n6"
    it "justify #2"
        $ do justify "Lorem  ipsum  dolor  sit amet, consectetur  adipiscing  elit. Vestibulum" 30 `shouldBe` "Lorem  ipsum  dolor  sit amet,\nconsectetur  adipiscing  elit.\nVestibulum"

    it "splitLines #1"
      $ do splitLines "" 4 4 ["ABC", "AB", "C", "AB", "AB"] `shouldBe` "ABC\nAB C\nAB\nAB"

    it "interSpace"
      $ do interSpace ["X", "X", "X", "X"]  2 1 `shouldBe` "X   X  X  X"

    it "addSpaces #1"
      $ do addSpaces ["X", "X", "X", "X"]  7 `shouldBe` "X X X X"
    it "addSpaces #2"
      $ do addSpaces ["X", "X", "X", "X"]  9 `shouldBe` "X  X  X X"
    it "addSpaces #3"
      $ do addSpaces ["X"]  9 `shouldBe` "X"
    it "addSpaces #4"
      $ do addSpaces ["X", "X"] 5 `shouldBe` "X   X"
