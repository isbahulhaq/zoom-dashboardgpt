import os
from flask import Flask, render_template, request, jsonify
from datetime import datetime

# Flask app initialization
app = Flask(__name__)

# Secret key for session management (change this in production)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-change-this-in-production')

# Sample data for dashboard (you can replace this with your actual data)
dashboard_stats = {
    'total_meetings': 150,
    'active_users': 45,
    'total_hours': 320,
    'upcoming_meetings': 12
}

# Routes
@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('index.html', stats=dashboard_stats)

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

@app.route('/api/stats')
def api_stats():
    """API endpoint to get dashboard statistics"""
    return jsonify(dashboard_stats)

@app.route('/api/meetings')
def api_meetings():
    """API endpoint to get meetings data"""
    meetings = [
        {
            'id': 1,
            'title': 'Team Standup',
            'time': '10:00 AM',
            'duration': '30 mins',
            'participants': 8
        },
        {
            'id': 2,
            'title': 'Client Meeting',
            'time': '2:00 PM',
            'duration': '1 hour',
            'participants': 5
        },
        {
            'id': 3,
            'title': 'Project Review',
            'time': '4:30 PM',
            'duration': '45 mins',
            'participants': 12
        }
    ]
    return jsonify(meetings)

@app.route('/health')
def health():
    """Health check endpoint for Render"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    })

# Error handlers
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return render_template('500.html'), 500

# Main entry point
if __name__ == '__main__':
    # Get port from environment variable (Render sets this)
    port = int(os.environ.get('PORT', 5000))
    
    # Get debug mode from environment
    debug_mode = os.environ.get('DEBUG', 'False') == 'True'
    
    # Run the application
    # IMPORTANT: host='0.0.0.0' is required for Render to work
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
