from src.ds.constants import *
from src.ds.utlis.common import Load_yaml, create_dir
from src.ds.entity.config_entity import DataIngestionConfig,DataValidationConfig


class ConfigManager:
    def __init__(
            self,
            config_filepath=CONFIG_FILE_PATH,
            params_filepath=PARAMS_FILE_PATH,
            schema_filepath=SCHEMA_FILE_PATH
            ):
        self.config = Load_yaml(config_filepath)
        self.yaml= Load_yaml(params_filepath)
        self.schema= Load_yaml(schema_filepath)
        create_dir([self.config.artifacts_root])
    def get_data_ingest(self)-> DataIngestionConfig:
        config=self.config.data_ingestion
        create_dir([config.root_dir])

        data_in_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_in_config
    def get_data_val(self)-> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.columns

        create_dir([config.root_dir])

        dvc = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_dir=config.unzip_dir,
            all_schema=schema
        )
        return dvc
        
        
        