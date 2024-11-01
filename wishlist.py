from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data structures to store wishlists and books
# Sample data structures to store wishlists and books
wishlists = {
    "user123": {
        "My Wishlist": ["book1"]
    }
}

books = {
    "book1": "The Great Gatsby",
    "book2": "To Kill a Mockingbird",
    "book3": "1984"
}

# Function to create a wishlist for a user
@app.route('/create_wishlist', methods=['POST'])
def create_wishlist():
    user_id = request.json.get('user_id')
    wishlist_name = request.json.get('wishlist_name')
    if user_id not in wishlists:
        wishlists[user_id] = {}
    if wishlist_name in wishlists[user_id]:
        return jsonify({"message": "Wishlist name must be unique for the user."}), 400
    wishlists[user_id][wishlist_name] = []
    return jsonify({"message": "Wishlist created successfully"})

# Function to add a book to a user's wishlist
# Function to add a book to a user's wishlist
@app.route('/add_book_to_wishlist', methods=['POST', 'GET'])
def add_book_to_wishlist():
    user_id = request.args.get('user_id')  # Accept as a URL parameter
    wishlist_name = request.args.get('wishlist_name')  # Accept as a URL parameter
    book_id = request.args.get('book_id')  # Accept as a URL parameter
    
    if user_id in wishlists and wishlist_name in wishlists[user_id]:
        if book_id not in wishlists[user_id][wishlist_name]:
            wishlists[user_id][wishlist_name].append(book_id)
            return jsonify({"message": "Book added to wishlist successfully"})
        else:
            return jsonify({"message": "Book is already in the wishlist."}), 400
    else:
        return jsonify({"message": "User or wishlist not found."}), 404

# Function to remove a book from a user's wishlist
@app.route('/remove_book_from_wishlist', methods=['DELETE'])
def remove_book_from_wishlist():
    user_id = request.json.get('user_id')
    wishlist_name = request.json.get('wishlist_name')
    book_id = request.json.get('book_id')
    if user_id in wishlists and wishlist_name in wishlists[user_id]:
        if book_id in wishlists[user_id][wishlist_name]:
            wishlists[user_id][wishlist_name].remove(book_id)
            return jsonify({"message": "Book removed from wishlist successfully"})
        else:
            return jsonify({"message": "Book not found in the wishlist."}), 400
    else:
        return jsonify({"message": "User or wishlist not found."}), 404

# Function to list books in a user's wishlist
@app.route('/list_books_in_wishlist', methods=['GET'])
def list_books_in_wishlist():
    user_id = request.args.get('user_id')
    wishlist_name = request.args.get('wishlist_name')
    if user_id in wishlists and wishlist_name in wishlists[user_id]:
        books_in_wishlist = wishlists[user_id][wishlist_name]
        book_names = [books[book_id] for book_id in books_in_wishlist]
        return jsonify({"books_in_wishlist": book_names})
    else:
        return jsonify({"message": "User or wishlist not found."}), 404

if __name__ == '__main__':
    app.run(debug=True)
