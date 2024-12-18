import os
from textSummarizer.logging import logger
from textSummarizer.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:
            present_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))
            
            missing_files = [file for file in self.config.ALL_REQUIRED_FILES if file not in present_files]
            
            validation_status = ( len(missing_files) == 0 )
            
            with open(self.config.STATUS_FILE, 'w') as f:
                if validation_status:
                    f.write("Validation status: True. All required files are present.")
                else:
                    f.write(f"Validation status: False. Missing files: {', '.join(missing_files)}")
            
            return validation_status

        except Exception as e:
            raise e