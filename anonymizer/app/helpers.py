import os
import hashlib


def hash(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def deletefiles(*filenames):
    for filename in filenames:
        if os.path.exists(filename):
            os.remove(filename)
