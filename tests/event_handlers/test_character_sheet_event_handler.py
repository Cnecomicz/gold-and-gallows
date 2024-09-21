from flexmock import flexmock
import pytest

from gng.event_handlers.character_sheet_event_handler import CharacterSheetEventHandler
from gng.managers.character_statistics import CharacterSheetManager

# def test_pressing_e():
#     csm = CharacterSheetManager(flexmock(), flexmock(), flexmock(), flexmock())
#     cseh = CharacterSheetEventHandler(csm, flexmock())
#     cseh.handle_keydown_use(flexmock())