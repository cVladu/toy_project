import pytest


@pytest.mark.zephyr_testcase(
    objective="To veirfy that it works",
    precondution="None",
    priorityName="Low",
    statusName="Draft",
    ownerId="5c6db07284926c623fb1b347",
    labels=["meta", "test_the_test"],
    jira_issues=["TP-18"],
    urls=["www.google.com", "www.example.com"],
    test_steps="doc",
)
def test_trial():
    """
    Test the test
    """
    assert 1 + 1 == 2
