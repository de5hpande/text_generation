# 🦙 Fine-Tuning the Llama Model with Unsloth 🚀

## 📌 Project Overview
This project demonstrates how to **fine-tune the Llama-3 model** using **Unsloth** and deploy it via a **FastAPI-based inference server**. The model is optimized for efficient inference with **2x faster performance** and **70% less memory consumption**! 💡

## 🔥 Key Features
✅ Fine-tunes **Llama-3.2-3B** with **Unsloth** for optimal performance 🚀  
✅ Deploys the fine-tuned model using **FastAPI** 🌍  
✅ Supports **customizable text generation** (prompt, max tokens, temperature) 📜  
✅ GPU acceleration enabled for **fast inference** ⚡  
✅ Efficient memory usage, reducing computational costs 💾  

## 🛠️ Setup & Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Install Dependencies
Make sure you have **Python 3.10+** installed. Then, install the required packages:
```bash
pip install fastapi uvicorn torch transformers unsloth
```

### 3️⃣ Run the FastAPI Server
Start the inference API using **Uvicorn**:
```bash
uvicorn Fastapi_Llama_Inference:app --host 0.0.0.0 --port 8000 --reload
```

### 4️⃣ Access the API
Once the server is running, open your browser or use **Postman** to test the API:
📌 **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
📌 **Redoc UI**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)  

## 🚀 API Usage
### **Endpoint: `POST /generate`**
Send a **JSON request** to generate text:
```json
{
  "prompt": "Tell me a fun fact about space!",
  "max_length": 200,
  "temperature": 0.7
}
```
### **Response Example**
```json
{
  "response": "Did you know that a day on Venus is longer than a year on Venus? 🌌"
}
```

## 📌 Model & Training Details
- **Base Model**: Llama-3.2-3B
- **Fine-Tuning Framework**: Unsloth 🦥
- **Performance Boost**: 2x Faster 🚀, 70% Less Memory 💾
- **Hardware Used**: GPU-enabled environment (CUDA support recommended) ⚡

## 🤝 Contributing
Want to improve this project? Feel free to **fork** the repo and submit a PR! 🔥

## 📜 License
This project is licensed under the **MIT License** 📄

---
💡 **Developed by [Your Name]** | 🛠️ **Powered by FastAPI & Unsloth** 💙
