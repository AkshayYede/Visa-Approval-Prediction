import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)

# Use current working directory
logs_folder_path = os.path.join(os.getcwd(), log_dir)
os.makedirs(logs_folder_path, exist_ok=True)

logs_path = os.path.join(logs_folder_path, LOG_FILE)

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)