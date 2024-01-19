import streamlit as st
import pandas as pd

st.title('Streamlit File Upload Example')

# Uploading the CSV File
st.subheader('1. Upload CSV File')
df = st.file_uploader("Upload the CSV file:", type=['csv', 'xlsx'])

# Displaying the DataFrame
if df is not None:
    st.subheader('2. Display DataFrame')
    df = pd.read_csv(df)  # Read the CSV file
    st.write(df.head())  # Display the DataFrame in a table

# Working with Images
st.subheader('3. Upload Image')
img_file = st.file_uploader("Upload the Image file:", type=['png', 'jpeg'])
if img_file is not None:
    st.subheader('4. Display Image')
    st.image(img_file)

# Working with Videos
st.subheader('5. Upload Video')
video_file = st.file_uploader("Upload the Video file:", type=['mkv', 'mp4'])
if video_file is not None:
    st.subheader('6. Display Video')
    st.video(video_file, start_time=0)

# st.subheader('Working with Audio')
# audio_file = st.file_uploader("Upload the audio file : ", type = ['mp3', 'wav'])
# if audio_file is not None:
#     st.audio(audio_file.read())