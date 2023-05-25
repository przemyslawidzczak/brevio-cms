import os
from src import create_app
from dotenv import load_dotenv

load_dotenv()

app = create_app()

if __name__ == "__main__":
    app.run(debug=os.getenv('DEBUG_MODE'), port=os.getenv('APP_PORT'))