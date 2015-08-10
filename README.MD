# Notifier

Tool to send notification to Jabber server. In future: add other protocols and fix bugs.
Now available just dev version.

##Installation

```bash
git clone https://github.com/Detonavomek/notifier.git
cd notifier/
pip install -r requirements.txt
```

##General usage

To show general help message:
```bash
python main.py --help
```

Available commands:
```bash
jabber
```

##jabber

To show help message for jabber:
```bash
python main.py jabber --help
```

Options:
```bash
  -u, --username TEXT  Username on Jabber server.
  -p, --password TEXT  Password of Jabber server.
  -s, --server TEXT    URL Jabber server.
  -p, --port INTEGER   Jabber server port.
  -c, --channel TEXT   Name of Jabber channel.
  -m, --message TEXT   Message to show in Jabber channel.
  --help               Show this message and exit.
```

Also can use environment variables(save them on ~/.bashrc):
```bash
export JABBER_USERNAME=<your.username@domain.com>
export JABBER_PASSWORD=<your.password>
export JABBER_SERVER=<jabber.server.url>
export JABBER_PORT=<jabber.port>
export JABBER_CHANNEL=<jabber.channel>
```
