import sys
from src import logging, CustomException
from src.wine_reg.e_pipeline.stg_01_data_ingestion import DataIngestionPipeline

STAGE_NAME = "DATA -- INGESTION -- STAGE"


try:
    logging.info(
        f"\n\nx==========x\n\n>>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logging.info(
        f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x\n\n")
except Exception as e:
    logging.exception(CustomException(e, sys))
    raise CustomException(e, sys)
