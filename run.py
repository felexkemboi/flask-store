# run.py

#import os
import config
from notesApp import create_app

#config_name = os.getenv('FLASK_CONFIG')
#print(config_name)
app = create_app(config)

if __name__ == '__main__':
    app.run(port=config.PORT)



# app.config.from_object(config)
# print(app.config)

#app.run(port=config.PORT)
