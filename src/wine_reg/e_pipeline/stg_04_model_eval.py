import os
import sys
from pathlib import Path

from src import logging, CustomException
from src.wine_reg.b_entity.config_entity import ModelEvalConfig
from src.wine_reg.c_config.configuration import ConfigurationManager
from src.wine_reg.d_components.model_eval import ModelEvaluation

STAGE_NAME = "MODEL -- EVALUATION -- STAGE"


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_eval_config = config.get_model_eval_config()
        model_eval = ModelEvaluation(config=model_eval_config)
        model_eval.log_to_mlflow()


if __name__ == '__main__':
    try:
        logging.info(
            f"\n\nx==========x\n\n>>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logging.info(
            f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x\n\n")
    except Exception as e:
        logging.exception(CustomException(e, sys))
        raise CustomException(e, sys)
