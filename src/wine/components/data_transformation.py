import os
from src.wine.logging import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from src.wine.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    # perform EDA
    # perform data transformation techniques such as scaling, standardization, PCA, feature scaling, etc.
    # perform train_test_split

    # here we are just adding train_test_spliting because this data is already cleaned up


    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
        