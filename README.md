# Text-Summarizer

## Overview

Text-Summarizer is a Python-based project that leverages NLP techniques to summarize text. The project uses the SAMSum dataset for training and evaluation. It includes various stages such as data ingestion, data validation, data transformation, model training, and model evaluation.

## Workflows

1. **Update `config.yaml`**: Modify the configuration file located at [config/config.yaml](config/config.yaml) to set paths and parameters for different stages of the pipeline.
2. **Update `params.yaml`**: Adjust the training parameters in the [params.yaml](params.yaml) file.
3. **Update entity classes**: Modify the entity classes in [src/textSummarizer/entity](src/textSummarizer/entity) as needed.
4. **Update the configuration manager**: Update the configuration manager in [src/textSummarizer/config/configuration.py](src/textSummarizer/config/configuration.py) to reflect any changes in the configuration.
5. **Update the components**: Modify the components in [src/textSummarizer/components](src/textSummarizer/components) to implement new features or fix bugs.
6. **Update the pipeline**: Adjust the pipeline in [src/textSummarizer/pipeline](src/textSummarizer/pipeline) to integrate new components or modify existing ones.
7. **Update `main.py`**: Make necessary changes in [main.py](main.py) to ensure the main script runs correctly with the updated components and pipeline.
8. **Update `app.py`**: Modify [app.py](app.py) to update the web application interface or backend logic.

## Installation

To install the required dependencies, run:

```sh
pip install --use-pep517 -r requirements.txt
```

## Project Structure
```
.  
├── .gitignore   
├── README.md  
├── app.py  
├── artifacts/  
│   ├── data_ingestion/  
│   ├── data_transformation/  
│   ├── data_validation/  
│   ├── model_evaluation/  
│   ├── model_trainer/  
├── config/  
│   └── config.yaml  
├── logs/  
│   └── running_logs.log  
├── main.py  
├── params.yaml  
├── requirements.txt  
├── setup.py  
├── src/  
│   ├── textSummarizer/  
│   │   ├── __init__.py  
│   │   ├── components/  
│   │   ├── config/  
│   │   ├── constants/  
│   │   ├── entity/  
│   │   ├── logging/  
│   │   ├── pipeline/  
│   │   └── utils/  
├── static/  
│   ├── icon/  
│   ├── js/  
├── template.py  
└── templates/  
    └── index.html  
```
## Usage
Running the Application
To run the application, execute:
```
python app.py
```
Training the Model
To train the model, execute:
```
python app.py
```
## Configuration
config.yaml
Update the `config.yaml` file to configure the paths and parameters for different stages of the pipeline.

params.yaml
Update the `params.yaml` file to set the training parameters.

## Logging
Logs are stored in the `running_logs.log` file.