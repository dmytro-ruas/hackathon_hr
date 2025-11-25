import csv
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Optional, Callable

# -----------------------------
# Data Model
# -----------------------------

@dataclass
class ClockHour:
    Id: int
    EmployeeId: int
    ActivityId: int
    Year: int
    Month: int
    Date: str
    FromTime: str
    ToTime: str
    Hours: float
    Rate: float
    Status: str

# -----------------------------
# CSV Connector
# Changes are not required to this file, but you can modify it if you want to add features.
# -----------------------------

class CsvConnector:
    def __init__(self, path: str):
        self.path = Path(path)
        self.entries: List[ClockHour] = []
        self.header: List[str] = []
