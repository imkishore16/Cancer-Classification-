from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import preparebaseModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_04_model_evaluation_with_mlflow import EvaluationPipeline
import os

logger.info("Welcom to CNN_Classifier")

STAGE_NAME ="Data Ingestion Stage"

try:
    logger.info(f">>>>stage {STAGE_NAME} started <<<<")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Prepare base model"    
try:
    logger.info(f">>>>stage {STAGE_NAME} started <<<<")
    obj=preparebaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME = "Training"
try:
    logger.info(f">>>>stage {STAGE_NAME} started <<<<")
    obj=ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e 


STAGE_NAME = "Evaluation stage"
try:
    os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/imkishor16/Cancer-Classification-.mlflow"
    os.environ["MLFLOW_TRACKING_USERNAME"]="imkishor16"
    os.environ["MLFLOW_TRACKING_PASSWORD"]="0ce5e70a3b1a01a6d55eddf646009426e1067b04"
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_evalution = EvaluationPipeline()
    model_evalution.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e
