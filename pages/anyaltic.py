import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Plotting Demo")

st.title('Analytics')

# Load dataset and feature text
new_df = pd.read_csv('dataset/data_viz1.csv')
feature_text_data = pickle.load(open('dataset/feature_dict.pkl', 'rb'))

# Geomap
numeric_cols = ['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']
group_df = new_df.groupby('sector')[numeric_cols].mean()

st.header('Sector Price per Sqft Geomap')
fig = px.scatter_mapbox(group_df,
                        lat="latitude",
                        lon="longitude",
                        color="price_per_sqft",
                        size='built_up_area',
                        color_continuous_scale=px.colors.cyclical.IceFire,
                        zoom=10,
                        mapbox_style="open-street-map",
                        width=1200,
                        height=700,
                        hover_name=group_df.index)

st.plotly_chart(fig, use_container_width=True)

# WordCloud
st.header('Features Wordcloud')

st.header('Features Wordcloud by Sector')

sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0, 'overall')

selected_sector_wc = st.selectbox('Select Sector for Wordcloud', sector_options)

if selected_sector_wc == 'overall':
    feature_text = ' '.join(feature_text_data.values())  # Combine all sector texts
else:
    feature_text = feature_text_data.get(selected_sector_wc, 'No data for this sector')

if feature_text.strip():  # Avoid blank wordclouds
    wordcloud = WordCloud(width=800, height=800,
                          background_color='black',
                          stopwords=set(['s']),
                          min_font_size=10).generate(feature_text)

    fig_wc, ax = plt.subplots(figsize=(8, 8), facecolor=None)
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    plt.tight_layout(pad=0)
    st.pyplot(fig_wc)
else:
    st.warning("No wordcloud data available for this sector.")

st.header('Area Vs Price')

property_type=st.selectbox('property type',['Flat','house'])

if property_type == 'house':
    fig1= px.scatter(new_df[new_df['property_type'] == 'house'],x='built_up_area',y='price',color='bedRoom', title="Area Vs Price")
    st.plotly_chart(fig1, use_container_width=True)
else:
    fig2 = px.scatter(new_df[new_df['property_type'] == 'flat'], x='built_up_area', y='price', color='bedRoom',title="Area Vs Price")
    st.plotly_chart(fig2, use_container_width=True)

st.header('PIE chart')
sector_option=new_df['sector'].unique().tolist()
sector_option.insert(0,'Overall')

select_sector=st.selectbox('select sector',sector_option)
if select_sector=='Overall':
      fig1=px.pie(new_df,names='bedRoom')
      st.plotly_chart(fig1, use_container_width=True)
else:
    fig2=px.pie(new_df[new_df['sector']==select_sector],names='bedRoom')
    st.plotly_chart(fig2, use_container_width=True)

st.header('Side by Side BHK price comparison')

fig3 = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price', title='BHK Price Range')

st.plotly_chart(fig3, use_container_width=True)

st.header('Side by Side Distplot for property type')

fig3 = plt.figure(figsize=(10, 4))
sns.distplot(new_df[new_df['property_type'] == 'house']['price'],label='house')
sns.distplot(new_df[new_df['property_type'] == 'flat']['price'], label='flat')
plt.legend()
st.pyplot(fig3)
