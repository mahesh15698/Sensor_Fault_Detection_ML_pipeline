import sys,os
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from sensor.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact, DataTransformationArtifact
from sensor.components.data_ingestion import DataIngestion
from sensor.components.data_validation import DataValidation
from sensor.components.data_transformation import DataTransformation

class TrainPipeline:
    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()

    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            self.data_ingestion_config=DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Starting Data Ingestion")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info(f"Data ingestion completed and artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact
        
        except Exception as e:
            raise SensorException(e,sys)
    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact)->DataValidationArtifact:
        try:
            data_validation_config=DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Starting Data Validation")
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,
            data_validation_config=data_validation_config                              
            )
            data_validation_artifact = data_validation.initiate_data_validation()
            logging.info(f"Data Validation completed and artifact: {data_validation_artifact}")
            return data_validation_artifact
        except Exception as e:
            raise SensorException(e,sys)      
    def data_transformation(self,data_validation_artifact:DataValidationArtifact)-> DataTransformationArtifact:
        try:
            data_transformation_config= DataTransformationConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Starting Data Transformation")
            data_tranfromation = DataTransformation(data_validation_artifact=data_validation_artifact,
                data_transformation_config=data_transformation_config)
            data_tranfromation_artifact = data_tranfromation.initiate_data_transformation()
            logging.info(f"Data Transformation is completed and artifact:{data_tranfromation_artifact}")
            return data_tranfromation_artifact
        except Exception as e:
            raise SensorException
    def start_model_trainer(self):
        try:
            pass
        except Exception as e:
            raise SensorException
    def start_model_evaluation(self):
        try:
            pass
        except Exception as e:
            raise SensorException
    def model_pusher(self):
        try:
            pass
        except Exception as e:
            raise SensorException 
    def run_pipeline(self):
        try:
            
            data_ingestion_artifact: DataIngestionArtifact=self.start_data_ingestion()
            data_validation_artifact: DataValidationArtifact=self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            data_transformation_artifact: DataTransformationArtifact= self.data_transformation(data_validation_artifact=data_validation_artifact)            
        except Exception as e:
            raise SensorException
    