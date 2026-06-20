from src.wine.config.configuration import ConfigurationManager
from src.wine.components.data_ingestion import DataIngestion
from src.wine.logging import logger

STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()     # object creation
        data_ingestion_config = config.get_data_ingestion_config()      # stored output of config object's method
        data_ingestion = DataIngestion(config = data_ingestion_config)     # object creation
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e