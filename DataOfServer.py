import psutil

class DataServer:
    def __GetMemoryInfo(self):
        return psutil.virtual_memory()
    def GetData(self):
        return self.__GetMemoryInfo().percent

# ...