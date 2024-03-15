# -*- coding: utf-8 -*-
def naive_write_csv_row(fields):
    return ",".join(f'"{field}"' for field in fields)


def naive_read_csv_row(row):
    return [field[1:-1] for field in row.split(",")]
