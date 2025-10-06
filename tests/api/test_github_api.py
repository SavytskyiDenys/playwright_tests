import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('SavytskyiDenys')
    assert user['login'] == 'SavytskyiDenys'

@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('Savytskyi_Denys')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 57
    assert 'become-qa-auto' in r['items'][0]['name']

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('eroiwutyow')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('q')
    assert r['total_count'] != 0

@pytest.mark.api
def test_emoji_list_retrieved(github_api):
    r = github_api.get_emojis()
    assert r.status_code == 200
    assert 'crossed_fingers' in r.json()

@pytest.mark.api
def test_list_of_commits_retrieved_exist_repo(github_api):
    r = github_api.get_commits_of_public_repo('SavytskyiDenys', 'playwright_tests')
    assert r is not None
    assert 'Denys Savytskyi' in r[0]['commit']['author']['name']

@pytest.mark.api
def test_list_of_commits_not_retrieved_non_exist_repo(github_api):
    r = github_api.get_commits_of_public_repo('SavytskyiDenys','11111')
    assert r['status'] == "404"
