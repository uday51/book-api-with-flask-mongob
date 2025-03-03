# Flask + MongoDB Book Collection API

## Overview

This is a simple RESTful API built using Flask and MongoDB. It allows users to manage a book collection by adding, retrieving, and deleting books.

## Features

- Add a Book (POST /add_book)

- Retrieve All Books (GET /books)

- Retrieve a Book by Title (GET /book/<title>)

- Delete a Book by Title (DELETE /delete_book/<title>)

## Technologies Used

- Python

- Flask

- MongoDB

- PyMongo



## API Endpoints

- Add a Book

Endpoint: /add_book

Method: POST

Request Body (JSON):

{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "year": 1925
}

Response:

{ "message": "Book added successfully" }

- Get All Books

Endpoint: /books

Method: GET

Response:

[
  {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925
  }
]

- Get a Book by Title

Endpoint: /book/<title>

Method: GET

Example: /book/The Great Gatsby

Response:

{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "year": 1925
}

- Delete a Book by Title

Endpoint: /delete_book/<title>

Method: DELETE

Example: /delete_book/The Great Gatsby

Response:

{ "message": "Book deleted successfully" }


