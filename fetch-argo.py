import requests
import re

def get_content():
    try:
        url = "https://23ef8b4b-c51a-4393-b6f7-87d96fbc1d68-00-239oofdhbgijm.pike.replit.dev/23ef8b4b-c51a-4393-b6f7-87d96fbc1d68.html"
        response = requests.get(url)
        response.raise_for_status()
        content = response.text
        return content
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
        return None

def get_subdomain(content):
    match = re.search(r"(\w+-\w+-\w+-\w+).trycloudflare.com", content)
    if match:
        return match.group(1)
    else:
        return None

def replace_subdomain(content, subdomain):
    new_content = re.sub(r"23ef8b4b-c51a-4393-b6f7-87d96fbc1d68-00-239oofdhbgijm.pike.replit.dev", f"{subdomain}.trycloudflare.com", content)
    return new_content

def write_to_file(content):
    with open('argoconfig.txt', 'w') as file:
        file.write(content)

def main():
    content = get_content()
    if content:
        subdomain = get_subdomain(content)
        if subdomain:
            new_content = replace_subdomain(content, subdomain)
            write_to_file(new_content)
            print("New content written to argoconfig.txt")
        else:
            print("Subdomain not found in the content.")
    else:
        print("Failed to fetch the content.")

if __name__ == "__main__":
    main()
