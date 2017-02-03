import Test.Hspec

lcs :: String -> String -> String
lcs "" _ = ""
lcs _ "" = ""
lcs (a:left) (b:right)
  | a == b = a : lcs left right
  | otherwise = longest
    where
      leftLcs = lcs left (b:right)
      rightLcs = lcs (a:left) right
      longest = longer leftLcs rightLcs

longer :: String -> String -> String
longer left right = if length left > length right
    then left
    else right

main = hspec $ do
  describe "lcs" $ do
    it "should work on some examples" $ do
      lcs "a"         "b"         `shouldBe` ""
      lcs "abcdef"    "abc"       `shouldBe` "abc"
      lcs "132535365" "123456789" `shouldBe` "12356"
      lcs "1234" "133456789" `shouldBe` "134"
