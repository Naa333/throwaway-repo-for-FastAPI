from datetime import datetime
from pydantic import BaseModel
from app.models.enums import QCStatus, RuleViolation


class QCReport(BaseModel):
    report_id: int
    analyte_id: int
    status: QCStatus
    violation: RuleViolation
    timestamp: datetime