import glob
from pathlib import Path
from main.utils import load_plugins
import logging
from . import bot
from flask import Flask
import threading
import os

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "main/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

# Simple Flask app to satisfy Render's port detection
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Bot is running!'

def run_flask():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    print("Successfully deployed!")
    print("By MaheshChauhan • DroneBots")

    bot.run_until_disconnected()
