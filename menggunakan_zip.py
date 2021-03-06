from pathlib import Path
from zipfile import ZipFile

zip = ZipFile("files.zip", "w")
for path in Path("ecommerce").rglob("*.*"):
    zip.write(path)
zip.close()

# with ZipFile("file.zip", "w") as zip:
#     for path in Path("ecommerce").rglob("*.*"):
#         zip.write(path)

# with ZipFile("file.zip") as zip:
#     print(zip.namelist())
#     info = zip.getinfo("ecommerce/__init__.py")
#     print(info.file_size)
#     print(info.compress_size)
#     zip.extractall("extract")
