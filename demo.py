# from us_visa.configuration.mongo_db_connection import MongoDBClient

# ins = MongoDBClient()

# from us_visa.configuration.aws_connection import S3Client

# ins = S3Client()

#Data ingestion 
from us_visa.entity.config_entity import DataIngestionConfig,DataTransformationConfig
from us_visa.entity.config_entity import DataValidationConfig

from us_visa.components.data_ingestion import DataIngestionArtifact
from us_visa.components.data_validation import DataValidationArtifact
from us_visa.components.data_transformation import DataTransformationArtifact

from us_visa.components.data_ingestion import DataIngestion
from us_visa.components.data_validation import DataValidation
from us_visa.components.data_transformation import DataTransformation


di_ins = DataIngestion(DataIngestionConfig)

di_art = di_ins.initiate_data_ingestion()

# Data validation 
dv_ins = DataValidation(data_ingestion_artifact=di_art, data_validation_config=DataValidationConfig)

dv_art = dv_ins.initiate_data_validation()

# Data transformation

dt_ins = DataTransformation(data_ingestion_artifact=di_art, data_transformation_config=DataTransformationConfig, data_validation_artifact=dv_art)

dt_art = dt_ins.initiate_data_transformation()