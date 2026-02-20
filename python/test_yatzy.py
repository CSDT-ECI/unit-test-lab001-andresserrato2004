from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


def test_demo():
        expected = 15
        actual = 15
        assert expected == actual        


def test_chance():

        d1 = 2
        d2 = 2
        d3 = 2
        d4 = 2
        d5 = 2
        expected = 10

        assert Yatzy.chance(d1,d2,d3,d4,d5) == expected

def test_yatzy_return_50():
        arr = [1,1,1,1,1]
        expected = 50
        
        assert Yatzy.yatzy(arr) == expected

def test_yatzy_return_0():
        arr = [1,1,1,2,1]
        expected = 0
        
        assert Yatzy.yatzy(arr) == expected

def test_ones():
        d1 = 1
        d2 = 1
        d3 = 1
        d4 = 1
        d5 = 1

        expected = 5

        assert Yatzy.ones(d1,d2,d3,d4,d5) == expected


def test_threes():
        d1 = 2
        d2 = 2
        d3 = 2
        d4 = 2
        d5 = 2

        expected = 10

        assert Yatzy.twos(d1,d2,d3,d4,d5) == expected

def test_fours():
        d1 = 3
        d2 = 3
        d3 = 3
        d4 = 3
        d5 = 3

        expected = 15

        assert Yatzy.threes(d1,d2,d3,d4,d5) == expected

