
import pathlib 

from setuptools import setup



about          = dict()
root_directory = pathlib.Path(__file__).resolve().parent
with open(str(root_directory.joinpath("bookmark_manager", "__version__.py").absolute()), "r", "utf-8") as _file_descriptor:
    exec(_file_descriptor.read(), about)

setup(
  name             = about["__title__"],
  version          = about["__version__"],
  description      = about["__description__"],
  long_description = about["__description__"],
  packages         = ["bookmark_manager"],
  author           = about["__author__"],
  url              = about["__url__"],
)

