from exercise2 import evaluate
 

def test_for_single_operand():
    assert evaluate("5") ==5

def test_for_add():
    assert evaluate("67+") == 13
    