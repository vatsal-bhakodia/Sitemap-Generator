# Sitemap Generator

![Sitemap Generator Logo](https://github.com/vatsal-bhakodia/Sitemap-Generator/blob/main/assets/logo.png)
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)](LICENSE)

A Python script to generate a sitemap for a given website by crawling its pages and extracting URLs. The script also includes options for formatting output and handling system shutdowns upon task completion.

## Features

- Extracts all internal links from a given home page URL.
- Generates a sitemap in XML format.
- Handles non-HTML content types and invalid URLs.
- Provides color-coded terminal output using `colorama`.
- Optionally shuts down the system after task completion.

## Requirements

- Python 3.x
- Required Python packages:
  - `requests`
  - `beautifulsoup4`
  - `colorama`

You can install the required packages using pip:

```bash
pip install requests beautifulsoup4 colorama
```
