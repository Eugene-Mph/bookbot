import requests
from pathlib import Path


# url for frankenstein book
frank = "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/frankenstein.txt"
mobydick = "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/mobydick.txt"
pandp = "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/prideandprejudice.txt"
urls = [frank, mobydick, pandp]

# The function downloads the book
def get_book(url):


    # path to save the book
    path = f"books/{url.split("/")[-1]}"


    response = requests.get(url)

    # check if the request was successful
    if response.status_code == 200:
        
        # save the book to a file
        with open(path, "w") as f:
            f.write(response.text)
        print("Successfully retrieved the book.")
        print(f"The book has been saved to {path}.")
    else:
        print("Failed to retrieve the book.")


if __name__ == "__main__":
    for url in urls:
        get_book(url)
