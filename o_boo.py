from __future__ import absolute_import  # NOQA
"""This module implements Swak output plugin of Boo."""

import click

from swak.plugin import Output


class Boo(Output):
    """Boo class."""

    def _write(self, bulk):
        """Write a bulk."""
        raise NotImplementedError()


@click.command(help="PLUGIN HELP MESSAGE GOES HERE")
@click.pass_context
def main(ctx):
    """Plugin entry."""
    return Boo()


if __name__ == '__main__':
    main()