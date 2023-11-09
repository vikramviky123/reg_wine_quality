import os
import sys

from src import logging, CustomException

from src.wine_reg.a_constants import *
from src.wine_reg.f_utils.common import read_yaml, create_directories
from src.wine_reg.b_entity.config_entity import (DataIngestionConfig,
                                                 DataTransformationConfig,
                                                 ModelTrainerConfig)


class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH):

        self.config = read_yaml(config_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir,
                            config.downloaded_dir,
                            config.extracted_dir])

        data_ingestion_config = DataIngestionConfig(root_dir=config.root_dir,
                                                    source_URL=config.source_URL,
                                                    downloaded_dir=config.downloaded_dir,
                                                    extracted_dir=config.extracted_dir,
                                                    file_path=config.file_path)

        return data_ingestion_config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
        )

        return data_transformation_config

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            model_name=config.model_name,
            target=config.target,
        )

        return model_trainer_config
