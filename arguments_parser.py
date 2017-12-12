from argparse import ArgumentParser


parser = ArgumentParser(description='Instagram follows parser')

parser.add_argument(
    '-u', '--username',
    help='Username or login or email or mobile phone',
    type=str,
    required=True
)

parser.add_argument(
    '-p', '--password',
    help='Password',
    type=str,
    required=True
)

parser.add_argument(
    '-o', '--output',
    help='Output csv file name (without `.csv`).\nDefault: following.csv',
    type=str,
    default='following'
)

parser.add_argument(
    '-f', '--un-follow',
    help='Un-follow list in csv',
    type=str
)

parser.add_argument(
    '-x', '--un-follow-only',
    help='Only un-follow by list',
    type=bool,
    default=False
)

parser.add_argument(
    '-a', '--user-agent',
    help='Browser user agent',
    type=str
)

parser.add_argument(
    '-s', '--proxy-server',
    help='Proxy server for chrome. Example: 172.11.28.32:8188',
    type=str
)
