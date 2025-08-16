import nltk
import string
import random
from nltk.tokenize import sent_tokenize
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from responses import casual_responses  # Make sure this is a dictionary

nltk.download("punkt")

# Load the ISRO knowledge base
with open("knowledge_base.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

# Chunking function – 3 sentences per chunk
def chunk_text(text, chunk_size=3):
    sentences = sent_tokenize(text)
    return [' '.join(sentences[i:i+chunk_size]) for i in range(0, len(sentences), chunk_size)]

# Basic preprocessing
stemmer = PorterStemmer()

def preprocess(text):
    return ' '.join(
        stemmer.stem(word.lower()) for word in text.split() if word not in string.punctuation
    )

# Prepare chunks and vectorize
chunks = chunk_text(raw_text)
preprocessed_chunks = [preprocess(chunk) for chunk in chunks]
vectorizer = TfidfVectorizer().fit(preprocessed_chunks)
chunk_vectors = vectorizer.transform(preprocessed_chunks)

# Main response logic
def get_response(user_input):
    key = user_input.lower().strip()

    # Handle casual replies
    for phrase in casual_responses:
        if phrase in key:
            return random.choice(casual_responses[phrase])

    # Semantic match with knowledge base
    processed_input = preprocess(user_input)
    input_vec = vectorizer.transform([processed_input])
    similarity = cosine_similarity(input_vec, chunk_vectors)
    max_score = similarity.max()

    if max_score > 0.2:
        best_match = similarity.argmax()
        return chunks[best_match]
    else:
        return "I'm not sure how to respond to that. Could you rephrase your question?"
