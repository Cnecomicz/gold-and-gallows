from flexmock import flexmock
import pytest

from gng.functions.character_functions import (
    InvalidClass,
    calculate_AV
)

def test_calculate_AV_matches_data_in_pdf_cleric():
    assert calculate_AV("Cleric",  1) == 11
    assert calculate_AV("Cleric",  2) == 11
    assert calculate_AV("Cleric",  3) == 12
    assert calculate_AV("Cleric",  4) == 12
    assert calculate_AV("Cleric",  5) == 12
    assert calculate_AV("Cleric",  6) == 13
    assert calculate_AV("Cleric",  7) == 13
    assert calculate_AV("Cleric",  8) == 14
    assert calculate_AV("Cleric",  9) == 14
    assert calculate_AV("Cleric", 10) == 14
    assert calculate_AV("Cleric", 99) == 50

def test_calculate_AV_matches_data_in_pdf_druid():
    assert calculate_AV("Druid",  1) ==  8
    assert calculate_AV("Druid",  2) ==  8
    assert calculate_AV("Druid",  3) ==  9
    assert calculate_AV("Druid",  4) ==  9
    assert calculate_AV("Druid",  5) ==  9
    assert calculate_AV("Druid",  6) == 10
    assert calculate_AV("Druid",  7) == 10
    assert calculate_AV("Druid",  8) == 11
    assert calculate_AV("Druid",  9) == 11
    assert calculate_AV("Druid", 10) == 11
    assert calculate_AV("Druid", 99) == 47

def test_calculate_AV_matches_data_in_pdf_dwarf():
    assert calculate_AV("Dwarf",  1) == 11
    assert calculate_AV("Dwarf",  2) == 11
    assert calculate_AV("Dwarf",  3) == 12
    assert calculate_AV("Dwarf",  4) == 12
    assert calculate_AV("Dwarf",  5) == 13
    assert calculate_AV("Dwarf",  6) == 13
    assert calculate_AV("Dwarf",  7) == 14
    assert calculate_AV("Dwarf",  8) == 14
    assert calculate_AV("Dwarf",  9) == 15
    assert calculate_AV("Dwarf", 10) == 15
    assert calculate_AV("Dwarf", 99) == 60

def test_calculate_AV_matches_data_in_pdf_elf():
    assert calculate_AV("Elf",  1) == 11
    assert calculate_AV("Elf",  2) == 11
    assert calculate_AV("Elf",  3) == 12
    assert calculate_AV("Elf",  4) == 13
    assert calculate_AV("Elf",  5) == 13
    assert calculate_AV("Elf",  6) == 14
    assert calculate_AV("Elf",  7) == 15
    assert calculate_AV("Elf",  8) == 15
    assert calculate_AV("Elf",  9) == 16
    assert calculate_AV("Elf", 10) == 17
    assert calculate_AV("Elf", 99) == 76

def test_calculate_AV_matches_data_in_pdf_fighter():
    assert calculate_AV("Fighter",  1) == 11
    assert calculate_AV("Fighter",  2) == 12
    assert calculate_AV("Fighter",  3) == 12
    assert calculate_AV("Fighter",  4) == 13
    assert calculate_AV("Fighter",  5) == 14
    assert calculate_AV("Fighter",  6) == 14
    assert calculate_AV("Fighter",  7) == 15
    assert calculate_AV("Fighter",  8) == 16
    assert calculate_AV("Fighter",  9) == 16
    assert calculate_AV("Fighter", 10) == 17
    assert calculate_AV("Fighter", 99) == 76

def test_calculate_AV_matches_data_in_pdf_halfling():
    assert calculate_AV("Halfling",  1) == 12
    assert calculate_AV("Halfling",  2) == 12
    assert calculate_AV("Halfling",  3) == 12
    assert calculate_AV("Halfling",  4) == 12
    assert calculate_AV("Halfling",  5) == 13
    assert calculate_AV("Halfling",  6) == 13
    assert calculate_AV("Halfling",  7) == 13
    assert calculate_AV("Halfling",  8) == 13
    assert calculate_AV("Halfling",  9) == 14
    assert calculate_AV("Halfling", 10) == 14
    assert calculate_AV("Halfling", 99) == 36

def test_calculate_AV_matches_data_in_pdf_magic_user():
    assert calculate_AV("Magic-User",  1) ==  8
    assert calculate_AV("Magic-User",  2) ==  8
    assert calculate_AV("Magic-User",  3) ==  8
    assert calculate_AV("Magic-User",  4) ==  9
    assert calculate_AV("Magic-User",  5) ==  9
    assert calculate_AV("Magic-User",  6) ==  9
    assert calculate_AV("Magic-User",  7) == 10
    assert calculate_AV("Magic-User",  8) == 10
    assert calculate_AV("Magic-User",  9) == 10
    assert calculate_AV("Magic-User", 10) == 11
    assert calculate_AV("Magic-User", 99) == 40

def test_calculate_AV_matches_data_in_pdf_paladin():
    assert calculate_AV("Paladin",  1) == 11
    assert calculate_AV("Paladin",  2) == 11
    assert calculate_AV("Paladin",  3) == 12
    assert calculate_AV("Paladin",  4) == 12
    assert calculate_AV("Paladin",  5) == 13
    assert calculate_AV("Paladin",  6) == 13
    assert calculate_AV("Paladin",  7) == 14
    assert calculate_AV("Paladin",  8) == 14
    assert calculate_AV("Paladin",  9) == 15
    assert calculate_AV("Paladin", 10) == 15
    assert calculate_AV("Paladin", 99) == 60

def test_calculate_AV_matches_data_in_pdf_ranger():
    assert calculate_AV("Ranger",  1) == 11
    assert calculate_AV("Ranger",  2) == 11
    assert calculate_AV("Ranger",  3) == 12
    assert calculate_AV("Ranger",  4) == 12
    assert calculate_AV("Ranger",  5) == 13
    assert calculate_AV("Ranger",  6) == 13
    assert calculate_AV("Ranger",  7) == 14
    assert calculate_AV("Ranger",  8) == 14
    assert calculate_AV("Ranger",  9) == 15
    assert calculate_AV("Ranger", 10) == 15
    assert calculate_AV("Ranger", 99) == 60

def test_calculate_AV_matches_data_in_pdf_warlock():
    assert calculate_AV("Warlock",  1) ==  8
    assert calculate_AV("Warlock",  2) ==  8
    assert calculate_AV("Warlock",  3) ==  8
    assert calculate_AV("Warlock",  4) ==  9
    assert calculate_AV("Warlock",  5) ==  9
    assert calculate_AV("Warlock",  6) ==  9
    assert calculate_AV("Warlock",  7) == 10
    assert calculate_AV("Warlock",  8) == 10
    assert calculate_AV("Warlock",  9) == 10
    assert calculate_AV("Warlock", 10) == 11
    assert calculate_AV("Warlock", 99) == 40

def test_catching_typos():
    with pytest.raises(InvalidClass):
        calculate_AV("typo", 4)
