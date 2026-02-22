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

def test_ones_if_a_number_not_is_one():
        d1 = 1
        d2 = 1
        d3 = 2
        d4 = 1
        d5 = 1

        expected = 4
        assert Yatzy.ones(d1,d2,d3,d4,d5) == expected

def test_twos():
        d1 = 2
        d2 = 2
        d3 = 2
        d4 = 2
        d5 = 2

        expected = 10
        assert Yatzy.twos(d1,d2,d3,d4,d5) == expected

def test_twos_if_a_number_not_is_two():
        d1 = 2
        d2 = 3
        d3 = 2
        d4 = 2
        d5 = 2

        expected = 8
        assert Yatzy.twos(d1,d2,d3,d4,d5) == expected

def test_threes():
        d1 = 3
        d2 = 3
        d3 = 3
        d4 = 3
        d5 = 3

        expected = 15
        assert Yatzy.threes(d1,d2,d3,d4,d5) == expected

def test_threes_if_a_number_not_is_three():
        d1 = 3
        d2 = 3
        d3 = 2
        d4 = 3
        d5 = 3
        
        expected = 12
        assert Yatzy.threes(d1,d2,d3,d4,d5) == expected

def test_fours():
        game = Yatzy(4,4,4,4,4)
        expected = 20
        assert game.fours() == expected

def test_fours_if_a_number_not_is_four():
        game = Yatzy(4,4,4,4,42)
        expected = 16
        assert game.fours() == expected


def test_fives():
        game = Yatzy(5,5,5,5,5)
        expected = 25
        assert game.fives() == expected

def test_fives_if_a_number_not_is_five():
        game = Yatzy(5,5,5,5,42)
        expected = 20
        assert game.fives() == expected


def test_sixes():
        game = Yatzy(6,6,6,6,6)
        expected = 30
        assert game.sixes() == expected

def test_sixes_if_a_number_not_is_six():
        game = Yatzy(6,6,6,6,42)
        expected = 24
        assert game.sixes() == expected


def test_score_pair_return_0():
        expected=0
        assert Yatzy.score_pair(1,2,3,4,5) == expected


def test_score_pair_return_6():
        expected=6
        assert Yatzy.score_pair(1,2,3,3,5) == expected

def test_score_pair_return_8():
        expected=8
        assert Yatzy.score_pair(1,2,4,4,5) == expected



def test_two_pair_return_0():
        expected=0
        assert Yatzy.two_pair(1,2,3,4,5) == expected


def test_two_pair_return_16():
        expected=16
        assert Yatzy.two_pair(2,2,6,6,5) == expected



def test_four_of_a_kind_return_0():
        expected=0
        assert Yatzy.four_of_a_kind(1,2,3,4,5) == expected


def test_four_of_a_kind_return_4():
        expected=8
        assert Yatzy.four_of_a_kind(2,2,2,2,5) == expected


def test_three_of_a_kind_return_0():
        expected=0
        assert Yatzy.three_of_a_kind(1,2,3,4,5) == expected


def test_three_of_a_kind_return_4():
        expected=6
        assert Yatzy.three_of_a_kind(2,1,2,2,5) == expected

def test_smallStraight_return_15():
        expected=15
        assert Yatzy.smallStraight(1,2,3,4,5) == expected


def test_smallStraight_return_0():
        expected=0
        assert Yatzy.smallStraight(2,1,2,2,5) == expected


def test_largeStraight_return_20():
        expected=20
        assert Yatzy.largeStraight(6,2,3,4,5) == expected


def test_largeStraight_return_0():
        expected=0
        assert Yatzy.largeStraight(2,1,2,2,5) == expected

def test_fullHouse_return_13():
        expected=13
        assert Yatzy.fullHouse(2,2,3,3,3) == expected


def test_fullHouse_return_0():
        expected=0
        assert Yatzy.fullHouse(2,1,2,2,5) == expected
