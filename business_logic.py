from infrastructure import IRepository

class BlogService:
    def __init__(self, repository: IRepository):
        self.repository = repository

    def import_data_from_file(self, file_path):
        raw_data = self.repository.read_csv(file_path)
        for item in raw_data:
            user_data = {'username': item['username'], 'email': item['email']}
            post_data = {'title': item['post_title'], 'content': item['post_content']}
            
            self.repository.save_user_with_post(user_data, post_data)
        print("Import completed successfully.")