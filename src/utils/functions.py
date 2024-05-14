import shutil

from .directory import Dir
class Funct:

    @staticmethod
    def copy(source: str, destination: str) -> str:
        Dir.create_dir('/'.join(destination.split('/')[:-1]))
        destination: str = shutil.copy2(src=source, dst=destination)

        return destination
        ...