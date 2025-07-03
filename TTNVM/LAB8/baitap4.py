# tải các gói dữ liệu cần thiết:
import nltk
nltk.download('brown')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

from textblob import TextBlob

# Nhập văn bản cần phân tích
text = "I love NTTU and teacher Duc Bui Tien"

# Tạo đối tượng TextBlob
blob = TextBlob(text)

# Phân tích cảm xúc
sentiment = blob.sentiment

# In ra kết quả
print(f"Độ phân cực: {sentiment.polarity}")
print(f"Độ chủ quan: {sentiment.subjectivity}")
