from bs4 import BeautifulSoup
import re

# Read the HTML file and create a BeautifulSoup object
with open('idless_html.html', 'r', encoding='utf-8') as file:
    html_content = file.read()
soup = BeautifulSoup(html_content, 'html.parser')

# Assign IDs to elements
class_names = soup.find_all(class_=re.compile("^element"))
for idx, element in enumerate(class_names, start=1):
    element['id'] = f"auto_id_{idx}"

# Write the processed HTML content to a new file
with open('html_with_ids.html', 'w', encoding='utf-8') as output_file:
    output_file.write(soup.prettify())

print("IDs successfully added and saved to the output file.")