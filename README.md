<img width="832" height="367" alt="image" src="https://github.com/user-attachments/assets/ab62a680-c285-4afb-88e6-4883bacd8781" /># flat-price-prediction
🏢 Flat Price Prediction App 🏘️
This is an end-to-end Machine Learning project designed to predict the price of a flat based on input features like location, area, number of bedrooms, bathrooms, etc. The application also includes data visualization, price analytics, and a recommendation engine to provide a more complete experience.

The project is deployed with a clean UI built using Streamlit, making it easy and interactive for users to predict prices instantly.
# ✅ Key Features <br>
    📊 Predicts flat prices based on user input  
    🔍 Interactive visualizations of dataset insights  
    📈 Price recommendation based on similar properties  
    🖥️ Streamlit-based frontend UI for seamless experience  
    🧠 Trained ML model using Scikit-Learn  
    💾 Model serialized using Pickle

<img width="832" height="367" alt="image" src="https://github.com/user-attachments/assets/9d636bf3-f34d-442e-bcb0-e6cf77230f63" />

# 📂 Folder Structure

      flat-price-prediction/
        │
        ├── README.md                      - Project overview and instructions
        ├── gurgaon_sectors_coordinates.csv  - Dataset with latitude & longitude of sectors
        ├── home.py                        - Main Streamlit app file
        ├── latlong_scraper.py            - Script to scrape latitude & longitude
        │
        ├── pages/                         - Contains UI pages for the Streamlit app
        │   └── [Multiple UI Scripts]      - Streamlit pages (e.g., input forms, predictions)
        │
        ├── research/                      - Notebooks and datasets used for training
        │   ├── [Notebook].ipynb           - Jupyter notebooks for EDA, model training
        │   └── [Raw/Processed datasets]   - CSV files used in the notebooks
