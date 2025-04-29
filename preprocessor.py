import re
import pandas as pd


def preprocess(data):
    # Updated regex pattern to support:
    # - Format 1: [19/09/2023, 5:17:58 PM]
    # - Format 2: 1/26/23, 8:19 PM -
    # - Format 3: 20/08/2023, 10:43 am -
    pattern = r'(?:\[\d{1,2}/\d{1,2}/\d{2,4}, \d{1,2}:\d{2}(?::\d{2})?\s?[aApP][mM]\]|\d{1,2}/\d{1,2}/\d{2,4}, \d{1,2}:\d{2}(?::\d{2})?\s?[aApP][mM]\s?-)'

    # Split data into messages and date parts based on the regex pattern
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    # Create DataFrame
    df = pd.DataFrame({'user_message': messages, 'message_date': dates})

    # Clean unicode spaces and trailing characters
    df['message_date'] = df['message_date'].str.replace('\u202f', ' ', regex=True)
    df['message_date'] = df['message_date'].str.replace(' -', '', regex=False)
    df['message_date'] = df['message_date'].str.strip('[]')

    # Try parsing with different day/month formats
    def parse_date(val):
        for fmt in ("%d/%m/%Y, %I:%M:%S %p", "%d/%m/%Y, %I:%M %p", "%m/%d/%y, %I:%M %p"):
            try:
                return pd.to_datetime(val, format=fmt)
            except:
                continue
        return pd.NaT

    df['date'] = df['message_date'].apply(parse_date)

    # Split the user_message column into user and message
    users = []
    messages = []

    for message in df['user_message']:
        entry = re.split(r'([\w\W]+?):\s', message)
        if entry[1:]:  # User name exists
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message', 'message_date'], inplace=True)

    # Feature extraction
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    df['month_num'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute
    df['day_name'] = df['date'].dt.day_name()
    df['only_date'] = df['date'].dt.date

    # Time period feature
    period = []
    for hour in df['hour']:
        if hour == 23:
            period.append(f"{hour}-00")
        elif hour == 0:
            period.append("00-1")
        else:
            period.append(f"{hour}-{hour + 1}")
    df['period'] = period

    return df
