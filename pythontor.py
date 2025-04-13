import socks
import socket
import sys
import random
from PyQt5.QtWidgets import QApplication, QInputDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

# Extended list of public Tor proxy servers to cycle through (doubled)
TOR_PROXIES = [
    ('135.181.8.210', 9050),
    ('185.220.101.240', 9050),
    ('45.77.91.243', 9050),
    ('46.101.17.12', 9050),
    ('62.210.209.94', 9050),
    ('51.15.255.74', 9050),
    ('38.29.247.194', 9050),
    ('94.23.234.98', 9050),
    ('212.83.164.11', 9050),
    ('209.127.9.26', 9050),
    ('185.221.156.74', 9050),
    ('198.27.65.207', 9050),
    ('128.199.145.11', 9050),
    ('104.238.207.246', 9050),
    ('173.249.28.1', 9050),
    ('159.89.168.240', 9050),
    ('45.77.155.74', 9050),
    ('192.241.233.25', 9050),
    ('199.19.192.56', 9050),
    ('185.27.135.105', 9050),
    ('144.217.14.215', 9050),
    ('104.236.123.145', 9050),
    ('172.104.47.50', 9050),
    ('51.79.131.101', 9050),
    ('188.165.248.69', 9050),
    ('185.192.233.40', 9050),
    ('206.189.19.52', 9050),
    ('206.189.168.12', 9050),
    ('104.198.179.218', 9050),
    ('185.99.133.138', 9050),
    ('178.62.193.13', 9050),
    ('178.128.142.215', 9050)
]

# Function to switch to a random proxy
def set_random_proxy():
    proxy = random.choice(TOR_PROXIES)
    socks.set_default_proxy(socks.SOCKS5, proxy[0], proxy[1])
    socket.socket = socks.socksocket

class TorBrowser(QWebEngineView):
    def __init__(self, url):
        super().__init__()
        self.setWindowTitle("Python Tor Browser")
        self.load(QUrl(url))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Set up random proxy before loading the page
    set_random_proxy()

    url, ok = QInputDialog.getText(None, "Enter URL", "Site to visit (http/https):")
    if ok and url:
        browser = TorBrowser(url)
        app.exec_()
