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
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('vless://'):
            lines[i] = re.sub(r"23ef8b4b-c51a-4393-b6f7-87d96fbc1d68-00-239oofdhbgijm.pike.replit.dev", f"{subdomain}.trycloudflare.com", line)
    return '\n'.join(lines)

def get_vless_line(content):
    lines = content.split('\n')
    for line in lines:
        if line.startswith('vless://'):
            return line
    return None

def main():
    content = get_content()
    if content:
        subdomain = get_subdomain(content)
        if subdomain:
            new_content = replace_subdomain(content, subdomain)
            vless_line = get_vless_line(new_content)
            if vless_line:
                print(vless_line)
            else:
                print("No 'vless://' line found in the content.")
        else:
            print("Subdomain not found in the content.")
    else:
        print("Failed to fetch the content.")

if __name__ == "__main__":
    main()
