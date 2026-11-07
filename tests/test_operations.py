from arithmp.parser import Parser
import pytest

def test_mul():
    parser = Parser()
    assert( parser.parse("3 * 4"))==12.0
    assert( parser.parse("3 * -1"))==-3.0

def test_add():
    parser = Parser()
    assert( parser.parse("3 + 4"))==7

def test_div():
    parser = Parser()
    assert( parser.parse("4 / 4"))==1.0
    with pytest.raises(ZeroDivisionError):
        parser.parse("4 / 0")

def test_sub():
    parser = Parser()
    assert( parser.parse("10 - 4"))==6.0
    assert( parser.parse("10 - -4"))==14.0


def test_mod():
    parser = Parser()
    assert( parser.parse("12 % 4"))==0.0
    assert( parser.parse("12 % 5"))==2.0
    with pytest.raises(ZeroDivisionError):
        parser.parse("0 % 0")



def test_abs():
    parser = Parser()
    assert( parser.parse("abs(-5)"))==5.0
    assert( parser.parse("abs(5)"))==5.0

def test_round():
    parser= Parser()
    assert(parser.parse("round(10.2)"))==10.0
    assert(parser.parse("round(10.6)"))==11.0

    


def test_variable():
    parser  = Parser()
    assert( parser.parse("a = 10"))==10.0
    assert(parser.parse("b = a * 2 "))==20.0
    assert(parser.parse("b = b +a" ))==30.0
    
