import json
from pathlib import Path

# movies = [
#     {"id": 1, "title": "Terminator", "year": 1998},
#     {"id": 2, "title": "Kindergarten cop", "year": 1993},
# ]

# data = json.dumps(movies)
# print(data)

# Path("movies.json").write_text(data)

data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies[0]["title"])
