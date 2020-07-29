"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -msnyk_test` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``snyk_test.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``snyk_test.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import argparse
import json
from sys import argv

from pandas import json_normalize

from snyk_test.Package import Package


def parse_args(args):
    parser = argparse.ArgumentParser(description='Process optional arguments.')
    parser.add_argument('package', help='Specify the package name and version')
    parser.add_argument('--json', dest="is_json", action='store_true',
                        help='Format the result as JSON (default: false)')

    return parser.parse_args(args)


def main(argv=argv):
    """
    Args:
        argv: arguments list from command line

    Returns:
        int: A return code

    """

    parser = parse_args(argv[1:])

    package = Package(parser.package.split('@')[0], parser.package.split('@')[1])
    package.run_assesment()

    if parser.is_json:
        print(
            json.dumps({
                "security_vulnerabilities": package.vulnerabilities, "license_issues": package.license_issues
            })
        )
    else:
        print("Security Vulnerabilities:")
        print(json_normalize(package.vulnerabilities))
        print("\n")
        print("License Issues:")
        print(json_normalize(package.license_issues))
        print("\n")

    return 0
