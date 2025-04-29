# [🌐 Visit WhisperLytics Live](https://whisperlytics-9cly7mcd9yzoh2doercqxn.streamlit.app/)


# WhisperLytics 📊💬
**The Ultimate WhatsApp Chat Analyzer**

---

## 📖 Overview
**WhisperLytics** is a powerful, interactive **WhatsApp Chat Analyzer** built with **Streamlit**, **Python**, and data visualization libraries.  
It helps users dive deep into their personal or group conversations, uncover patterns, discover trends, and visualize interactions — all in a few clicks!

---

## 🚀 Features
- 📄 **Upload and Process** your exported WhatsApp chat `.txt` files easily.
- 📈 **Key Stats** like number of messages, words, media files shared, and links sent.
- 📅 **Monthly and Daily Timeline Analysis**.
- 📆 **Activity Maps** — discover your most active days and months.
- 🔥 **Weekly Heatmap** to visualize chat activity throughout the day.
- 👑 **Most Active Users** detection (for group chats).
- ☁️ **WordCloud Generation** to visualize frequent words.
- 📚 **Most Common Words** listing.
- 😂 **Emoji Analysis** — find out your most used emojis.
- 🎨 **Beautiful Visualizations** using **Matplotlib** and **Seaborn**.
- 🛡️ **Stop Words Filtering** for better word cloud and stats.

---

## 🛠️ How It Works
### 1. Preprocessing (`preprocessor.py`)
- Cleans and parses raw WhatsApp `.txt` chat exports.
- Extracts date, time, user names, and messages.
- Adds additional metadata like year, month, day name, and time period.

### 2. Data Analysis (`helper.py`)
- **Statistics fetching** (messages, words, media, links).
- **User-based filtering** (analyze individual users or the entire group).
- **Timeline creation** for daily and monthly trends.
- **Activity heatmaps** to visualize chat frequency by time slots.
- **Most common words** and **emoji analysis**.

### 3. Frontend Application (`app.py`)
- Built with **Streamlit** for an intuitive and interactive web experience.
- Upload file ➞ Choose user ➞ Explore rich visualizations and dataframes!

---

## 📂 Project Structure
```bash
WhisperLytics/
│
├── app.py          # Streamlit web application
├── helper.py       # Core analysis and visualization functions
├── preprocessor.py # Chat preprocessing and cleaning
├── stop_hinglish.txt # Stop words list for wordcloud cleaning
├── README.md       # Project documentation (you're reading it!)
└── requirements.txt # (optional) Python dependencies
```

---

## 🔧 Installation
```bash
# Clone the repository
git clone https://github.com/your-username/WhisperLytics.git

# Navigate to the project directory
cd WhisperLytics

# Install required libraries
pip install -r requirements.txt

# Start the Streamlit app
streamlit run app.py
```

> 📌 Make sure you have Python 3.7+ installed.

---

## 📋 Requirements
- **streamlit**
- **pandas**
- **matplotlib**
- **seaborn**
- **wordcloud**
- **urlextract**
- **emoji**

---

## 🖼️ Video Tutorial
| Upload Chat | Timeline Analysis | Word Cloud |
| :---: | :---: | :---: |


[streamlit-app-2025-04-29-01-04-39.webm](https://github.com/user-attachments/assets/293da40c-999e-449c-bbb2-bada067c4961)


---

## ✨ Future Enhancements
- Multi-platform chat support (Telegram, Signal)
- Sentiment Analysis (Positive/Negative/Neutral messages)
- User mentions and hashtag tracking
- Exportable reports (PDF/Excel)

---

## 👨‍💻 Author
**Developed by:** [Shahzaib Ali]  
🔗 *Feel free to connect!* (add your LinkedIn, GitHub, or Portfolio link)


---



> *WhisperLytics — Because every chat tells a story!* 🌟

