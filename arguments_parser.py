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
