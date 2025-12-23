from src.ds import logger
from src.ds.pipeline.di1 import Dctp
STAGE_NAME= 'Data Ingestion Stage'
try:
    logger.info(f'>>>> {STAGE_NAME} started <<<<')
    data_ing = Dctp()
    data_ing.initiate_data()
    logger.info(f'>>>>> {STAGE_NAME} Completed')
except Exception as e:
    logger.exception(e)
    raise e 