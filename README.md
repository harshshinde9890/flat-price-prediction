
# 🏢 Flat Price Prediction App 🏘️
This is an end-to-end Machine Learning project designed to predict the price of a flat based on input features like location, area, number of bedrooms, bathrooms, etc. The application also includes data visualization, price analytics, and a recommendation engine to provide a more complete experience.

The project is deployed with a clean UI built using Streamlit, making it easy and interactive for users to predict prices instantly.
# ✅ Key Features <br>
    📊 Predicts flat prices based on user input  
    🔍 Interactive visualizations of dataset insights  
    📈 Price recommendation based on similar properties  
    🖥️ Streamlit-based frontend UI for seamless experience  
    🧠 Trained ML model using Scikit-Learn  
    💾 Model serialized using Pickle


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

# 🛠️ Technologies Used
        Python – Core programming language for data processing and model development
        Pandas – Data analysis and manipulation
        NumPy – Numerical computations
        Matplotlib & Seaborn – Data visualization and analytics
        Scikit-learn (sklearn) – Machine Learning model building and evaluation
        Streamlit – Web-based interactive UI for deploying the ML model
        Pickle – Saving and loading trained ML models
        Jupyter Notebook – Research and exploratory data analysis (EDA)
        CSV – Dataset format for storing flat and geolocation data

# 📚 Required Libraries
Make sure the following Python libraries are installed before running the project:

        pandas
        numpy
        matplotlib
        seaborn
        scikit-learn
        streamlit
        pickle-mixin
