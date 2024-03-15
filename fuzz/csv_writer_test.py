# -*- coding: utf-8 -*-
import pytest
from hypothesis import given
from hypothesis import strategies as st

from src.csv_writer import naive_read_csv_row, naive_write_csv_row


@pytest.mark.zephyr_testcase(
    objective="To fuzz the csv writer and parser",
    precondition="None",
    priorityName="Low",
    statusName="Approved",
    ownerId="5c6db07284926c623fb1b347",
    labels=["fuzz", "csv_writer", "csv_reader"],
    jira_issues=["TP-20"],
    test_steps="doc",
)
@given(fields=st.lists(st.text(), min_size=1, max_size=10))
def test_read_write_csv_hypothesis(fields):
    """
    Fuzz test for CSV writer and parser
    """
    formatted_row = naive_write_csv_row(fields)
    parsed_row = naive_read_csv_row(formatted_row)
    assert fields == parsed_row
