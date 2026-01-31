 🧠 AI MCQ Generator

## 🌟 Overview

**AI MCQ Generator** is an intelligent application that automatically generates **Multiple Choice Questions (MCQs)** from textual data using Python-based AI and NLP techniques.

The project is designed to help **students, educators, and content creators** quickly create quizzes and assessments from raw text or datasets. It also includes a **Streamlit-based web interface** for easy interaction and real-time MCQ generation.

---

## 🎯 Project Objectives

- Automatically generate MCQs from input text or datasets  
- Reduce manual effort in quiz and question paper creation  
- Provide an interactive and user-friendly web interface  
- Demonstrate practical use of AI/NLP in education technology  

---

## 🧠 System Architecture

### 🔹 High-Level Workflow

Input Text / Dataset

↓

Text Preprocessing

↓

Keyword / Concept Extraction

↓

Question Generation Logic

↓

Option Generation

↓

Final MCQs Output




---

## 🖥️ Application Flow (Streamlit App)

User Input (Text / File)

↓

Streamlit Interface

↓

AI / NLP Processing

↓

MCQ Generation Engine

↓

Display MCQs on Web App



---

## 📂 Repository Structure

| File | Description |
|-----|-------------|
| `MCQ_generator.ipynb` | Core logic for MCQ generation |
| `StreamlitAPP.py` | Streamlit web application |
| `data.txt` | Sample input text |
| `machinelearning.csv` | Dataset used for MCQ generation |
| `test.py` | Testing and experimentation script |
| `requirements.txt` | Project dependencies |

---

## 🛠️ Technologies Used
🛠️ Tech Stack Used
🐍 Programming Language — Python
<p align="left"> <img src="https://img.icons8.com/color/48/python--v1.png" alt="Python"/> </p>

Python is used for implementing the MCQ generation logic, data processing, and application backend.

📓 Development & Experimentation — Jupyter Notebook
<p align="left"> <img src="https://raw.githubusercontent.com/jupyter/design/main/logos/Square%20Logo/squarelogo-greytext-orangebody.svg" alt="Jupyter Notebook" width="70" /> </p>

Jupyter Notebook is used for prototyping, testing, and experimenting with MCQ generation logic.

🖥️ Web Application Framework — Streamlit
<p align="left"> <img src="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png" alt="Streamlit" width="130" /> </p>

Streamlit is used to build an interactive web interface that allows users to generate MCQs in real time.

📊 Data Handling — Pandas
<p align="left"> <img src="https://upload.wikimedia.org/wikipedia/commons/2/22/Pandas_mark.svg" alt="Pandas" width="90" /> </p>

Pandas is used for handling CSV datasets and structured input data.

🧠 NLP / AI Logic — Python NLP Utilities
<p align="left"> <img src="https://img.icons8.com/color/48/artificial-intelligence.png" alt="AI"/> </p>

Custom NLP logic is used for text preprocessing, keyword extraction, question formation, and option generation.

🔧 Version Control — Git & GitHub
<p align="left"> <img src="https://img.icons8.com/color/48/git.png" alt="Git"/> <img src="https://img.icons8.com/ios-glyphs/48/github.png" alt="GitHub"/> </p>

Git and GitHub are used for version control and project collaboration.

✅ Optional: Badge Version (Top of README)

If you want a clean one-line badge style (very popular on GitHub):

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
---

### 🖥️ Web Interface — Streamlit
<img src="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png" width="120"/>

Streamlit is used to build an interactive and lightweight web interface for real-time MCQ generation.

---

### 📊 Data Handling
<img src="https://upload.wikimedia.org/wikipedia/commons/2/22/Pandas_mark.svg" width="80"/>

Used for handling CSV datasets and structured data.

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/AnmolRajpoot25/AI_MCQ_GEnerator.git
cd AI_MCQ_GEnerator
2️⃣ Create Virtual Environment (Optional)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run the Streamlit App
streamlit run StreamlitAPP.py
```
📈 Example Use Cases
Generate MCQs for exams and quizzes

Create practice questions from textbooks

Automate question creation for e-learning platforms

Assist teachers in assessment design

