from flexmock import flexmock
import pytest

from gng.managers.character_sheet_manager import CharacterSheetManager

def test_there_are_the_same_number_of_submenu_states_and_submenu_transitions():
    csm = CharacterSheetManager(flexmock(), flexmock())
    assert len(csm.list_of_submenus) == len(csm.list_of_events_to_submenus)