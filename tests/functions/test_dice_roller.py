from flexmock import flexmock
import pytest

import gng.functions.dice_roller as dr

from gng.functions.dice_roller import (
	roll_above,
	roll_below,
	thread_the_needle,
	roll_usage,
	roll,
	UnexpectedDiceSyntax,
)

def test_thread_the_needle_extrema_always_fail():
	flexmock(dr).should_receive("roll_x_d_n").with_args(1,20).and_return(1).once()
	assert thread_the_needle(1,20) == False

def test_thread_the_needle_extrema_always_fail_2():
	flexmock(dr).should_receive("roll_x_d_n").with_args(1,20).and_return(20).once()
	assert thread_the_needle(1,20) == False

def test_roll_above_fails_on_1():
	flexmock(dr).should_receive("roll_x_d_n").with_args(1,20).and_return(1).once()
	assert roll_above(1) == False

def test_roll_below_fails_on_20():
	flexmock(dr).should_receive("roll_x_d_n").with_args(1,20).and_return(20).once()
	assert roll_below(20) == False

def test_roll_usage_downgrades_on_1():
	flexmock(dr).should_receive("roll_x_d_n").with_args(1,20).and_return(1).once()
	assert roll_usage(20) == 12

def test_roll_usage_downgrades_on_2():
	flexmock(dr).should_receive("roll_x_d_n").with_args(1,20).and_return(2).once()
	assert roll_usage(20) == 12

def test_roll_usage_downgrade_track_is_20_12_10_8_6_4_None():
	flexmock(dr).should_receive("roll_x_d_n").with_args(1,20).and_return(1).once()
	flexmock(dr).should_receive("roll_x_d_n").with_args(1,12).and_return(1).once()
	flexmock(dr).should_receive("roll_x_d_n").with_args(1,10).and_return(1).once()
	flexmock(dr).should_receive("roll_x_d_n").with_args(1,8).and_return(1).once()
	flexmock(dr).should_receive("roll_x_d_n").with_args(1,6).and_return(1).once()
	flexmock(dr).should_receive("roll_x_d_n").with_args(1,4).and_return(1).once()
	assert roll_usage(20) == 12
	assert roll_usage(12) == 10
	assert roll_usage(10) == 8
	assert roll_usage(8) == 6
	assert roll_usage(6) == 4
	assert roll_usage(4) == None

def test_usage_exception():
	with pytest.raises(UnexpectedDiceSyntax):
		roll_usage("u5")



def test_roll_can_parse_xdn():
	flexmock(dr).should_receive("roll_x_d_n").with_args(3,6).and_return(10).once()
	assert roll("3d6") == 10

def test_roll_can_parse_xdn_when_x_and_n_are_multiple_digits():
	flexmock(dr).should_receive("roll_x_d_n").with_args(10,20).and_return(10).once()
	assert roll("10d20") == 10


def test_roll_can_parse_dn():
	flexmock(dr).should_receive("roll_x_d_n").with_args(1,6).and_return(3).twice()
	assert roll("d6") == 3
	assert roll("1d6") == 3

def test_roll_can_parse_xdnkk():
	flexmock(dr).should_receive("roll_x_d_n_and_keep_highest_k").with_args(3,6,2).and_return(7).once()
	assert roll("3d6k2") == 7

def test_roll_can_parse_xdn_when_x_n_and_k_are_multiple_digits():
	flexmock(dr).should_receive("roll_x_d_n_and_keep_highest_k").with_args(15,20,10).and_return(10).once()
	assert roll("15d20k10") == 10

def test_roll_cannot_xdnkk_if_x_is_1():
	with pytest.raises(UnexpectedDiceSyntax):
		roll("1d6k1")
		roll("d6k1")

def test_but_roll_can_xdnkk_if_x_is_10():
	flexmock(dr).should_receive("roll_x_d_n_and_keep_highest_k").with_args(10,6,2).and_return(7).once()
	assert roll("10d6k2") == 7

def test_roll_understands_usage_syntax():
	flexmock(dr).should_receive("roll").with_args("d20").and_return(1).once()
	assert roll("u20") == "u12"



def test_roll_raises_exception_on_unexpected_syntax():
	with pytest.raises(UnexpectedDiceSyntax):
		roll("hello world")
