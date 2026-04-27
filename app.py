import logging
import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from ai import categorize

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create Flask app
app = Flask(__name__, template_folder="html")

# Load configuration
app.config['JSON_SORT_KEYS'] = False
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024  # 16KB max request size

# Enable CORS for API requests
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Security headers middleware
@app.after_request
def set_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    return response

# Home page
@app.route("/")
def home():
    logger.info("Home page accessed")
    return render_template("firstpage.html")

# Results page
@app.route("/results")
def results():
    logger.info("Results page accessed")
    return render_template("result.html")

# API: Categorize items
@app.route("/api/categorize", methods=["POST"])
def api_categorize():
    """Categorize a single grocery item"""
    try:
        data = request.get_json(silent=True)
        
        # Validation
        if not data or "item" not in data:
            logger.warning("Missing 'item' in request")
            return jsonify({"error": "missing item"}), 400
        
        item = data["item"]
        if not isinstance(item, str):
            logger.warning(f"Invalid item type: {type(item)}")
            return jsonify({"error": "item must be a string"}), 400
        
        item = item.strip()[:200]  # Limit to 200 chars for security
        if not item:
            logger.warning("Empty item provided")
            return jsonify({"error": "item cannot be empty"}), 400
        
        # Categorize
        category = categorize(item)
        logger.info(f"Categorized '{item}' as '{category}'")
        
        return jsonify({
            "success": True,
            "item": item,
            "category": category
        }), 200
    
    except Exception as e:
        logger.error(f"Error in categorization: {str(e)}")
        return jsonify({"error": "internal server error"}), 500

# Legacy endpoint support
@app.route("/add", methods=["POST"])
def add():
    """Legacy endpoint - forwards to /api/categorize"""
    return api_categorize()

# Health check endpoint
@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy", "service": "GrocerySort"}), 200

# Error handlers
@app.errorhandler(404)
def not_found(error):
    logger.warning(f"404 error: {request.url}")
    return jsonify({"error": "not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"500 error: {str(error)}")
    return jsonify({"error": "internal server error"}), 500

if __name__ == "__main__":
    debug_mode = os.environ.get("FLASK_DEBUG", "False") == "True"
    port = int(os.environ.get("PORT", 5000))
    host = os.environ.get("HOST", "0.0.0.0")
    
    logger.info(f"Starting GrocerySort on {host}:{port}")
    logger.info(f"Debug mode: {debug_mode}")
    logger.info(f"Environment: {os.environ.get('FLASK_ENV', 'production')}")
    
    app.run(host=host, port=port, debug=debug_mode)
