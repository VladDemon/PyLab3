import re
class HTMLParserForEmail:
    def __init__(self, filename):
        self.filename = filename

    def read_html_file(self):
        with open(self.filename, 'r') as f:
            html_string = f.read()
        return html_string

    def parse_all_emails(self, html_string):
        pattern = r'<a href="([^"]+@[^"]+\.[^"]+)">.*?</a>'
        return re.findall(pattern, html_string)

    def extract_emails(self):
        html_string = self.read_html_file()
        return self.parse_all_emails(html_string)

filename = 'index.html'
parser = HTMLParserForEmail(filename)
# print(parser.read_html_file()
emails = parser.extract_emails()
print(emails)
