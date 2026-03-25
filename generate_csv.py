import csv
import random

def generate_csv(filename="data.csv", rows=1050):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["username", "email", "post_title", "post_content"])
        
        for i in range(rows):
            writer.writerow([
                f"user_{i}",
                f"user{i}@example.com",
                f"Post Title {i}",
                f"This is a long content for post number {i}."
            ])
    print(f"File {filename} generated with {rows} rows.")

if __name__ == "__main__":
    generate_csv()