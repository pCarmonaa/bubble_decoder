from flask import Flask, request, jsonify
from flask_cors import CORS
from domain.ports.driving.content_analyzer import ContentAnalyzer
from infrastructure.web.serializers.generic_object_serializer import GenericObjectSerializer

class BubbleDecoderAPI:
    def __init__(self, content_analyzer: ContentAnalyzer):
        self.app = Flask(__name__)
        CORS(self.app)
        self.content_analyzer = content_analyzer
        self._setup_routes()
    
    def _setup_routes(self):
        @self.app.route('/health', methods=['GET'])
        def health_check():
            return jsonify({'status': 'healthy', 'service': 'BubbleDecoder'})

        @self.app.route('/analyze_bubble_map', methods=['POST'])
        def analyze_bubble_map():
            try:
                data = request.get_json()
                
                if not data or 'content' not in data:
                    return jsonify({'error': 'Content field is required'}), 400
                
                content = data['content']
                
                if not isinstance(content, str):
                    return jsonify({'error': 'Content must be a string'}), 400
                
                analysis_result = self.content_analyzer.analyze_bubble_map(content)
                
                return jsonify({
                    'success': True,
                    'analysis': GenericObjectSerializer.to_dict(analysis_result)
                }), 200
                
            except ValueError as e:
                return jsonify({'error': str(e)}), 400
            except Exception as e:
                return jsonify({'error': 'Internal server error'}), 500
    
    def run(self, debug=True, host='0.0.0.0', port=5000):
        self.app.run(debug=debug, host=host, port=port) 