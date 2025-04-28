import streamlit as st
import helper
import preprocessor
import matplotlib.pyplot as plt
from wordcloud import WordCloud
st.sidebar.title("WhatsApp Chat Analyzer")
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)
    st.dataframe(df)

    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"Overall")
    selected_user = st.sidebar.selectbox("Show analysis wrt", user_list)
    if st.sidebar.button("Show Analysis"):

        num_messages, words, media_messages, total_links = helper.fetch_stats(selected_user, df)
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words  ")
            st.title(words)
        with col3:
            st.header("Media Shared")
            st.title(media_messages)
        with col4:
            st.header("Links Shared")
            st.title(total_links)

        st.title("Monthly TimeLine")
        timeline = helper.monthly_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'], color='green')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)
        if selected_user == 'Overall':
            st.title('Most Active Users')

            x, new_df = helper.most_busy_user(df)
            fig, ax = plt.subplots()
            col1, col2 = st.columns(2)
            with col1:
                ax.bar(x.index, x.values, color="#6DE1D2")

                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)

            # Word cloud
            st.title("Word Cloud")
            df_wc = helper.create_wordcloud(selected_user,df)
            fig, ax = plt.subplots()
            ax.imshow(df_wc)
            st.pyplot(fig)

            # most common words
            most_common_df = helper.most_common_words(selected_user, df)
            st.title("Most Common Words")
            st.dataframe(most_common_df)
            fig, ax = plt.subplots()
            ax.barh(most_common_df[0], most_common_df[1])
            plt.xticks(rotation='vertical')

            st.pyplot(fig)

            # emoji Analysis
            st.title("Emoji Analysis")
            emoji_df = helper.emoji_helper(selected_user, df)
            col1, col2 = st.columns(2)

            with col1:
                st.dataframe(emoji_df)

            with col2:
                fig, ax = plt.subplots()
                ax.pie(emoji_df[1].head(), labels=emoji_df[0].head(), autopct="%0.2f")
                st.pyplot(fig)

