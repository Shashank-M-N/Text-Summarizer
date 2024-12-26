from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from textSummarizer.logging import logger
from filelock import FileLock

LOCK_FILE = "pipeline.lock"

with FileLock(LOCK_FILE):
    if __name__ == "__main__":
        STAGE_NAME = "Data Ingestion stage"
        try:
            logger.info(f">>>> stage {STAGE_NAME} started <<<<")
            data_ingestion = DataIngestionTrainingPipeline()
            data_ingestion.main()
            logger.info(f">>>> stage {STAGE_NAME} completed <<<<\n")
        except Exception as e:
            logger.exception(e)
            raise e

        STAGE_NAME = "Data Validation stage"
        try:
            logger.info(f">>>> stage {STAGE_NAME} started <<<<")
            data_validation = DataValidationTrainingPipeline()
            data_validation.main()
            logger.info(f">>>> stage {STAGE_NAME} completed <<<<\n")
        except Exception as e:
            logger.exception(e)
            raise e

        STAGE_NAME = "Data Transformation stage"
        try:
            logger.info(f">>>> stage {STAGE_NAME} started <<<<")
            data_transformation = DataTransformationTrainingPipeline()
            data_transformation.main()
            logger.info(f">>>> stage {STAGE_NAME} completed <<<<\n")
        except Exception as e:
            logger.exception(e)
            raise e

        STAGE_NAME = "Model Trainer stage"
        try:
            logger.info(f">>>> stage {STAGE_NAME} started <<<<")
            model_trainer = ModelTrainerTrainingPipeline()
            model_trainer.main()
            logger.info(f">>>> stage {STAGE_NAME} completed <<<<\n")
        except Exception as e:
            logger.exception(e)
            raise e

        STAGE_NAME = "Test"
        try:
            logger.info(f">>>> stage {STAGE_NAME} started <<<<")
            logger.info(f">>>> stage {STAGE_NAME} completed <<<<\n")
        except Exception as e:
            logger.exception(e)
            raise e