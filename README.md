# 🧠 Stock Sentiment Analysis — Backend (Flask + Hugging Face)

This is the **backend** of the Stock Sentiment Analysis project.  
It uses **Flask** for the REST API and **Hugging Face Transformers** to perform real-time sentiment analysis on news headlines related to a specific company.

---

## 🚀 Features

- Fetches company news using the NewsAPI  
- Performs **sentiment analysis** using Hugging Face Transformers  
- Returns sentiment breakdown (positive, negative, neutral) as JSON  
- CORS enabled for connection with the React frontend  
- Modular Flask structure for scalability  

---

## 🛠️ Tech Stack

| Component | Technology |
|------------|-------------|
| Backend Framework | Flask |
| ML Model | Hugging Face Transformers |
| Language | Python |
| Data Fetching | NewsAPI |
| Hosting (Optional) | Render / Railway |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/CodeWithAkash/stock-sentiment-backend.git
cd stock-sentiment-backend
