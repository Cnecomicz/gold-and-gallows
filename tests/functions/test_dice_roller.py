from flexmock import flexmock
import pytest

import gng.functions.dice_roller as dr

from gng.functions.dice_roller import (
	roll_above,
	roll_below,
	thread_the_needle
)

def test_thread_the_needle_extrema_always_fail():
	flexmock(dr).should_receive("roll_x_d_n").with_args(1,20).and_return(1)
	assert thread_the_needle(1,20) == False

def test_thread_the_needle_extrema_always_fail_2():
	flexmock(dr).should_receive("roll_x_d_n").with_args(1,20).and_return(20)
	assert thread_the_needle(1,20) == False

def test_roll_above_fails_on_1():
	flexmock(dr).should_receive("roll_x_d_n").with_args(1,20).and_return(1)
	assert roll_above(1) == False

def test_roll_below_fails_on_20():
	flexmock(dr).should_receive("roll_x_d_n").with_args(1,20).and_return(20)
	assert roll_below(20) == False