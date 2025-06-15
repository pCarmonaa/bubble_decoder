# BubbleDecoder

A service that analyzes social media content to identify algorithmic bias and bubble filters by examining topics, emotional tone, sentiment, language style, and polarization.

## Setup

1 Service setup

1.1 Create venv (optional):
```bash
python3 -m venv venv
source venv/bin/activate
```

1.2. Install dependencies:
```bash
pip install -r requirements.txt
```

2 Run the service:
```bash
python app.py
```

3 The API will be available at `http://localhost:5000`

## API Usage

POST `/analyze_bubble_map`
- Body: `{"content": "Your social media post content here"}`
- Returns: Analysis results with topic, sentiment, emotional tone, language style, and polarization 