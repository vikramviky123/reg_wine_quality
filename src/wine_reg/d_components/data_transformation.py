import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split

from src import logging, CustomException
from src.wine_reg.b_entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    # Note: You can add different data transformation techniques such as Scaler, PCA and all
    # You can perform all kinds of EDA in ML cycle here before passing this data to the model

    # I am only adding train_test_spliting cz this data is already cleaned up

    def train_test_spliting(self):
        try:
            data = pd.read_csv(self.config.data_path)

            # Split the data into training and test sets. (0.75, 0.25) split.
            train, test = train_test_split(data)

            train.to_csv(os.path.join(
                self.config.root_dir, "train.csv"), index=False)
            test.to_csv(os.path.join(
                self.config.root_dir, "test.csv"), index=False)

            logging.info("Splited data into training and test sets")
            logging.info(
                f" Train Shape ==> {train.shape} | test Shape ==> {test.shape}")
        except Exception as e:
            logging.error(CustomException(e, sys))
            raise CustomException(e, sys)
