from globals.strings import OUTPUT_FILETYPE

class FileNameHandling:
    @staticmethod
    def asmToBin(path: str) -> str:
        name = path.rsplit(".", 1)[0]
        return name + OUTPUT_FILETYPE