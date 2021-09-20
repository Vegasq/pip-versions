from html.parser import HTMLParser


class VersionsPageParser(HTMLParser):
    def __init__(self, package_name: str):
        super().__init__()
        self._versions = set()
        self._handle_link_content = False
        self._package_name = package_name

    @property
    def versions(self):
        return self._versions

    def handle_starttag(self, tag, _):
        if tag == "a":
            self._handle_link_content = True

    def handle_endtag(self, tag):
        if tag == "a":
            self._handle_link_content = False

    def handle_data(self, data):
        if self._handle_link_content:
            if data.endswith(".whl"):
                data = data.split("-py3")[0]
                data = data.split("-py2")[0]
                data = data.replace(self._package_name + "-", "")
                self._versions.add(data)
            elif data.endswith(".tar.gz"):
                data = data.replace(self._package_name + "-", "")
                data = data.replace(".tar.gz", "")
                self._versions.add(data)
