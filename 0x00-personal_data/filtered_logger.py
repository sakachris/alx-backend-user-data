#!/usr/bin/env python3
''' filtered_logger.py '''

import re
from typing import List


def extract_pattern(fields: List[str], separator: str) -> str:
    """Generate the regular expression pattern for extracting fields."""
    return rf'(?P<field>{ "|".join(fields) })=[^{separator}]*'


def replace_pattern(redaction: str) -> str:
    """Generate the replacement pattern."""
    return rf'\g<field>={redaction}'


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str,
        ) -> str:
    """Filters a log line."""
    extract = extract_pattern(fields, separator)
    replace = replace_pattern(redaction)
    return re.sub(extract, replace, message)
