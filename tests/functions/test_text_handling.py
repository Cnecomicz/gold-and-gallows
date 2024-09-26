from flexmock import flexmock
import pytest
import pygame

import gng.global_constants as gc

from gng.functions.text_handling import (
    TextBundle,
    bdlr,
    make_text,
    make_hovered_option,
    get_number_of_lines,
    make_all_options,
)

@pytest.fixture
def bgcolor_left_top_text_width():
    return (0, 0, 0), 10, 10, 1000

def test_TextBundle_has_default_args():
    bundle = TextBundle("text")
    assert bundle.font == gc.BASIC_FONT \
        and bundle.color == gc.TEXT_COLOR \
        and bundle.font_size == gc.FONT_SIZE

def test_bdlr_returns_TextBundle():
    bundle = bdlr("text")
    assert type(bundle) == TextBundle

def test_make_text_handles_newline_characters(bgcolor_left_top_text_width):
    DISPLAY_SURF = flexmock() 
    flexmock(DISPLAY_SURF).should_receive("blit").times(2)
    bundle = bdlr("text \n text")
    make_text(DISPLAY_SURF, *bgcolor_left_top_text_width, bundle)

def test_make_text_handles_long_lines_automatically(bgcolor_left_top_text_width):
    DISPLAY_SURF = flexmock() 
    flexmock(DISPLAY_SURF).should_receive("blit").times(5)
    # Note that 5 DOES depend on the font (size and typeface), which is
    # implicit. It also depends on the text_width.
    bundle = bdlr("text "*100)
    make_text(DISPLAY_SURF, *bgcolor_left_top_text_width, bundle)

def test_make_text_handles_multiple_bundles(bgcolor_left_top_text_width):
    DISPLAY_SURF = flexmock() 
    flexmock(DISPLAY_SURF).should_receive("blit").times(7)
    # Note that 7 DOES depend on the font (size and typeface), which is
    # implicit. It also depends on the text_width.
    bundle_one = bdlr("text \n text")
    bundle_two = bdlr("text "*100)
    make_text(DISPLAY_SURF, *bgcolor_left_top_text_width, bundle_one, bundle_two)


def test_make_text_handles_different_text_colors(bgcolor_left_top_text_width):
    DISPLAY_SURF = flexmock() 
    flexmock(DISPLAY_SURF).should_receive("blit").times(7)
    # Note that 7 DOES depend on the font (size and typeface), which is
    # implicit. It also depends on the text_width.
    bundle_one = bdlr("text \n text", color=(0, 0, 255))
    bundle_two = bdlr("text "*100, color=(255, 0, 0))
    make_text(DISPLAY_SURF, *bgcolor_left_top_text_width, bundle_one, bundle_two)

def test_get_number_of_lines_handles_newline_characters():
    left = 10
    text_width = 1000
    bundle = bdlr("text \n text")
    assert get_number_of_lines(left, text_width, bundle) == 2

def test_get_number_of_lines_handles_long_lines_automatically():
    left = 10
    text_width = 1000
    bundle = bdlr("text "*100)
    assert get_number_of_lines(left, text_width, bundle) == 5
    # Note that 5 DOES depend on the font (size and typeface), which is
    # implicit. It also depends on the text_width.

def test_make_all_options(bgcolor_left_top_text_width):
    DISPLAY_SURF = flexmock()
    flexmock(DISPLAY_SURF).should_receive("blit").times(4)
    # Once for each bundle, and a fourth for the hovered cursor.
    cursor_index = 0
    bundle_one = bdlr("one")
    bundle_two = bdlr("two")
    bundle_three = bdlr("three")
    make_all_options(
            DISPLAY_SURF, 
            *bgcolor_left_top_text_width,
            cursor_index, 
            bundle_one,
            bundle_two,
            bundle_three
        )