from typing import IO

class File:
    def __init__(self, FileName: str, FileSize: int, FileData: str, File: IO) -> None:
        self.FileName = FileName
        self.__FileSize = FileSize
        self.FileData = FileData
        self.File = File

    @property
    def FileSize(self) -> str:
        if self.__FileSize >= 1 << 30:  # 1 гигабайт
            file_size = f"{self.__FileSize / (1 << 30):.2f} ГБ"
        elif self.__FileSize >= 1 << 20:  # 1 мегабайт
            file_size = f"{self.__FileSize / (1 << 20):.2f} МБ"
        elif self.__FileSize >= 1 << 10:  # 1 килобайт
            file_size = f"{self.__FileSize / (1 << 10):.2f} КБ"
        else:
            file_size = f"{self.__FileSize} байт"
        return file_size

# ...