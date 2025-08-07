import streamlit as st
from PIL import Image

# Optional: add logo or banner
# image = Image.open('your_image_path.png')
# st.image(image, use_column_width=True)

# Title with emoji
st.markdown("<h1 style='text-align: center; color: #f63366;'>🏠 Smart Flat Explorer</h1>", unsafe_allow_html=True)

# Subheading
st.markdown("### 🔍 Welcome to your personalized Property Analysis & Recommendation Dashboard!")

# Description Box
with st.container():
    st.markdown("""
    This app helps you:
    - 📊 **Analyze** flat and house listings with insightful visualizations
    - 📈 **Predict** property prices based on features like location, size, and amenities
    - 💡 **Recommend** the best apartments using machine learning & similarity scores

    Use the sidebar to explore each section:
    - **Analytic**: Explore interactive charts and trends
    - **Predict**: Estimate prices for your ideal flat
    - **Recommend Appartment**: Get top suggestions based on your preferences
    """)

# Call to Action
st.success("👉 Select a module from the sidebar to get started!")

# Footer / Note
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 14px;'>Created by Harsh Shinde | Powered by Streamlit & Machine Learning 🔧</p>", unsafe_allow_html=True)
