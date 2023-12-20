from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import preparebaseModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline


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
 
    
try:
    logger.info(f">>>>stage {STAGE_NAME} started <<<<")
    obj=preparebaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e 

try:
    logger.info(f">>>>stage {STAGE_NAME} started <<<<")
    obj=ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e 
