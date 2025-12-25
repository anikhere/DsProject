from src.ds import logger
from src.ds.pipeline.di1 import Dctp
from src.ds.pipeline.dv1 import DataValidationPipeline
from src.ds.pipeline.dtrans import DataTrans
STAGE_NAME= 'Data Ingestion Stage'
try:
    logger.info(f'>>>> {STAGE_NAME} started <<<<')
    data_ing = Dctp()
    data_ing.initiate_data()
    logger.info(f'>>>>> {STAGE_NAME} Completed')
except Exception as e:
    logger.exception(e)
    raise e 


stage_name = 'Data Validation Stage'
try:
    logger.info(f'>>>stage_name{stage_name} started')
    obj = DataValidationPipeline()
    obj.main()
    logger.info(f'stage name {stage_name} completed')
except Exception as e:
    logger.exception(e)
    raise e

stage_name = "Data Transformation"
try:
    logger.info(f'stage_name>>>>>{stage_name}<<<<<<<<')
    transformer = DataTrans()
    transformer._initiate_transformation()
    logger.info(f'stage>>>>>{stage_name}')
except Exception as e:
    logger.exception(e)
    raise e

