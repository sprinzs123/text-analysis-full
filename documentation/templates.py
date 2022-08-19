# make what templates are used where
import os


get_all_html = """
    echo $0
    find  -type f -name "*.html"
"""

all_html_string = os.system("bash -c '%s'" % get_all_html)
