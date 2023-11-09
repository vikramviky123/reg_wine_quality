import sys
from src import logging, CustomException
from src.wine_reg.e_pipeline.stg_01_data_ingestion import DataIngestionPipeline
from src.wine_reg.e_pipeline.stg_02_data_transformation import DataTransformationPipeline
from src.wine_reg.e_pipeline.stg_03_model_training import ModelTrainingPipeline
# ----------------------------------------------------------------------------------------------------
STAGE_NAME = "DATA -- INGESTION -- STAGE"

try:
    logging.info(
        f"\n\nx==========x\n\n>>>>>> stage {STAGE_NAME} started <<<<<<\n\n")
    obj = DataIngestionPipeline()
    obj.main()
    logging.info(
        f"\n\n>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x\n\n")
except Exception as e:
    logging.exception(CustomException(e, sys))
    raise CustomException(e, sys)
# ----------------------------------------------------------------------------------------------------

STAGE_NAME = "DATA -- TRANSFORMATION -- STAGE"

try:
    logging.info(
        f"\n\nx==========x\n\n>>>>>> stage {STAGE_NAME} started <<<<<<\n\n")
    obj = DataTransformationPipeline()
    obj.main()
    logging.info(
        f"\n\n>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x\n\n")
except Exception as e:
    logging.exception(CustomException(e, sys))
    raise CustomException(e, sys)
# ----------------------------------------------------------------------------------------------------

STAGE_NAME = "DATA -- TRAINING -- STAGE"

try:
    logging.info(
        f"\n\nx==========x\n\n>>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logging.info(
        f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x\n\n")
except Exception as e:
    logging.exception(CustomException(e, sys))
    raise CustomException(e, sys)
