
# Text Summarization Project

A comprehensive text summarization system that trains and deploys transformer-based models for automatic text summarization. This project provides a complete MLOps pipeline from data ingestion to web deployment.

![Python](https://img.shields.io/badge/Python-3.7%252B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68%252B-green)
![PyTorch](https://img.shields.io/badge/PyTorch-1.9%252B-red)
![Transformers](https://img.shields.io/badge/%F0%9F%A4%97%2520Transformers-4.0%252B-yellow)

---

## 📖 Overview

This project implements an end-to-end text summarization system that:

- Trains custom summarization models using transformer architectures
- Evaluates model performance with standard NLP metrics
- Deploys trained models via a FastAPI web interface
- Supports both REST API and web UI interactions

---

## 🚀 Features

- **4-Stage Training Pipeline:** Data ingestion → transformation → training → evaluation  
- **GPU Support:** Automatic CUDA detection for accelerated inference  
- **Web Interface:** User-friendly UI for text summarization  
- **REST API:** Programmatic access to summarization capabilities  
- **Production Ready:** Modular codebase following MLOps best practices  
- **Configurable:** Easy configuration management for different use cases  

---

## 🛠️ Installation

### Prerequisites

- Python 3.7+  
- `pip` package manager  
- (Optional) CUDA-enabled GPU for faster training/inference  

### Setup

1. **Clone the repository**

```bash
git clone https://github.com/your-username/text-summarizer.git
cd text-summarizer
```

2. **Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Project structure**

```bash
# The project uses a modular structure with these main components:
# - src/textSummarizer/          # Core ML components
# - templates/                   # Web UI templates  
# - config/                      # Configuration files
```

---

## 📁 Project Structure

```
text-summarizer/
├── src/textSummarizer/
│   ├── components/              
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   └── model_evaluation.py
│   ├── pipeline/               
│   │   ├── stage_1_data_ingestion_pipeline.py
│   │   ├── stage_2_data_transformation_pipeline.py
│   │   ├── stage_3_model_trainer_pipeline.py
│   │   ├── stage_4_model_evaluation.py
│   │   └── prediction_pipeline.py
│   ├── config/                 
│   │   └── configuration.py
│   └── logging/               
├── templates/                 
│   └── index.html
├── app.py                    
├── main.py                   
└── requirements.txt          
```

---

## 🎯 Usage

### Starting the Web Application

```bash
python app.py
```

- Web UI: [http://localhost:8080/ui](http://localhost:8080/ui)  
- API Docs: [http://localhost:8080/docs](http://localhost:8080/docs)  
- Base URL: `http://localhost:8080`

### Training the Model

**Option 1: Via Web Interface**

```bash
GET http://localhost:8080/train
```

**Option 2: Direct execution**

```bash
python main.py
```

### Making Predictions

**Via Web UI:**

- Navigate to [http://localhost:8080/ui](http://localhost:8080/ui)  
- Enter your text in the input box  
- Click `"Summarize"` to get the summary  

**Via API:**

```bash
curl -X POST "http://localhost:8080/predict"   -H "Content-Type: application/x-www-form-urlencoded"   -d "text=Your long article text goes here. This can be a news article, research paper, or any lengthy content that you want to summarize..."
```

**API Response:**

```json
{
  "summary": "This is the generated summary of your input text."
}
```

---

## 🔧 Configuration

The project uses a configuration management system that handles:

- **Model Parameters:** Architecture, tokenizer, training hyperparameters  
- **Data Paths:** Input data locations and output directories  
- **Training Settings:** Batch sizes, learning rates, epochs  
- **Inference Settings:** Beam search parameters, length constraints  

**Key inference parameters:**

```text
length_penalty: 0.8
num_beams: 8
max_length: 128 tokens
```

---

## 🏗️ Pipeline Stages

1. **Data Ingestion**
   - Downloads dataset files  
   - Extracts and validates data  
   - Prepares raw data for processing  

2. **Data Transformation**
   - Converts raw text to model-ready format  
   - Handles tokenization and encoding  
   - Splits data into training/validation sets  

3. **Model Training**
   - Initializes transformer model  
   - Configures training parameters  
   - Executes model training with checkpointing  

4. **Model Evaluation**
   - Evaluates model performance  
   - Calculates metrics (ROUGE scores)  
   - Generates evaluation reports  

5. **Prediction Pipeline**
   - Loads trained model and tokenizer  
   - Handles text preprocessing  
   - Generates summaries with beam search  

---

## 🚀 Performance

- **GPU Acceleration:** Automatic detection and utilization of CUDA  
- **Beam Search:** 8 beams for optimal quality/speed balance  
- **Memory Efficient:** Handles long texts with appropriate chunking  
- **Fast Inference:** Optimized pipeline for production use  

---

## 🤝 Contributing

We welcome contributions!  

**Development Setup**

1. Fork the repository  
2. Create a feature branch  
3. Make your changes  
4. Add tests if applicable  
5. Submit a pull request  

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- Hugging Face for the Transformers library  
- FastAPI for the web framework  
- PyTorch for the deep learning framework  

---

## 📞 Support

If you have any questions or run into issues:

- Check the existing Issues  
- Create a new issue with detailed description  
- Provide relevant code snippets and error messages  

⭐ If you find this project useful, please give it a star on GitHub!
