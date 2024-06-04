import os
import logging
import sys
from datetime import datetime
import FileObject
from aiogram.types import FSInputFile
from typing import IO

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)


class FileManager:
    def __init__(self, dir: str = "drive"):
        if os.path.isdir(dir):
            logger.info("Dir exist")
        else:
            logger.info("Dir no found, Creating!")
            os.makedirs(dir, exist_ok=True)
        self.__dir = dir

    def GetFile(self, FileName: str, Folder: str = ""):
        path = os.path.join(self.__dir, Folder, FileName)
        if os.path.isfile(path):
            return FSInputFile(path)
        else:
            logger.error(f"File {path} not found!")
            return None

    def PutFile(self, FileName: str, Content: bytes) -> bool:
        try:
            with open(os.path.join(self.__dir, FileName), 'wb') as file:
                file.write(Content)
                file.close()
            return True
        except Exception as e:
            logger.error(f"Failed to write file: {e}")
            return False

    def GetAllObjectFromFolders(self, FolderName) -> list[FileObject.File]:
        files = os.listdir(self.__dir + "/" + FolderName + "/")
        FilesObject = []
        for file_name in files:
            file_path = os.path.join(self.__dir, FolderName, file_name)

            if os.path.isfile(file_path):
                file_size_bytes = os.path.getsize(file_path)

                creation_time = os.path.getctime(file_path)
                creation_date = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')

                file = FileObject.File(file_name, file_size_bytes, creation_date,
                                       open(self.__dir + "/" + FolderName + "/" + file_name, "r"))

                FilesObject.append(file)

        return FilesObject

    def CreateFolders(self, FolderName) -> bool:
        try:
            if os.path.isdir(self.__dir + "/" + FolderName):
                logger.info("Dir exist")
            else:
                logger.info("Dir no found, Creating!")
                os.makedirs(self.__dir + "/" + FolderName, exist_ok=True)
        except:
            ...

    def GetAllObject(self) -> list[FileObject.File]:
        files = os.listdir(self.__dir)
        FilesObject = []
        for file_name in files:
            file_path = os.path.join(self.__dir, file_name)

            if os.path.isfile(file_path):
                file_size_bytes = os.path.getsize(file_path)

                creation_time = os.path.getctime(file_path)
                creation_date = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')

                file = FileObject.File(file_name, file_size_bytes, creation_date,
                                       open(self.__dir + "/" + file_name, "r"))
                FilesObject.append(file)

        return FilesObject

    def DeleteFile(self, FileName) -> bool:
        file_path = os.path.join(self.__dir, FileName)
        if os.path.exists(file_path):
            os.remove(file_path)
            logger.info(f"File {file_path} was successfully deleted.")
            return True
        else:
            logger.warning(f"File {file_path} not found.")
            return False

# ...