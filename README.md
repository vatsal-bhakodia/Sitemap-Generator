# Sitemap Generator

![Sitemap Generator Logo](https://github.com/vatsal-bhakodia/Sitemap-Generator/blob/main/assets/logo.png)

A Python script for generating XML sitemaps by crawling a website and extracting URLs. This tool is designed for web developers, SEO specialists, and website administrators to efficiently create and manage sitemaps, enhancing SEO and website structure. Key features include priority settings for URLs based on depth, system shutdown options, and detailed debugging output.

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)](LICENSE)

[Download executable](https://github.com/vatsal-bhakodia/Sitemap-Generator/blob/main/SitemapGen.exe)


## Features

- **XML Sitemap Generation**: Generates a sitemap in XML format with priority values based on URL depth (e.g., `1.0`, `0.8`, `0.6`, `0.4`).
- **Link Extraction**: Extracts all internal links from the specified home page URL.
- **Content Handling**: Manages non-HTML content types and invalid URLs gracefully.
- **Color-Coded Terminal Output**: Utilizes `colorama` for color-coded output to enhance readability.
- **System Shutdown Option**: Optionally shuts down the system upon completion of the task.
- **Debugging Output**: Creates a `dump.txt` file listing all discovered links and their referring pages for troubleshooting purposes.

## Requirements

- Python 3.x
- Required Python packages:
  - `requests`
  - `beautifulsoup4`
  - `colorama`

To install the required packages, run:

```bash
pip install requests beautifulsoup4 colorama
```

## Installation and Usage

1. **Clone the Repository:**
   ```BASH
   git clone https://github.com/vatsal-bhakodia/Sitemap-Generator.git
   cd Sitemap-Generator
   ```
  
2. **Run the Script:**
  ```bash
  python sitemap_generator.py
  ```

3. **Follow the Prompts:**
  Enter the home page URL of the website you want to crawl.
  Choose whether you want the system to shut down after the task is completed.

3. **Review Output:**
  XML Sitemap: The generated XML sitemap will be saved with the domain name.
  Dump File: A dump.txt file will be created, listing all links and their referring pages.
