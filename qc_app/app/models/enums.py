from fastapi import FastAPI
from enum import Enum

class RuleViolation(str, Enum):
    no_violation = "PASS"
    one_2s = "Warning, One point exceeding mean ± 2SD)"
    one_3s = "Fail, One point exceeding mean ± 3SD)"
    two_2s = "Fail, Two consecutive points exceeding mean ± 2SD)"
    range_4s = "Fail, Range of four consecutive points exceeding mean ± 2SD)"
    four_1s = "Fail, Four consecutive points exceeding mean ± 1SD)"
    ten_x = "Fail, Ten consecutive points on the same side of the mean)"

class QCStatus(str, Enum):
    PASS = "PASS"
    WARNING = "WARNING"
    FAIL = "FAIL"
