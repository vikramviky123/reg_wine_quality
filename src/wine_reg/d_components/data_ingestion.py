import os
import sys
from pathlib import Path
import urllib.request as request
import zipfile

from src import logging, CustomException

from src.wine_reg.c_config.configuration import DataIngestionConfig
from src.wine_reg.f_utils.common import get_size


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.file_path):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.file_path
            )
            logging.info(
                f"{filename} download! with following info: \n{headers}")
        else:
            logging.info(
                f"File already exists of size: {get_size(Path(self.config.file_path))}")

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.extracted_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.file_path, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
