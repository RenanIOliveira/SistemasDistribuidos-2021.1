from .IFileAccessor import IFileAccessor;


class FileSystemAccessor(IFileAccessor):

    def __init__(self, folder):
        self.folder = folder + "/";

    def GetFile(self, file: str) -> str:
        f = open(self.folder + file, "r")
        return f.read();