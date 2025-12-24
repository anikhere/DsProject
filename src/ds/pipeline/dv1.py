from src.ds.config.configuration import ConfigManager
from src.ds.components.data_val import DataVal,DataValidationConfig 
from src.ds import logger

stage_name = 'Data Validation Stage'

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigManager()
        data_vale = config.get_data_val()
        data_vale_con = DataVal(data_vale)
        data_vale_con.val_all_col()
if __name__ == "__main__":
    try:
        logger.info(f'>>>stage_name{stage_name} started')
        obj = DataValidationPipeline()
        obj.main()
        logger.info(f'stage name {stage_name} completed')
    except Exception as e:
        logger.exception(e)
        raise e
