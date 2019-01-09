'''this file is the entry point to our app'''

import os
from app import create_app

config_name = "development"
app = create_app(config_name)
'''We create the app by running create_app function and passing in the config_name'''


if __name__ == "__main__":
    app.run()