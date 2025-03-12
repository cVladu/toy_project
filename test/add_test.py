# -*- coding: utf-8 -*-
import pytest
import numpy as np
import src.sum as sum

# Just a comment

@pytest.mark.zephyr_testcase(
    objective="To verify basic add functionality",
    precondition="None",
    priorityName="Low",
    statusName="Approved",
    ownerId="5c6db07284926c623fb1b347",
    labels=["smoke", "add"],
    jira_issues=["TP-19"],
    test_steps="doc",
)
def test_add_smoke():
    """
    Test the add function
    """
    assert sum.do_sum(1, 2) == 3


@pytest.mark.zephyr_testcase(
    objective="To verify basic add functionality",
    precondition="None",
    priorityName="Low",
    statusName="Approved",
    ownerId="5c6db07284926c623fb1b347",
    labels=["smoke", "add"],
    jira_issues=["TP-19"],
    test_steps="doc",
)
def test_add_another_test():
    """
    Test the add function
    """
    assert sum.do_sum(1, 5) == 6


@pytest.mark.zephyr_testcase(
    objective="To verify multiple cases",
    precondition="None",
    priorityName="Normal",
    statusName="Approved",
    ownerId="5c6db07284926c623fb1b347",
    labels=["add"],
    jira_issues=["TP-19"],
    test_steps="doc",
)
@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (2, 3, 5), (3, 4, 7)])
def test_add_parametrized(a, b, expected):
    """
    Test the add function
    """
    assert sum.do_sum(a, b) == expected


@pytest.mark.zephyr_testcase(
    objective="To verify multiple cases",
    precondition="None",
    priorityName="Normal",
    statusName="Approved",
    ownerId="5c6db07284926c623fb1b347",
    labels=["add"],
    jira_issues=["TP-19"],
    test_steps="doc",
)
@pytest.mark.skip(reason="Not implemented yet")
@pytest.mark.parametrize(
    "a, b, c, expected", [(1, 2, 3, 3), (2, 3, 4, 5), (3, 4, 5, 7)]
)
def test_add_multiple_parametrized(a, b, c, expected):
    """
    Test the add function
    """
    assert sum.do_sum_multiple(a, b, c) == expected


@pytest.mark.zephyr_testcase(
    objective="To verify multiple cases",
    precondition="None",
    priorityName="Normal",
    statusName="Approved",
    ownerId="5c6db07284926c623fb1b347",
    labels=["add"],
    jira_issues=["TP-19"],
    test_steps=[
        {"step": "Step 1", "expected": "Expected 1"},
        {
            "step": "Step without expectation",
        },
    ],
)
@pytest.mark.parametrize(
    "a, b, c, expected", [(1, 2, 3, 3), (2, 3, 4, 5), (3, 4, 5, 7)]
)
def test_with_test_steps(a, b, c, expected):
    """
    Test the add function
    """
    assert sum.do_sum(a, b) == expected


@pytest.mark.zephyr_testcase(
    objective="To verify multiple cases",
    precondition="None",
    priorityName="Normal",
    statusName="Approved",
    ownerId="5c6db07284926c623fb1b347",
    labels=["add"],
    jira_issues=["TP-19"],
    test_steps=[
        {"step": "Step 1", "expected": "Expected 1"},
        {
            "step": "Step without expectation",
        },
    ],
)
@pytest.mark.parametrize(
    "a, b, c, expected", [(1, 2, 3, 3), (2, 3, 4, 5), (3, 4, 5, 7)]
)
def test_with_test_steps_failed(a, b, c, expected):
    """
    Test the add function
    """
    assert sum.do_sum(a, c) == expected
