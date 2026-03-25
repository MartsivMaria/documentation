from infrastructure import SqliteRepository
from business_logic import BlogService

def main():
    repository = SqliteRepository()
    
    service = BlogService(repository)
    
    service.import_data_from_file("data.csv")

if __name__ == "__main__":
    main()