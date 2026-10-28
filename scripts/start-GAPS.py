
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import quote
import os
import webbrowser

# Directory containing this script
gaps_dir = Path(__file__).resolve().parent.parent

# The folder must be named GAPS because the current index.html
# uses paths such as /GAPS/images/GAPS-logo-mala.png.
if gaps_dir.name != "GAPS":
    raise SystemExit(
        "Please name the extracted folder 'GAPS' and run this script again."
    )

# Serve the parent directory so the site is available at /GAPS/
os.chdir(gaps_dir.parent)

host = "127.0.0.1"
port = 8000
url = f"http://{host}:{port}/GAPS/"

server = ThreadingHTTPServer(
    (host, port),
    SimpleHTTPRequestHandler
)

print("GAPS is running locally.")
print(f"Open this address in your browser: {url}")
print("To stop the server, press Ctrl+C.")

webbrowser.open(url)

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nGAPS server stopped.")
finally:
    server.server_close()
