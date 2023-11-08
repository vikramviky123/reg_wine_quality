from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    downloaded_dir: Path
    extracted_dir: Path
    file_path: Path
