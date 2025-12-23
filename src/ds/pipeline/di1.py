from src.ds.config.configuration import ConfigManager
from src.ds.components.data_ingestion import DataIngestion,DataIngestionConfig 
from src.ds import logger

STAGE_NAME= "DATA INGESTION STAGE"
class Dctp:
    def __init__(self):
        pass
    def initiate_data(self):
        config = ConfigManager()
        DataIngestion_c = config.get_data_ingest()
        data_ingestion=DataIngestion(config=DataIngestion_c)
        data_ingestion.download_file()

if __name__ == "__main__":
    try:
        logger.info(f'>>>stage_name{STAGE_NAME} started')
        obj = Dctp()
        obj.initiate_data()
        logger.info(f'stage name {STAGE_NAME} completed')
    except Exception as e:
        logger.exception(e)
        raise e
