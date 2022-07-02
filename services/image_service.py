from wand.image import Image


class ImageService:
    def __init__(self, path):
        self.path = path

    def resize(self, width, height=None):
        with Image(filename=self.path) as img:
            img.resize(width, height or round(width / img.width * img.height))
            img.save(filename=self.path)

    def copy_and_resize(self, new_file_path, width, height=None):
        with Image(filename=self.path) as img:
            img.resize(width, height or round(width / img.width * img.height))
            img.save(filename=new_file_path)
