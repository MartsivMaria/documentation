import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Post
from interfaces import IRepository

class SqliteRepository(IRepository):
    def __init__(self, db_url="sqlite:///wordpress.db"):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def read_csv(self, file_path: str):
        data = []
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
        return data

    def save_user_with_post(self, user_dict: dict, post_dict: dict):
        session = self.Session()
        try:
            new_user = User(username=user_dict['username'], email=user_dict['email'])
            session.add(new_user)
            session.flush()
            
            new_post = Post(
                title=post_dict['title'], 
                content=post_dict['content'], 
                user_id=new_user.id
            )
            session.add(new_post)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error while saving: {e}")
        finally:
            session.close()

    def get_all_posts(self):
        session = self.Session()
        posts = session.query(Post).all()
        session.close()
        return posts