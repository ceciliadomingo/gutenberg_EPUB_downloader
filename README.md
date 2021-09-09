# gutenberg_EPUB_downloader
Downloads copyright-free books in EPUB format (with pictures when available). 
Opens the chrome browser, goes to the first result for your search term(s) and downloads the book in EPUB format. The downloaded book will be named with your search term(s).

**System:** Windows

**Browser:** Chrome

## Third-party modules:
**selenium:** to use the Chrome browser. Requires downloading chromedriver

**shutil:** to move downloads to an EPUB folder and rename them

## Usage:
1. In the .bat file, rename the path to where the script is (somewhere in your PATH environment)
2. In the .py file, rename the paths marked with ******:
- The path to your chromedriver
- Your default Downloads directory
- The directory where you want your EPUB files stored
3. Open Run and type gutenberg, followed by your search term(s).
4. Enjoy your reading :)
