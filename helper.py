from urlextract import URLExtract
from wordcloud import WordCloud
from collections import Counter
import pandas as pd
import emoji
import unicodedata
extract = URLExtract()


def clean_message(msg):
    if isinstance(msg, str):
        # Normalize and remove all invisible/control characters like \u200e
        msg = unicodedata.normalize("NFKD", msg)
        msg = ''.join(ch for ch in msg if not unicodedata.category(ch).startswith("C"))
        return msg.strip().lower()
    return ""

def fetch_stats(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    num_messages = df.shape[0]

    words = []
    for message in df['message']:
        words.extend(message.split())

    # Clean each message
    df['clean_message'] = df['message'].apply(clean_message)

    # Match media messages after cleaning
    media_phrases = ['<media omitted>', 'image omitted']
    num_media_messages = df[df['clean_message'].isin(media_phrases)].shape[0]

    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))

    return num_messages, len(words), num_media_messages, len(links)


def most_busy_user(df):
    x = df['user'].value_counts().head()
    new_df = round(df['user'].value_counts()/df.shape[0]*100, 2).reset_index().rename(columns={'index':'name', 'user':'percent'})

    return x, new_df


def create_wordcloud(selected_user, df):
    f = open('stop_hinglish.txt', 'r')

    stop_words = f.read()
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    temp = df[df['user'] != 'group_notification']

    temp = temp[temp['message'] != '<Media omitted>\n']
    temp = temp[temp['message'] != 'image ommited']
    temp = temp[temp['message'] != 'message deleted']

    def remove_stop_words(message):
        y = []
        for word in message.lower().split():
            if word not in stop_words or word != 'https' or word != 'message deleted' or word != 'deleted':
                y.append(word)
        return " ".join(y)

    temp['message'] = temp['message'].apply(remove_stop_words)
    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')

    df_wc = wc.generate(temp['message'].str.cat(sep=" "))
    return df_wc


def most_common_words(selected_user, df):
    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']
    f = open('stop_hinglish.txt', 'r')
    stop_words = f.read()
    words = []
    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)
    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df


def emoji_helper(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if emoji.is_emoji(c)])

    emoji_counter = Counter(emojis)
    emoji_df = pd.DataFrame(emoji_counter.most_common(len(emoji_counter)))

    return emoji_df


def monthly_timeline(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    time_line = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()

    time = []

    for i in range(time_line.shape[0]):
        time.append(time_line['month'][i] + "-" + str(time_line['year'][i]))
    time_line['time'] = time
    return time_line


def daily_timeline(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    daily_timeline = df.groupby('only_date').count()['message'].reset_index()

    return daily_timeline


def weekly_activity_map(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['day_name'].value_counts()


def month_activity_map(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['month'].value_counts()


def activity_heatmap(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    user_heatmap = df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)

    return user_heatmap
