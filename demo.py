# from us_visa.configuration.mongo_db_connection import MongoDBClient

# ins = MongoDBClient()

# from us_visa.configuration.aws_connection import S3Client

# ins = S3Client()

# Data ingestion 
# from us_visa.entity.config_entity import DataIngestionConfig,DataTransformationConfig,ModelTrainerConfig,ModelEvaluationConfig
# from us_visa.entity.config_entity import DataValidationConfig
# from us_visa.entity.config_entity import ModelPusherConfig

# from us_visa.components.data_ingestion import DataIngestionArtifact
# from us_visa.components.data_validation import DataValidationArtifact
# from us_visa.components.data_transformation import DataTransformationArtifact
# from us_visa.components.model_trainer import ModelTrainerArtifact
# from us_visa.components.model_evaluation import ModelEvaluationArtifact
# from us_visa.components.model_pusher import ModelPusherArtifact

# from us_visa.components.data_ingestion import DataIngestion
# from us_visa.components.data_validation import DataValidation
# from us_visa.components.data_transformation import DataTransformation
# from us_visa.components.model_trainer import ModelTrainer
# from us_visa.components.model_evaluation import ModelEvaluation
# from us_visa.components.model_pusher import ModelPusher


# di_ins = DataIngestion(DataIngestionConfig)

# di_art = di_ins.initiate_data_ingestion()

# # Data validation 
# dv_ins = DataValidation(data_ingestion_artifact=di_art, data_validation_config=DataValidationConfig)

# dv_art = dv_ins.initiate_data_validation()

# # Data transformation

# dt_ins = DataTransformation(data_ingestion_artifact=di_art, data_transformation_config=DataTransformationConfig, data_validation_artifact=dv_art)

# dt_art = dt_ins.initiate_data_transformation()

# # Model trainer

# mt_ins = ModelTrainer(data_transformation_artifact=dt_art, model_trainer_config=ModelTrainerConfig)

# mt_art = mt_ins.initiate_model_trainer()

# # check for aws connection
# # from us_visa.configuration.aws_connection import S3Client

# # ins = S3Client()

# me_ins = ModelEvaluation(model_eval_config=ModelEvaluationConfig, data_ingestion_artifact=di_art, model_trainer_artifact=mt_art)

# me_art = me_ins.initiate_model_evaluation()

# # Model Pusher
# mp_ins = ModelPusher(me_art, ModelPusherConfig)

# mp_art = mp_ins.initiate_model_pusher()

# comment all above code and run only below code for training pipeline working or not 
from us_visa.pipeline.training_pipeline import TrainPipeline
tr_pp = TrainPipeline()
tr_pp.run_pipeline()

# for prediction 

# from us_visa.pipeline.prediction_pipeline import USvisaData, USvisaClassifier

# usvisa_data = USvisaData(
#                         continent= 'Asia',
#                         education_of_employee = 'Doctorate',
#                         has_job_experience = 'Y',
#                         requires_job_training = 'N',
#                         no_of_employees= 20000,
#                         company_age= 100,
#                         region_of_employment = 'Northeast',
#                         prevailing_wage= 10000,
#                         unit_of_wage= 'Year',
#                         full_time_position= 'Y',
#                         )

# # usvisa_data = USvisaData(
# #                         continent= 'Asia',
# #                         education_of_employee = 'Doctorate',
# #                         has_job_experience = 'N',
# #                         requires_job_training = 'Y',
# #                         no_of_employees= 15000,
# #                         company_age= 10,
# #                         region_of_employment = 'West',
# #                         prevailing_wage= 1000,
# #                         unit_of_wage= 'Hour',
# #                         full_time_position= 'N',
# #                         )
# usvisa_df = usvisa_data.get_usvisa_input_data_frame()

# model_predictor = USvisaClassifier()

# value = model_predictor.predict(dataframe=usvisa_df)[0]

# print(value)