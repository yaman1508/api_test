# from flask import Flask, request, jsonify

# app = Flask(__name__)

# # Sample data storage (simulating a database)
# items = []

# # GET: Retrieve all items


# @app.route('/items', methods=['GET'])
# def get_items():
#     return jsonify(items)

# # POST: Add a new item


# @app.route('/items', methods=['POST'])
# def add_item():
#     try:
#         data = request.get_json()
#         if 'name' not in data:
#             return jsonify({'error': 'Name is required'}), 400
#         item = {'id': len(items) + 1, 'name': data['name']}
#         items.append(item)
#         return jsonify(item), 201
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# # PUT: Update an existing item


# @app.route('/items/<int:item_id>', methods=['PUT'])
# def update_item(item_id):
#     data = request.get_json()
#     for item in items:
#         if item['id'] == item_id:
#             item['name'] = data.get('name', item['name'])
#             return jsonify(item)
#     return jsonify({'error': 'Item not found'}), 404

# # DELETE: Remove an item


# @app.route('/items/<int:item_id>', methods=['DELETE'])
# def delete_item(item_id):
#     global items
#     items = [item for item in items if item['id'] != item_id]
#     return jsonify({'message': 'Item deleted'}), 200


# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask, request, jsonify

# app = Flask(__name__)

# # Sample data storage (simulating a database)
# items = []

# # GET: Retrieve all items
# @app.route('/items', methods=['GET'])
# def get_items():
#     return jsonify(items)

# # POST: Add a new item
# @app.route('/items', methods=['POST'])
# def add_item():
#     try:
#         data = request.get_json()
#         if 'name' not in data:
#             return jsonify({'error': 'Name is required'}), 400
#         item = {'id': len(items) + 1, 'name': data['name']}
#         items.append(item)
#         return jsonify(item), 201
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# # PUT: Update an existing item
# @app.route('/items/<int:item_id>', methods=['PUT'])
# def update_item(item_id):
#     data = request.get_json()
#     for item in items:
#         if item['id'] == item_id:
#             item['name'] = data.get('name', item['name'])
#             return jsonify(item)
#     return jsonify({'error': 'Item not found'}), 404

# # DELETE: Remove an item
# @app.route('/items/<int:item_id>', methods=['DELETE'])
# def delete_item(item_id):
#     global items
#     items = [item for item in items if item['id'] != item_id]
#     return jsonify({'message': 'Item deleted'}), 200

# # NEW: Process item and return a custom response
# @app.route('/process', methods=['POST'])
# def process_item():
#     data = request.get_json()
#     name = data.get('name')
#     item = data.get('item')
    
#     if not name or not item:
#         return jsonify({'error': 'Both name and item are required'}), 400
    
#     # Simulated task
#     response_message = f"Hello {name}, your item '{item}' has been processed successfully!"
    
#     return jsonify({
#         'status': 'success',
#         'message': response_message
#     }), 200

# if __name__ == '__main__':
#     app.run(debug=True)


import json
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data storage (simulating a database)
items = []

# ... (your existing routes for /items stay the same)

# NEW: Process item and return a custom response, then save it
@app.route('/process', methods=['POST'])
def process_item():
    data = request.get_json()
    name = data.get('name')
    item = data.get('item')
    
    if not name or not item:
        return jsonify({'error': 'Both name and item are required'}), 400
    
    response_data = {
        'status': 'success',
        'name': name,
        'item': item,
        'message': f"Hello {name}, your item '{item}' has been processed successfully!"
    }
    
    # Save to JSON file
    file_path = 'processed_items.json'
    
    # Check if file exists and load existing data
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            try:
                existing_data = json.load(f)
            except json.JSONDecodeError:
                existing_data = []
    else:
        existing_data = []

    # Append new entry
    existing_data.append(response_data)
    
    # Write back to file
    with open(file_path, 'w') as f:
        json.dump(existing_data, f, indent=4)
    
    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(debug=True)
