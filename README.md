# AdminCreator
##Overview

This Python script connects you to the Tor network via rotating public Tor proxies, allowing you to surf the web anonymously and without restriction. It's simple, efficient, and doesn’t require any extra installations like the Tor Browser. Just run the script and browse any website you desire with Tor routing, keeping your identity hidden.

Forget about installing heavy clients or configuring complex network settings. This tool does it all, while staying low-key.

##Features

Rotating Public Proxies: Automatically switches between multiple public Tor exit nodes to ensure anonymity and reduce the chance of getting blocked.
Lightweight: Just Python and a few libraries to run. No need for additional Tor binaries or services.
Easy to Use: Minimal setup. Type in the URL you want to visit, and let it handle the rest.

##How it Works

This script leverages the power of SOCKS5 proxies to route your traffic through the Tor network, giving you full anonymity. The script:

Chooses a random public Tor proxy from a list.
Routes your traffic over Tor, anonymizing your requests.
Opens a web browser window (using PyQt5) to display the page.
Switches proxies periodically to keep things fresh.

##Important Notes

No Tor.exe required: The script uses public Tor proxies to route traffic. You don’t need to install the Tor service or rely on tor.exe.
Proxies Rotate Automatically: If a proxy gets blocked or goes down, it’ll automatically switch to another proxy from the list, keeping your browsing secure.
Be Aware of Limits: Public proxies can sometimes be slow or go down. If you experience issues, you can edit the proxy list in the script or add your own.
Security Disclaimer

This script is for educational and testing purposes only. Use responsibly. Never perform illegal activities while using Tor or any proxies. Always follow the law.

DO NOT use this tool to perform malicious activities or to attack others.

##Contributing

Want to make this tool better? Feel free to fork it, improve it, and submit pull requests.

If you find a new proxy, or a better way to handle proxy rotation, let us know! Open issues, request features, or fix bugs—let's grow this project together.

##Credits

Python – The best programming language to get things done.
PyQt5 – For the slick GUI to view websites.
Socks5 Proxy Servers – Public proxies that power this tool.
Tor Network – The backbone of anonymity.
