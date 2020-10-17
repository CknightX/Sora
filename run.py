from app import create_app
import os

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
if __name__ == '__main__':
    app.run(debug=False,port=80,host='0.0.0.0')
    