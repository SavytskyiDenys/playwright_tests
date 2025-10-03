#import re
#from playwright.sync_api import Page, expect
import pytest

@pytest.mark.change
def test_remove_user(user):
    user.name = ''
    assert user.name == ''

@pytest.mark.check
def test_name(user):
    assert user.name == 'Denys'

@pytest.mark.check
def test_second_name(user):
    assert user.second_name == 'Savytskyi'
