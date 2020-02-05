from trytopackage import myModule
def test_myFibonacci():
    """Makes sure function works properly"""
  assert myModule.myFibonacci(1) == 1, 'incorrect'
  assert myModule.myFibonacci(2) == 1, 'incorrect'
  assert myModule.myFibonacci(3) == 2, 'incorrect'
  
