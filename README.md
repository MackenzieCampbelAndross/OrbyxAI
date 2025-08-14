OrbyxAI

Orbyx AI is an ISRO-focused chatbot built with Flask, NLP, and TF-IDF similarity search to
deliver accurate answers from a curated,auto-updated knowledge base. Designed for seamless
website integration with engaging UI/UX, it makes space exploration knowledge accessible
and interactive.


- Domain-specific: Specializes in ISRO-related knowledge.
- NLP-powered: Uses NLTK, TF-IDF, and cosine similarity.
- Auto-updating knowledge base via web scraping.
- Flask backend for easy integration into any website.
- Modern UI-ready: Designed for Particle.js and interactive designs.



FOLDER STRUCTURE

orbyx_ai/
│
├── orbyx.ai_web/        -> flask web app
├── scrapper.py          -> scraper script
├── urls.py              -> URL list
├── knowledge_base.txt   -> knowledge base
├── README.md            -> project readme
├── requirements.txt     -> dependencies
├── .gitignore           -> ignore unnecessary files
└── LICENSE              -> MIT license



INSTALLATION

1. Clone the Repository
   git clone https://github.com/yourusername/orbyx-ai.git
   cd orbyx-ai

2. Install Dependencies
   pip install -r requirements.txt

3. Run the App
   python app.py

4. Access the Chatbot
   Open your browser and go to:
   http://127.0.0.1:5000



REQUIREMENTS 

- Python 3.8+
- Flask
- NLTK
- scikit-learn
- BeautifulSoup4
- Requests



LICENSE

This project is licensed under the MIT License.



FUTURE PLANS

- Deploy to the web with a modern UI/UX.
- Add voice query support.
- Integrate advanced NLP models for more dynamic conversations.
