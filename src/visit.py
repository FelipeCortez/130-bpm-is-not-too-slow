import re
from pathlib import Path
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory")
    return parser.parse_args()

def get_library_dir(lib_name: str):
    return Path.cwd() / lib_name

def get_artists_dirs(lib_dir: Path):
    return subdirs(lib_dir)

def get_albums_dirs(artist_dir: Path):
    return subdirs(artist_dir)

def get_songs(album_dir: Path):
    return files(album_dir)

def subdirs(directory: Path):
    return [x for x in directory.iterdir() if x.is_dir()]

def files(directory: Path):
    return sorted([x for x in directory.iterdir() if x.is_file()], key=natural_sort)

def natural_sort(path: Path):
    int_or_lowercase = lambda t: int(t) if t.isdigit() else t.lower()
    return [int_or_lowercase(c) for c in re.split('([0-9]+)', path.name)]

def iprint(string: str, level: int = 0):
    spaces = "|  " * level * 1
    print(spaces + string)

if __name__ == "__main__":
    args = parse_args()

    lib_dir = get_library_dir(args.directory)

    for artist_dir in get_artists_dirs(lib_dir):
        print(artist_dir.name)
        for album_dir in get_albums_dirs(artist_dir):
            iprint(f"{album_dir.name}", 1)
            for song in get_songs(album_dir):
                iprint(f"{song.name}", 2)
