import os

CACHE_DIRECTIVE = "cache/"


def handle_cache_object(web_url: str, filename: str, obj: bytes):
	path = CACHE_DIRECTIVE + web_url.removeprefix("http://")
	os.makedirs(path.removesuffix(filename), exist_ok=True)
	cache_object(path, obj)


def cache_object(path, obj):
	with open(path, "wb") as file:
		file.write(obj)
