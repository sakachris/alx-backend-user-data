#!/usr/bin/env python3
''' filtered_logger.py '''

import re


def filter_datum(
        fields: list[str], redaction: str, message: str, separator: str
) -> str:
    for field in fields:
        pattern = rf'({field}=)[^{separator}]*'
        message = re.sub(pattern, rf'\1{redaction}', message)
    return message
