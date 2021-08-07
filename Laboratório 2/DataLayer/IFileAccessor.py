

class IFileAccessor:
    """Interface implemented by classes that obtain files from a data source"""
    
    def GetFile(self, filePath: str) -> str:
        pass


