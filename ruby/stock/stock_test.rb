require 'minitest/autorun'
require 'minitest/spec'

require './stock'

describe Stock do
  it "returns [0, 0] on a one element array" do
    Stock.best_transaction([5]).must_equal [0, 0]
  end

  it "returns [0, 1] with ascending array of size two" do
    Stock.best_transaction([1,3]).must_equal [0, 1]
  end

  it "returns [0, 2] when first and last of 3 element array is the best" do
    Stock.best_transaction([1,2,3]).must_equal [0, 2]
  end

  it "returns [0, 1] when the first and middle of 3 element array is the best" do
    Stock.best_transaction([1,3,2]).must_equal [0, 1]
  end

  it "returns [2, 3] when a later buy opportunity is better with 4 elements" do
    Stock.best_transaction([2,3,1,4]).must_equal [2, 3]
  end

  it "returns [2, 3] when the highest sell price is not the best" do
    Stock.best_transaction([4,5,1,3]).must_equal [2, 3]
  end

  it "returns [2, 3] when neither the highest nor lowest prices are best" do
     Stock.best_transaction([4, 6, 2, 5, 1, 3]).must_equal [2, 3]
  end
end
