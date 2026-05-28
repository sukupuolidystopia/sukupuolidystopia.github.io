import logging
import os

LOG_FILTER = [(logging.DEBUG, ".*")]
AUTHOR = "Esa"
SITENAME = "Sukupuolidystopia"

SITEURL = "https://sukupuolidystopia.github.io/test"
RELATIVE_URLS = False

PATH = "content"
TIMEZONE = "UTC"
DEFAULT_LANG = "en"

THEME = "pelican-themes/photowall"
THEME_STATIC_DIR = "theme"
CSS_FILE = "main.css"

STATIC_PATHS = ["images"]
CSS_FILE = "main.css"
PLUGINS = []

DISPLAY_ARTICLE_SUMMARY = True
DISPLAY_COVER = True
DEFAULT_METADATA = {"category": "General", "summary": ""}

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

PAGE_URL = "{slug}.html"
PAGE_SAVE_AS = "{slug}.html"

BASE_DIR = os.path.dirname(__file__)
content_dir = os.path.abspath(os.path.join(BASE_DIR, PATH))

print(">>> Pelican INPUT content scan <<<")
print("PATH =", PATH)
print("Resolved absolute path:", content_dir)

if os.path.isdir(content_dir):
    for root, dirs, files in os.walk(content_dir):
        for f in files:
            rel = os.path.relpath(os.path.join(root, f), content_dir)
            print("   ->", rel)
else:
    print("   (content dir not found)")