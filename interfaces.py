from abc import ABC, abstractmethod

class IRepository(ABC):
    
    @abstractmethod
    def read_csv(self, file_path: str):
        """Method for reading raw data from a CSV file"""
        pass

    @abstractmethod
    def save_user_with_post(self, user_dict: dict, post_dict: dict):
        """Method for saving data to the database through ORM"""
        pass

    @abstractmethod
    def get_all_posts(self):
        """Method for retrieving a list of all posts (for the presentation level)"""
        pass