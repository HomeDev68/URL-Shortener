from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4
import os

# TO-DO Later
# ADD rate-limiter using Flask-Limiter

# init flask
app = Flask(__name__)
# Configure SQLite db
db_dir = os.path.join(os.path.dirname(__file__), 'db')
db_path = os.path.join(db_dir, 'urls.db')

# Create the db directory if it doesn't exist
if not os.path.exists(db_dir):
    os.makedirs(db_dir)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Disable modification tracking
db = SQLAlchemy(app)

# create a model (db structure)
class URLMapping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_code = db.Column(db.String(10), unique=True, nullable=False)
    clicks = db.Column(db.Integer, default=0)
    # repr method is used to represent each object of this instance
    def __repr__(self):
        return f'<URLMapping {self.short_code}>'

with app.app_context():
    db.create_all()
    
def genshort_url(length=6):
    return str(uuid4())[:length]

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    data = request.get_json()
    original_url = data.get('url')
    if not original_url:
        return jsonify({'error': 'URL is required'}), 400
    # check if original url exists
    existing_mapping = URLMapping.query.filter_by(original_url=original_url).first()
    if existing_mapping:
        return jsonify({'shortUrl': f'{existing_mapping.short_code}'})
    else:
        short_code = genshort_url()
        new_mapping = URLMapping(original_url=original_url, short_code=short_code)
        db.session.add(new_mapping)
        db.session.commit()
        return jsonify({'shortUrl': f'{short_code}'})

@app.route('/<short_code>')
def redirect_to_original(short_code):
    found = URLMapping.query.filter_by(short_code=short_code).first()
    if found:
        found.clicks += 1 # Increment the click count
        db.session.commit()  # Commit the changes to the database
        return render_template('redirect.html', original_url=found.original_url)  # Render the redirect template
    else:
        return render_template('404.html')
        
@app.route('/analytics')
def analytics():
    url_mappings = URLMapping.query.all()
    return render_template('analytics.html', mappings=url_mappings) 
          
if __name__ == '__main__':
    app.run(debug=True)
