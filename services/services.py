from models.models import db, Post

class PostService:
    @staticmethod
    def get_all_posts():
        return Post.query.all()

    @staticmethod
    def get_post_by_id(post_id):
        return Post.query.get_or_404(post_id)

    @staticmethod
    def create_post(title, content, author):
        new_post = Post(title=title, content=content, author=author)
        db.session.add(new_post)
        db.session.commit()
        return new_post

    @staticmethod
    def update_post(post_id, title, content, author):
        post = Post.query.get_or_404(post_id)
        post.title = title
        post.content = content
        post.author = author
        db.session.commit()
        return post

    @staticmethod
    def delete_post(post_id):
        post = Post.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()