# ! pip install pymupdf

import fitz


class PageExtract():
    def __init__(self, path, page=None):
        self.path = path
        self.doc = fitz.Document(self.path)
        if page is not None:
            self.page = self.doc.loadPage(int(page) - 1)



