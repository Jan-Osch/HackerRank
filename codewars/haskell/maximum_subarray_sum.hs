module MaxSequence where
import           Test.Hspec

-- Return the greatest subarray sum within the array of integers passed in.
maxSequence :: [Int] -> Int
maxSequence list =  res
 where
   (res, _, _ ) = foldingFunciton list

foldingFunciton :: [Int] -> (Int, Int,Int)
foldingFunciton [] = (0,0,0)
foldingFunciton (first:rest) = (newResult, newSmallest, summed)
  where
    (result, smallest, soFar) = foldingFunciton rest
    summed = soFar + first
    newSmallest = min smallest soFar
    candidateResult = summed - newSmallest
    newResult = max candidateResult result

main = hspec $ do
  describe "maxSequence" $ do
    it "Should work on empty list "
      $ do maxSequence [] `shouldBe` 0
    it  "Should work for the example"
      $ do maxSequence input3 `shouldBe` expected3
    it  "Should work for a one element list"
      $ do maxSequence [-1] `shouldBe` 0
    it  "Should work for a one element list with positive elements"
      $ do maxSequence [8] `shouldBe` 8
    it  "Should work for all positive elements"
      $ do maxSequence [2,1,1,2] `shouldBe` 6
    it  "Should work for all negative elements"
      $ do maxSequence [-2,-1,-1,-2] `shouldBe` 0
    it  "case #1"
      $ do maxSequence [-1,2] `shouldBe` 2
    it  "case #2"
      $ do maxSequence [1,-1] `shouldBe` 1

    where
      input3     = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
      expected3  = 6
