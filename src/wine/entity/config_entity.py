from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen = True) # frozen enures that once an instance of the following class is created the class attributes can't be modified.
class DataIngestionConfig:
    root_dir : Path
    src_url : str
    local_data_file : Path
    unzip_dir : Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir : Path
    unzip_data_dir : Path
    status_file : str
    all_schema : dict