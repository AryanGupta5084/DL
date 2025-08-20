# 👤 Gender Classification from Fingerprints  

## 📖 Introduction  
This project is a **deep learning application** that predicts **gender from fingerprint images**.  
It uses a **Convolutional Neural Network (CNN)** trained on the **[SOCOFing dataset](https://www.kaggle.com/datasets/ruizgara/socofing)** and provides a **Streamlit web interface** for uploading and classifying fingerprints in real time.  

## 📑 Table of Contents  
- [Introduction](#-introduction)  
- [Dataset](#-dataset)  
- [Installation](#-installation)  
- [Usage](#-usage)  
- [Features](#-features)  
- [Project Structure](#-project-structure)  
- [Dependencies](#-dependencies)  
- [Configuration](#-configuration)  
- [Examples](#-examples)  
- [Troubleshooting](#-troubleshooting)  
- [Contributors](#-contributors)  
- [License](#-license)  

## 📂 Dataset  

This project uses the **[SOCOFing dataset](https://www.kaggle.com/datasets/ruizgara/socofing)**, which contains **6,000 fingerprint images** (real and synthetically altered).  

### Option 1: Manual Download  
1. Download the dataset from Kaggle:  
   [👉 SOCOFing Dataset on Kaggle](https://www.kaggle.com/datasets/ruizgara/socofing)  

2. Extract the dataset into your project folder so the structure looks like this:  
   ```
   SOCOFing/
   ├── Real/
   └── Altered/
       ├── Altered-Easy/
       ├── Altered-Medium/
       └── Altered-Hard/
   ```

### Option 2: Kaggle API (Automatic Download)  
1. Install the Kaggle API:  
   ```bash
   pip install kaggle
   ```  

2. Create a Kaggle API token:  
   - Go to your [Kaggle Account Settings](https://www.kaggle.com/account)  
   - Click **Create New API Token**  
   - This downloads a file named `kaggle.json`  

3. Place `kaggle.json` in:  
   - **Linux/Mac**: `~/.kaggle/kaggle.json`  
   - **Windows**: `C:\Users\<YourUsername>\.kaggle\kaggle.json`  

4. Download and unzip the dataset automatically:  
   ```bash
   kaggle datasets download -d ruizgara/socofing
   unzip socofing.zip -d .
   ```

Now your dataset is ready in the `SOCOFing/` folder.  

## ⚙️ Installation  
1. Clone this repository:  
   ```bash
   git clone https://github.com/AryanGupta5084/DL.git
   cd DL
   ```  

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  

3. Ensure you have the **SOCOFing dataset** placed in the correct folder structure (see above).  

## 🚀 Usage  

### 1. Train the Model  
Run the training script to build and save the CNN model (`trained_model.h5`):  
```bash
python train.py
```  

### 2. Run the Web App  
Once the model is trained, launch the Streamlit app:  
```bash
streamlit run app.py
```  

### 3. Upload Fingerprints  
- Upload a fingerprint image (`.jpg`, `.jpeg`, `.png`)  
- The app will classify it as **Male** or **Female**  

## ✨ Features  
- CNN-based gender classification from fingerprints  
- Training on multiple difficulty levels of the SOCOFing dataset  
- Real-time predictions via a Streamlit web interface  
- Automatic preprocessing (grayscale conversion, resizing, normalization)  
- Model saved in `trained_model.h5` for reuse  

## 📂 Project Structure  
```
DL/
├── app.py              # Streamlit web app for predictions
├── train.py            # CNN training script
├── requirements.txt    # Dependencies
├── trained_model.h5    # Saved model (created after training)
└── SOCOFing/           # Dataset (not included in repo)
```

## 📦 Dependencies  
Main dependencies (from `requirements.txt`):  
- numpy  
- pandas  
- matplotlib, seaborn  
- scikit-learn  
- tensorflow, keras  
- opencv-python  
- streamlit  
- Pillow  

Install all with:  
```bash
pip install -r requirements.txt
```  

## ⚙️ Configuration  
- **Image size**: 96×96 pixels  
- **Batch size**: 128  
- **Epochs**: 30 (with early stopping)  
- **Optimizer**: Adam (learning rate = 0.001)  
- **Loss function**: Categorical Crossentropy  

## 🖼️ Examples  
1. **Upload a fingerprint:**  
   ![example-fingerprint](1__M_Left_index_finger.jpg) 
2. **Predicted Output in Streamlit:**  
   ```
   Predicted Gender: Male
   ```  

## 🛠️ Troubleshooting  
- **Error: trained_model.h5 not found** → Run `python train.py` before launching the app.  
- **Dataset missing** → Ensure the SOCOFing dataset is properly downloaded and structured.  
- **OpenCV errors** → Check that fingerprint images are valid grayscale images.  

## 👥 Contributors  
- **Aryan Gupta** — Developer & Maintainer  
