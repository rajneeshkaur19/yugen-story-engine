import os
import shutil


if __name__ == "__main__":
    if os.path.exists("data/cache"):
        shutil.rmtree("data/cache")
    if os.path.exists("data/logs"):
        shutil.rmtree("data/logs")
    print("Cleaned cache and logs.")
