from pathlib import Path

path = Path("ecommerce")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")

# print(path.iterdir())
# for p in path.iterdir():
#     print(p)

# paths = [p for p in path.iterdir() if p.is_dir()]
# paths = [p for p in path.iterdir() if p.is_dir()]
paths = [p for p in path.rglob("*.py")]
print(paths)
