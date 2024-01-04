from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class PriceIngestionConfig:
    root_dir: Path
    data_dir: str
    companies: dict
    date_start: str
    date_end: str
    period: str