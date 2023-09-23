import re


CADASTR_NUMBER_PATTERN = "^[\d]{2}:[\d]{2}:[\d]{6,7}:[1-9]{1}[\d]{0,5}$"

CADASTR_NUMBER_REGEX = re.compile(CADASTR_NUMBER_PATTERN)