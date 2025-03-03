from flask import Flask,request,jsonify
from pymongo import MongoClient

app=Flask(__name__)

client=MongoClient("mongodb://localhost:27017")
db=client["bookstore"]
collection=db["books"]

@app.route('/add_book',methods=["POST"])
def add_book():
    data=request.json
    if not data["title"] or not data["author"] or not data["year"]:
        return jsonify({"error":"Missing required fields"}),400
    if collection.find_one({"title":data["title"]}):
        return jsonify({"error":"Book already exists"}),400
    collection.insert_one(data)
    return jsonify({"message":"Book Added Successfully"}), 201

@app.route('/get-books',methods=["GET"])
def get_all_books():
    books=list(collection.find({},{"_id":0}))
    return jsonify(books),200

@app.route('/get-book/<title>',methods=["GET"])
def get_book(title):
    book=collection.find_one({"title":title},{"_id":0})
    if not book:
        return jsonify({"error":"book not found"}),404
    return jsonify(book)

@app.route('/delete-book/<title>',methods=["DELETE"])
def delete_book(title):
    book=collection.delete_one({"title":title})
    if book.deleted_count==0:
        return jsonify({"error":"Book not found"}),404
    return jsonify({"message":"Book Deleted Succesffully"}),200



if __name__=="__main__":
    app.run(debug=True)


