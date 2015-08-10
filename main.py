import click

from plugins.jabber import JabberClient


@click.group()
def cli():
    pass

@cli.command()
@click.option('-u', '--username', envvar='JABBER_USERNAME', prompt='Username', help='Username on Jabber server.')
@click.option('-p', '--password', envvar='JABBER_PASSWORD', prompt='Password', help='Password of Jabber server.')
@click.option('-s', '--server', envvar='JABBER_SERVER', prompt='Server', help='URL Jabber server.')
@click.option('-p', '--port', envvar='JABBER_PORT', default=5222, help='Jabber server port.')
@click.option('-c', '--channel', envvar='JABBER_CHANNEL', prompt='Channel', help='Name of Jabber channel.')
@click.option('-m', '--message', envvar='JABBER_MESSAGE', prompt='Message', help='Message to show in Jabber channel.')
def jabber(username, password, server, port, channel, message):
    with JabberClient(username=username, password=password,
                      server=server, port=port, channel=channel) as client:
        client.send(message)

if __name__ == '__main__':
    cli()
