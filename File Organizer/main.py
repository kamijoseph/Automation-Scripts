
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
    "Documents": {".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv", "json", ".odg", ".odt"},
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".aseprite"},
    "Videos": {".mp4", ".mkv", ".avi", ".mov"},
    "Audio": {".mp3", ".wav", ".flac"},
    "Archives": {".zip", ".tar", ".gz", ".rar", ".7z", ".sav", ".pkl", ".sql", ".keras"},
    "Code": {".py", ".c", ".cpp", ".js", ".html", ".css", ".ipynb"},
}

DEFAULT_FOLDER = "Others"

# organize function
def organize_directory(target_dir: Path):
    if not target_dir.exists():
        logging.error(f"directory does not exit: {target_dir}")
        return
    
    if not target_dir.is_dir():
        logging.error(f"not a directory: {target_dir}")
        return
    
    logging.info(f"starting organization of {target_dir}")

    for item in os.scandir(target_dir):
        try:
            if not item.is_file():
                continue

            file_path = Path(item.path)
            extension  = file_path.suffix.lower()
            destination_folder = DEFAULT_FOLDER

            for category, extensions in FILE_CATEGORIES.items():
                if extension in extensions:
                    destination_folder = category
                    break

            dest_dir = target_dir / destination_folder
            dest_dir.mkdir(exist_ok=True)

            shutil.move(
                str(file_path),
                dest_dir / file_path.name
            )
            logging.info(f"moved: {file_path.name} --> {destination_folder}")

        except PermissionError:
            logging.warning(f"permission denied: {item.name}")

        except shutil.Error as e:
            logging.warning(f"file move error ({item.name}) {e}")

        except Exception as e:
            logging.error(f"Unexpected error ({item.name}): {e}")
    
    logging.info("organization completed succesfully.")

if __name__ == "__main__":
    TARGWT_DIRECTORY =  Path.home() / "Downloads"
    organize_directory(TARGWT_DIRECTORY)