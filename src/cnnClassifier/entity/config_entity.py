# UPDATE ENTITY

from dataclasses import dataclass
from pathlib import Path

# defineing entity
# this entity defines the return type of a function
# this is the return tupe of the data_ingestion configuration
@dataclass(frozen=True) # frozen=True means we will not allow any more functionality to be added , ie if the data_ingestion returns one more value or one less , it throws error
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
# when we create the data_ingestion configuration this entity will tell what that configuration will return 

# @dataclass ,is a decorator that will enable us to write a class without using self


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    # these are from the params.config file
    params_image_size: list  
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int
    
    
    

@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    # from params.yaml , these are the parameters
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list
    

@dataclass(frozen=True)
class EvaluationConfig:
    path_of_model: Path
    training_data: Path
    all_params: dict
    mlflow_uri: str
    params_image_size: list
    params_batch_size: int