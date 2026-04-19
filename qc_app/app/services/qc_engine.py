from app.models.enums import QCStatus, RuleViolation
from app.schemas.validation import QCValidation

def calculate_z_score(value: float, mean: float, sd: float) -> float:
    if sd == 0:
        return 0.0
    result = (value - mean)/sd
    return result

def validate_result(value: int, mean: float, sd: float) -> QCValidation:
    z_score = calculate_z_score(value, mean, sd)

    if abs(z_score) >= 3:
        status = QCStatus.FAIL
        violation = RuleViolation.one_3s

    elif abs(z_score) >= 2:
        status = QCStatus.WARNING
        violation = RuleViolation.one_2s

    else:
        status = QCStatus.PASS
        violation = RuleViolation.no_violation

    return QCValidation(z_score= z_score, status= status, violation = violation)



























