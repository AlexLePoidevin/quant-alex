"""Preview server for site/public that behaves like GitHub Pages for this repo.

The site lives under /quant-alex/ (as on alexlepoidevin.github.io/quant-alex), and
/path resolves to path.html or path/index.html.
"""
import http.server
import os
import sys

root, port = sys.argv[1], int(sys.argv[2])
BASE = "/quant-alex"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=root, **k)

    def send_head(self):
        path = self.path.split("?")[0].split("#")[0]
        if path in ("/", BASE):
            self.send_response(301)
            self.send_header("Location", BASE + "/")
            self.end_headers()
            return None
        if not path.startswith(BASE + "/"):
            return self.not_found()
        path = path[len(BASE):]
        fs = self.translate_path(path)
        if os.path.isdir(fs) and os.path.exists(os.path.join(fs, "index.html")):
            self.path = path
        elif not os.path.exists(fs) and os.path.exists(fs + ".html"):
            self.path = path + ".html"
        elif os.path.exists(fs):
            self.path = path
        else:
            return self.not_found()
        return super().send_head()

    def not_found(self):
        body = open(os.path.join(root, "404.html"), "rb").read()
        self.send_response(404)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        return __import__("io").BytesIO(body)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")    # always show the latest build
        super().end_headers()


print(f"Serving {root} at http://localhost:{port}{BASE}/", flush=True)
http.server.ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()
