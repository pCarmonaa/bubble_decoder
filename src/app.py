from container import Container
import nltk

from logging_config import setup_logging

if __name__ == '__main__':
    try:
        nltk.download('punkt', quiet=True)
        nltk.download('punkt_tab')
        nltk.download('stopwords', quiet=True)
        nltk.download('averaged_perceptron_tagger', quiet=True)
    except:
        raise Exception("Error downloading nltk resources")
    
    container = Container()
    
    setup_logging(container.settings().LOG_LEVEL)
    
    bubble_decoder_api = container.bubble_decoder_api()
    bubble_decoder_api.run(debug=True, host='0.0.0.0', port=5000) 