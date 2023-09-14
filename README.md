# README for URL Shortener



https://github.com/anushil7a/LinkShortner/assets/87778762/5886b8ea-e318-418b-8433-3a49d05cbfb4



## Overview

The URL Shortener is a Flask-based web application that allows users to shorten long URLs. The application provides a simple interface for users to input a URL, which then returns a shortened version that redirects to the original URL when accessed.

## Features

1. **URL Shortening**: Convert long URLs into shorter, more shareable versions.
2. **Database Integration**: Store original and shortened URLs in an SQLite database for retrieval.
3. **Redirection**: Accessing the shortened URL redirects the user to the original URL.
4. **Copy to Clipboard**: Easily copy the shortened URL to the clipboard for sharing.

## Getting Started

### Prerequisites

- Python 3.x
- Pip (Python package installer)

### Installation

1. Clone the repository: git clone [repository-url]
2. Navigate to the project directory: cd [directory-name]
3. Install the required packages: pip install -r requirements.txt

### Usage

1. Start the Flask application: python app.py

2. Open a web browser and navigate to `http://127.0.0.1:5000/` to access the URL shortener interface.

3. Enter a URL into the provided form and click the "Shorten URL" button.

4. Copy the shortened URL and use it as needed!

## Files & Directories

- `app.py`: Main Flask application file.
- `Database.py`: Contains functions related to SQLite database operations.
- `home.html`: Frontend HTML template for the application.
- `urls.db`: SQLite database file storing original and shortened URLs.
- `requirements.txt`: Lists project dependencies for pip.

## Dependencies

- Flask (v2.0.1)
- Jinja2 (v3.0.1)
- Werkzeug (v2.0.1)

## License

This project is licensed under the MIT License. (You can modify this as per your license choice)



