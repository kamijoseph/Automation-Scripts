
# file organiser

import os
import shutil
import logging
from pathlib import Path
from datetime import datetime

#  logging
LOG_DIR = Path.home() / ".file_organizer_logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / f"organizer_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s | %(levelname)s | %(message)s",
    handlers = [
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

# file type map
FILE_CATEGORIES = {
    "Documents": {".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".zip", ".tar", ".gz", ".rar", ".7z", ".csv"},
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"},
    "Videos": {".mp4", ".mkv", ".avi", ".mov"},
    "Audio": {".mp3", ".wav", ".flac"},
    "Programming": {".py", ".c", ".cpp", ".js", ".html", ".css"},
}

DEFAULT_FOLDERS = "Others"