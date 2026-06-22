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


@dataclass(frozen = True)
class DataTransformationConfig:
    root_dir : Path
    data_path : Path


@dataclass(frozen = True)
class ModelTrainerConfig:
    root_dir : Path
    train_data_path : Path
    test_data_path : Path
    model_name : str
    alpha : float
    l1_ratio : float
    TARGET_COLUMN : str



@dataclass(frozen = True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    TARGET_COLUMN: str