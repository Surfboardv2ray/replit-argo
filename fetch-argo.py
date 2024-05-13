import requests
import re

repl_url = "https://23ef8b4b-c51a-4393-b6f7-87d96fbc1d68-00-239oofdhbgijm.pike.replit.dev/23ef8b4b-c51a-4393-b6f7-87d96fbc1d68.html"
host_sni = "23ef8b4b-c51a-4393-b6f7-87d96fbc1d68-00-239oofdhbgijm.pike.replit.dev"
target_ip = "azizimashin.com"

def get_content():
    try:
        response = requests.get(repl_url)
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
        if 'vless://' in line:
            lines[i] = re.sub(host_sni, f"{subdomain}.trycloudflare.com", line)
    return '\n'.join(lines)

def get_vless_line(content):
    lines = content.split('\n')
    for line in lines:
        if 'vless://' in line:
            parts = line.split('#')
            parts[-1] = '✅Argo+@Surfboardv2ray'
            vless_line = '#'.join(parts)
            vless_line = vless_line[vless_line.index('vless://'):]
            vless_line_parts = vless_line.split('@')
            ip_address_parts = vless_line_parts[1].split(':')
            ip_address_parts[0] = target_ip
            vless_line_parts[1] = ':'.join(ip_address_parts)
            return '@'.join(vless_line_parts)
    return None

def write_to_file(content):
    with open('argoconfig.txt', 'w') as file:
        file.write(content)

def main():
    content = get_content()
    if content:
        subdomain = get_subdomain(content)
        if subdomain:
            new_content = replace_subdomain(content, subdomain)
            vless_line = get_vless_line(new_content)
            if vless_line:
                write_to_file(vless_line)
                print("New content written to argoconfig.txt")
            else:
                print("No 'vless://' line found in the content.")
        else:
            print("Subdomain not found in the content.")
    else:
        print("Failed to fetch the content.")

if __name__ == "__main__":
    main()
