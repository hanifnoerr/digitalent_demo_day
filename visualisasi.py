import pandas as pd
import streamlit as st
from wordcloud import WordCloud
from wordcloud import STOPWORDS
import numpy as np
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False) #disable notif wordcloud

df=pd.read_csv('tweets_final.csv')
x = df['keyword'].unique()

menunya = st.sidebar.selectbox(
    'Menu:',
    ('Latar Belakang','Hasil')
)


if menunya == 'Latar Belakang' or menunya == '':
    st.title('Sosial Media 5')
    st.text('Hanif Noer Rofiq - 152236035100-1122')
    st.text('Handika Ramadhan - 152236035100-64')
    st.text('')
    st.markdown('Selected Theme')
    st.caption('NLP sentiment analysis')
    st.text('')
    st.markdown('Title of the Project')
    st.caption('Sentimen Analisis Data Sosial Media (Twitter)')
    st.text('')
    st.markdown('Background Summary')
    st.caption('Di era digital saat ini, sosial media mempunyai peran yang sangat penting dalam memberikan informasi karena masyarakat sering kali mengungkapkan pendapatnya melalui sosial media, baik itu terkait kehidupan pribadi mereka, ulasan suatu produk, kebijakan pemerintah maupun kejadian yang sedang berlangsung. Sentiment analytic ini adalah salah satu alat yang bisa membantu untuk membaca reaksi publik, memahami keinginan publik, dan menyusun kebijakan atau strategi komunikasi kepada masyarakat. Dengan menggunakan NLP dapat ditentukan sentimen masyarakat terhadap suatu kejadian atau kebijakan berdasarkan data dari social media dalam hal ini Twitter. Model dari hasil klasifikasi ini nantinya diharapkan akan membantu untuk memprediksi klasifikasi sentimen terhadap isu-isu di masa yang akan datang serta dapat digunakan untuk membuat counter policy atas current issue yang sedang hangat diperbincangkan.')
    st.text('')
    st.markdown('Tujuan')
    st.caption(' * Mengetahui simpulan dari tweet terkait suatu topik/tema')
    st.caption(' * Mengetahui sentimen masyarakat atas suatu topik/tema')

elif menunya == 'Hasil':

     option = st.selectbox(
          'Pilih keyword',
          (tuple(x)))

     df_topic=df[df['keyword'] == option]

     st.write('Banyak tweet terkait ' + option + ' : ' , df_topic.shape[0])

     text = " ".join(i for i in df_topic.text)
     stopwords = set(STOPWORDS)
     wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
     plt.figure( figsize=(15,10))
     plt.imshow(wordcloud, interpolation='bilinear')
     plt.axis("off")
     plt.show()
     st.pyplot()

     colors = np.array(["gray", 'orangered', 'hotpink', 'gold', 'teal', 'cornflowerblue'])

     plt.bar(df_topic.Sentiment.value_counts().index,df_topic.Sentiment.value_counts().values, color=colors)
     plt.title('Sentimen terkait kata kunci '+option)
     plt.show()
     st.pyplot()

     st.dataframe(df_topic)