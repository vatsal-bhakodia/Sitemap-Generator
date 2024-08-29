import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from time import time
import urllib.parse
from colorama import Fore, Style, init

# Initialize colorama
init()

def extract_domain_name(url):
    if url.startswith("https://"):
        url = url[8:]
    elif url.startswith("http://"):
        url = url[7:]
    return url.split("/")[0]

def domain_exists(domain):
    try:
        result = requests.get(domain, timeout=10)
        if result.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print(Fore.RED + f'Please enter a valid URL: {e}' + Style.RESET_ALL)
        return False

def format_time(elapsed_time):
    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)
    formatted_time = ""
    if hours > 0:
        formatted_time += f"{hours} h, "
    if minutes > 0:
        formatted_time += f"{minutes} min, "
    formatted_time += f"{seconds} sec"
    return formatted_time

def get_links(domain_name, url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Check if the content type is HTML
        content_type = response.headers.get('Content-Type', '')
        if 'text/html' not in content_type:
            return  # Skip URLs that do not point to HTML content

        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        raw_links = soup.find_all('a')
        
        global all_links
        for i in raw_links:
            try:
                link = i['href']
                # Convert relative URLs to absolute URLs
                if not link.startswith('http') and link[0] != '#':
                    link = urllib.parse.urljoin(url, link)
                
                # Remove query parameters from the URL
                link = urllib.parse.urlparse(link)._replace(query='').geturl()

                # Ensure link is a valid web page URL
                if domain_name in link and link not in set(all_links):
                    response = requests.head(link, allow_redirects=True)  # Perform a HEAD request
                    if 'text/html' in response.headers.get('Content-Type', ''):
                        all_links.append(link)
                        with open(f'dump.txt', 'a') as dump:
                            dump.write(f"[+] {link}\n[REF] {url}\n\n")
            except KeyError:
                pass  # Handle cases where 'href' might not exist in the anchor tag
    except requests.exceptions.HTTPError as errh:
        print(Fore.RED + f"HTTP Error: {errh} for URL: {url}" + Style.RESET_ALL)
        with open(f'dump.txt', 'a') as dump:
            dump.write(f"HTTP Error: {errh} for URL: {url}\n")
        # Remove the link from the list if it returns an error
        if url in all_links:
            all_links.remove(url)
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e} for URL: {url}" + Style.RESET_ALL)

def create_sitemap(domain, links):
    date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+00:00")
    with open(f'{domain}.xml', 'a') as sitemap_file:
        priority = 1
        pri_count = 0
        sitemap_file.write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset\n\txmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n\txmlns:xhtml="http://www.w3.org/1999/xhtml"\n\txsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd"\n\txmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
)
        for i in links:
            sitemap_file.write(
            f'''<url>\n\t<loc>{i}</loc>\n\t<lastmod>{date}</lastmod>\n\t<changefreq>monthly</changefreq>\n\t<priority>{priority}</priority>\n</url>\n'''
            )
            pri_count += 1
            if pri_count == 1:
                priority = 0.8
            elif pri_count == 55:
                priority = 0.6
            elif pri_count == 500:
                priority = 0.5
            elif pri_count == 20000:
                priority = 0.4
        sitemap_file.write('</urlset>')

    print(Fore.GREEN + f'Sitemap is saved by the name of {domain}.xml' + Style.RESET_ALL)

logo = '''   _____ __                      _____                      __          
  / __(_) /____ __ _  ___ ____  / ___/__ ___  ___ _______ _/ /____  ____
 _\ \/ / __/ -_)  ' \/ _ `/ _ \/ (_ / -_) _ \/ -_) __/ _ `/ __/ _ \/ __/
/___/_/\__/\__/_/_/_/\_,_/ .__/\___/\__/_//_/\__/_/  \_,_/\__/\___/_/   
                        /_/                                             
'''
print(Fore.GREEN + logo + Style.RESET_ALL)

# Get URL input
result = False
while not result:
    domain_name = input('Enter Home Page URL: ').strip()
    if 'http' not in domain_name:
        domain_name = 'http://' + domain_name
    if domain_name.endswith('/'):
        domain_name = domain_name[:-1]
    result = domain_exists(domain_name)

# Shutdown option
while True:
    try:
        shutdown = int(input('Do you want your system to shut down after this task?\n1) Yes\n2) No\nEnter Choice: '))
        if shutdown in [1, 2]:
            print(Fore.GREEN + 'Okay' + Style.RESET_ALL)
            break
        else:
            print(Fore.YELLOW + 'Please enter a correct choice' + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + 'Please enter a number' + Style.RESET_ALL)

# Start the process
all_links = [domain_name]
start_time = time()
update_interval = 10

for index, i in enumerate(all_links):
    if index % update_interval == 0:
        print(Fore.CYAN + f'Elapsed time: {format_time(time() - start_time)}. Completed {index+1}, now searching in {i}' + Style.RESET_ALL)
    try:
        get_links(domain_name, i)
    except Exception as e:
        all_links.remove(i)
        print(Fore.RED + f'{i} is not working and is removed' + Style.RESET_ALL)
        print(Fore.RED + f'{e}' + Style.RESET_ALL)

if domain_name+'/' in set(all_links):
    all_links.remove(domain_name+'/')

# Write sitemap file
create_sitemap(extract_domain_name(domain_name), all_links)

# Shutdown option handling
if shutdown == 1:
    print(Fore.GREEN + 'Shutting down the system' + Style.RESET_ALL)
    os.system("shutdown /s")
else:
    input(Fore.GREEN + 'Press Enter to Exit' + Style.RESET_ALL)
