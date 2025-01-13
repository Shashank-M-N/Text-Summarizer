# Text Summarizer  

A **modular** Python-based **Text Summarizer** that processes raw text through multiple stages, including data ingestion, validation, transformation, model training, and evaluation to generate high-quality summaries. The system allows for easy customization and tuning of parameters for improved performance, making it suitable for various summarization tasks.  

>All operations, including training and summarization, are carried out locally on my machine, ensuring complete data privacy and control.

## Table of Contents  

- [Text Summarizer](#text-summarizer)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
    - [Training Details](#training-details)
  - [Features](#features)
  - [Installation Instructions](#installation-instructions)
  - [Usage Instructions](#usage-instructions)
    - [Running the Application](#running-the-application)
  - [Configuration](#configuration)
  - [Logs](#logs)
  - [Project Structure](#project-structure)

## Project Overview  

This project leverages a **modular coding approach** to build a text summarization pipeline. Each part of the process, from data ingestion to model evaluation, is handled by separate stages, making the system easy to extend and modify. The text summarizer can be fine-tuned by adjusting hyperparameters and configurations to suit specific use cases. All relevant parameters can be customized through `config.yaml` and `params.yaml` files.  

### Training Details  

- The model is **fine-tuned** on the **[Samsum dataset](https://github.com/Shashank-M-N/Datasets/raw/main/summarizer-data.zip)**, which consists of human-written dialogues and their summaries.  
- It uses the **`google/pegasus-cnn_dailymail`** pre-trained transformer model for abstractive summarization. This model is optimized for handling long text inputs and generating concise summaries.  
- **Note**: The pre-trained model provided may not be highly accurate as it was trained on limited resources. Training took approximately **13 hours**, so be prepared if you plan to train the model from scratch. To use the model, download the zipped folder from the link, unzip it, and place it in the same directory as `app.py`.  

## Features  

- **Modular Pipeline**: The system is divided into clear stages—data ingestion, validation, transformation, model training, and evaluation—allowing for easy modifications and extensions.  
- **Configurable Parameters**: Easily tune parameters such as learning rate, batch size, and input-output directories. The configurations are stored in `config.yaml` and `params.yaml` files.  
- **Automatic Summarization**: Converts long text into concise, meaningful summaries using advanced algorithms.  
- **Pre-Trained Model**: Use a pre-trained model (link provided below) or train the model on your own dataset.  
- **Evaluation Metrics**: The system evaluates the performance of the model using standard metrics to ensure effective summarization.  

## Installation Instructions  

To install the project, follow these steps:  

1. Clone the repository:  
   ```bash  
   git clone https://github.com/Shashank-M-N/text-summarizer.git  
   cd text-summarizer  
   ```  

2. Create a virtual environment (optional but recommended):  
   ```bash  
   python -m venv venv  
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`  
   ```  

3. Install the required dependencies:  
   ```bash  
   pip install --use-pep517 -r requirements.txt  
   ```  
   > **Note**:  
   > - If you are using **Linux** and encounter an error related to `-e .`, use the following command instead:  
   >   ```bash  
   >   sudo pip install --use-pep517 -r requirements.txt  
   >   ```  
   > - Using the `--use-pep517` flag ensures compatibility and avoids potential warnings during dependency installation.

## Usage Instructions  

### Running the Application  

1. **Train the Model**:  
   - Before using the summarizer, you **must train the model**.  
   - You can either train the model using your dataset or download my pre-trained model via this [link](https://mega.nz/file/uZ5mWSbL#pDyM8CGp60mVusBR_lGX5i8C5sH95EzzI7b82clD-nw).  
     > **Note**: The pre-trained model was fine-tuned on the Samsum dataset and may not be highly accurate but performs decently. Training took **13 hours**, so be prepared for a long training time if starting from scratch.  
     - To use the pre-trained model, download the zipped folder from the link, unzip it, and place the folder in the same directory as `app.py`.  
   - To train the model, follow these steps:  
     - Open the application by running:  
       ```bash  
       python app.py  
       ```  
     - Navigate to:  
       ```  
       http://127.0.0.1:8080/summarizer  
       ```  
     - On the webpage, **change the default option from "Use Default Model" to "Train Model"** from the dropdown menu, which will display a **"Training" button**. Click the button to start the training process.  

   Alternatively, you can also train the model by running:  
   ```bash  
   python main.py  
   ```

2. **Summarize Text**:  
   - Once the model is trained or the pre-trained model is downloaded:  
     - **Re-run the application** by running:  
       ```bash  
       python app.py  
       ```  
     - Navigate to:  
       ```  
       http://127.0.0.1:8080/summarizer  
       ```  
     - Enter your text into the provided input field.  
     - Click the **"Summarizer" button** to generate a summary.  
   - The generated summary will appear below the input field.  

3. **Monitor Logs**:  
   - During both training and summarization, logs are printed to the terminal to provide real-time feedback on the application's status and processes.  
   - At a later time, you can refer to `logs/running_logs.log` to review the terminal outputs.

## Configuration  

The system uses two primary configuration files:  

- **`config.yaml`**: Defines all the directories, file paths, and other necessary configurations for the pipeline.  
- **`params.yaml`**: Contains parameters like batch size, learning rate, number of epochs, etc., which can be tuned as needed.  

Both files are located in the root directory and can be edited to customize the behavior of the pipeline.  

## Logs  

Logs for the pipeline and application are stored in the `logs` folder, specifically in the `running_logs.log` file. This file provides detailed information about the execution of each stage, making debugging and monitoring easier.  

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

This project structure shows the modular organization, including source code (`src`), configuration (`config.yaml`), logs (`running_logs.log`), and static files for the web interface (`templates` and `static`).  

---