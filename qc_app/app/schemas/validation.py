from pydantic import BaseModel

from app.models.enums import QCStatus, RuleViolation

class QCValidation(BaseModel):
    z_score: float
    status: QCStatus
    violation: RuleViolation
