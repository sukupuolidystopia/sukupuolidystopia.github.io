import logging



LOG_FILTER = [(logging.DEBUG, ".*")]

AUTHOR = "Esa"
SITENAME = "Sukupuolidystopia"
SITEURL = ""
RELATIVE_URLS = False
PATH = "content"
TIMEZONE = "UTC"
DEFAULT_LANG = "en"

import os

# Pelican always looks at PATH for input content
BASE_DIR = os.path.dirname(__file__)
content_dir = os.path.abspath(os.path.join(BASE_DIR, PATH))

print(">>> Pelican INPUT content scan <<<")
print("PATH setting:", PATH)
print("Resolved absolute path:", content_dir)

if os.path.isdir(content_dir):
    for root, dirs, files in os.walk(content_dir):
        for f in files:
            rel = os.path.relpath(os.path.join(root, f), content_dir)
            print("   ->", rel)
else:
    print("   (content dir not found)")


# Use default 'simple' theme
#THEME_TEMPLATES_OVERRIDES = ["templates"]

THEME = "pelican-themes/photowall"
THEME_STATIC_DIR = "theme"
CSS_FILE = "main.css"
RELATIVE_URLS = True
STATIC_PATHS = ["images", "css"]
print("STATIC_PATHS:", STATIC_PATHS)
#ARTICLE_EXCLUDES = ["images"]

# Plugins
PLUGINS = []

# Display summaries for cards
DISPLAY_ARTICLE_SUMMARY = True
DISPLAY_COVER = True
DEFAULT_METADATA = {"category": "General", "summary": ""}

import os
SITEURL = "https://sukupuolidystopia.github.io/test"
RELATIVE_URLS = False
BASE_DIR = os.path.dirname(__file__)
content_dir = os.path.abspath(os.path.join(BASE_DIR, PATH))
# Show pages (About, Resources, etc.) in menu
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
PAGE_URL = "{slug}.html"
PAGE_SAVE_AS = "{slug}.html"
# (Optional) Add custom menu items manually
MENUITEMS = (
    ('"Kansainväliset asiantuntijatehtävät"', '/'),
    ('Yhdysvaltain politiikka', '/'),
    ('Yhdysvaltain politiikka', '/'),
    ('Kansaivälinen media', '/media.html'),
    ('Tägien perusteella', '/tags.html'),

)



print(">>> INPUT content debug <<<")
print("PATH =", PATH)
print("Resolved absolute path:", content_dir)

if os.path.isdir(content_dir):
    for root, dirs, files in os.walk(content_dir):
        for f in files:
            rel = os.path.relpath(os.path.join(root, f), content_dir)
            print("   ->", rel)
else:
    print("   (content dir not found)")
