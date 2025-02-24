from flasklearning import create_app
from flasklearning import  db
from flasklearning.models import User

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)