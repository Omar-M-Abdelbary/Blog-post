# Blog Post

A simple blog web application built using Flask

## Features
- User authentication (register, login, logout)
- Create, edit, and delete blog posts
- Pagination for blog posts
- Password hashing and session management
- User profile pictures
- Flask Forms for input validation

## Installation

1. **Clone the repository:**
   ```bash
   git clone <https://github.com/Omar-M-Abdelbary/Blog-post>
   cd flask-blog
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   ```bash
   flask db upgrade
   ```

5. **Run the application:**
   ```bash
   flask run
   ```
   The app should now be running at `http://127.0.0.1:5000/`.

## Usage
- Register a new account or log in.
- Create blog posts and edit or delete them.
- Update your profile and upload a profile picture.
- View posts by different users.

## Technologies Used
- Flask (with Flask-SQLAlchemy, Flask-WTF, Flask-Login, Flask-Bcrypt)
- SQLite (or any SQL database)
- Bootstrap for frontend styling

## Folder Structure
```
/flask-blog
│── /static         # CSS, JavaScript, images
│── /templates      # HTML templates
│── /flaskblog      # Application code
│   │── routes.py   # Routes for the app
│   │── models.py   # Database models
│   │── forms.py    # Flask-WTF forms
│   │── __init__.py # App initialization
│── config.py       # Configuration settings
│── run.py          # Application entry point
│── requirements.txt # List of dependencies
```

## Future Improvements
- Implement a rich-text editor for posts.
- Add email verification for registration.
- Improve UI with more styling.

## Contributing
If you'd like to contribute, feel free to fork the repo and submit a pull request.

## License
This project is open-source and available under the MIT License.

---

Would you like to add any additional details, such as specific customization you made beyond the tutorial?
