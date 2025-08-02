class EmotionData:
    CATEGORIES = {
        'anger': ['anger', 'annoyance', 'disapproval', 'disgust'],
        'joy': ['joy', 'amusement', 'excitement', 'gratitude', 'pride', 'admiration', 'approval'],
        'sadness': ['sadness', 'grief', 'disappointment', 'remorse'],
        'fear': ['fear', 'nervousness'],
        'love': ['love', 'caring', 'desire'],
        'surprise': ['surprise', 'realization', 'curiosity'],
        'neutral': ['neutral']
    }

    WEIGHTS = {
        'anger': 1.3,
        'disgust': 1.2,
        'fear': 1.2,
        'sadness': 1.1,
        'grief': 1.1,
        'disappointment': 1.0,
        'remorse': 1.0,
        'annoyance': 0.9,
        'nervousness': 0.9,
        'confusion': 0.8,
        'surprise': 0.8,
        'joy': 0.7,
        'excitement': 0.7,
        'amusement': 0.7,
        'admiration': 0.6,
        'approval': 0.6,
        'gratitude': 0.6,
        'pride': 0.6,
        'curiosity': 0.5,
        'realization': 0.5,
        'relief': 0.5,
        'caring': 0.4,
        'desire': 0.4,
        'love': 0.4,
        'optimism': 0.4,
        'neutral': 0.3
    } 