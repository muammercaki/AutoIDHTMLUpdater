# AutoIDHTMLUpdater

AutoIDHTMLUpdater is a Python script to automatically add IDs to elements in an HTML file.

## Project Description

This project aims to automatically add IDs to elements within an existing HTML file. If you're working on web design and want to automatically assign unique IDs to elements, this script can be used for that purpose.

## How to Use

1. Open the content of the `idless_html.html` file. This file contains an example HTML content with elements lacking IDs.

2. Run the `add_ids_to_elements.py` file. This script will analyze the `idless_html.html` file, assign automatic IDs to elements, and save the result to the `html_with_ids.html` file.

3. Open the `html_with_ids.html` file. This file contains the updated version of the original HTML content, now including automatically added IDs.

## Use Cases

- Web developers might want to automatically assign unique IDs to elements of websites for design or automation purposes.
- In web scraping projects, automatically adding IDs to certain elements can be helpful for targeted access.

## Requirements

To ensure proper functionality of the project, the following libraries are required. You may need to install [Python](https://www.python.org/downloads/) before installing these libraries.

- `beautifulsoup4==4.9.3`
- `requests==2.26.0`

You can install the libraries using the following command:

```bash
pip install -r requirements.txt

## License

This project is licensed under the MIT License. For more information, please see the [LICENSE file](LICENSE).

