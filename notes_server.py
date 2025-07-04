from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

NOTES_FILE = 'notes.json'

def load_notes():
    """Load notes from JSON file"""
    if os.path.exists(NOTES_FILE):
        try:
            with open(NOTES_FILE, 'r') as f:
                return json.load(f)
        except:
            return []
    return []

def save_notes(notes):
    """Save notes to JSON file"""
    with open(NOTES_FILE, 'w') as f:
        json.dump(notes, f, indent=2)

@app.route('/api/notes', methods=['GET'])
def get_notes():
    """Get all notes"""
    notes = load_notes()
    return jsonify(notes)

@app.route('/api/notes', methods=['POST'])
def add_note():
    """Add a new note"""
    data = request.json
    note_text = data.get('text', '').strip()
    
    if not note_text:
        return jsonify({'error': 'Note text is required'}), 400
    
    notes = load_notes()
    
    new_note = {
        'id': int(datetime.now().timestamp() * 1000),  # Unique ID based on timestamp
        'text': note_text,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'timestamp': int(datetime.now().timestamp() * 1000)
    }
    
    notes.insert(0, new_note)  # Add to beginning
    save_notes(notes)
    
    return jsonify(new_note)

@app.route('/api/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    """Delete a note"""
    notes = load_notes()
    notes = [note for note in notes if note['id'] != note_id]
    save_notes(notes)
    return jsonify({'success': True})

if __name__ == '__main__':
    # Create notes file if it doesn't exist
    if not os.path.exists(NOTES_FILE):
        save_notes([])
    
    print("Notes server starting on http://localhost:5001")
    print("Notes will be stored in notes.json")
    app.run(host='0.0.0.0', port=5001, debug=True) 