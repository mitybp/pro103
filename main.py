import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/dimit/Downloads"
to_dir = "C:/Users/dimit/OneDrive/Área de Trabalho/103"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}


class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        name, ext = os.path.splitext(event.src_path)
        time.sleep(1)
        for key, value in dir_tree.items():
            time.sleep(1)
            if ext in value:
                file_name = os.path.basename(event.src_path)
                print(f"Baixado: {file_name}")
                path1 = from_dir + "/" + file_name
                path2 = to_dir + "/" + key
                path3 = to_dir + "/" + key + "/" + file_name

                if os.path.exists(path2):
                    print("Diretório existe")
                    print(f"Movendo: {file_name}")
                    shutil.move(path1, path3)
                    time.sleep(1)
                else:
                    print("Criando diretório")
                    os.makedirs(path2)
                    print(f"Movendo {file_name}")
                    shutil.move(path1, path3)
                    time.sleep(1)
    def on_deleted(self, event):
        time.sleep(1)
        print(f"Deletado: {event.src_path}")

    def on_created(self, event):
        time.sleep(1)
        print(f"Criado: {event.src_path}")

event_handler = FileMovementHandler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("Executando...")

except KeyboardInterrupt:
    print("Interrompido!")
    observer.stop()
