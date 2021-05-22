# run.py

#import os
import config
from onlineshop import create_app
app = create_app(config)

if __name__ == '__main__':
    app.run(port=config.PORT , debug=True)
