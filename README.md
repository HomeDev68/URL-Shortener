# URL Shortener

A simple URL shortener service built with Flask, SQLAlchemy, and SQLite in Python. 
## Features

*   **URL Shortening:**  Converts long URLs into short, unique codes.
*   **Redirection:**  Redirects users from the shortened URL to the original URL.
*   **Click Tracking:**  Counts the number of times a shortened URL is accessed.
*   **Analytics:**  Provides a view of all shortened URLs and their click counts.

## Technologies Used

*   **Flask:**  A lightweight Python web framework.
*   **SQLAlchemy:**  An SQL toolkit and Object-Relational Mapper (ORM) for Python.
*   **SQLite:**  A C-language library that implements a small, fast, self-contained, high reliability, full-featured, SQL database engine.
*   **HTML/CSS:**  For basic front-end templating and styling.

## TO-DO
- **Add favicon**
- **Rate Limiting:**  Implement rate limiting to prevent abuse of the URL shortening service.  (Consider using Flask-Limiter).
- **Custom Short Codes:**  Allow users to specify custom short codes for their URLs.

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/HomeDev68/urlshortener
    cd urlshortener
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Initialize the database:**

    The database will be automatically created when you run the application for the first time.  The database file (`urls.db`) will be located in the `db` directory.

5.  **Run the application:**

    ```bash
    python main.py
    ```

    The application will start in debug mode and be accessible at `http://127.0.0.1:5000/`.

## Usage

1.  **Shorten a URL:**  Enter a long URL in the input field on the homepage and submit the form.  You will receive a shortened URL.

2.  **Access the Original URL:**  Navigate to the shortened URL in your browser.  You will be redirected to the original URL, and the click count for that shortened URL will be incremented.

3.  **View Analytics:**  Go to the `/analytics` route to see a list of all shortened URLs and their corresponding click counts.

## Future Improvements

*   **Rate Limiting:**  Implement rate limiting to prevent abuse of the URL shortening service.  (Consider using Flask-Limiter).
*   **Custom Short Codes:**  Allow users to specify custom short codes for their URLs.
*   **User Authentication:**  Add user accounts to manage shortened URLs and track usage.
*   **Improved Front-End:**  Enhance the user interface with a more modern design and better user experience.
*   **Deployment:**  Deploy the application to a production environment (e.g., Heroku, AWS, etc.).

## Contributing

Contributions are welcome!  Please feel free to submit issues or pull requests.

## License

[LICENSE](LICENSE)
