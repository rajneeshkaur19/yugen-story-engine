from backend.database.db import SessionLocal
from backend.database.models import Story


if __name__ == "__main__":
    session = SessionLocal()
    stories = session.query(Story).all()
    for story in stories:
        print(story.title)
