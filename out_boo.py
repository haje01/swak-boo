from __future__ import absolute_import  # NOQA
"""This module implements Swak ut plugin of Boo."""

import click

from swak.plugin import Output


class Boo(Output):
    """Boo class."""

    def write_stream(self, tag, es):
        """Write event stream synchronously.

        Args:
            tag (str): Event tag.
            es (EventStream): Event stream.
        """
        raise NotImplemented()

    def write_chunk(self, chunk):
        """Write a chunk from buffer."""
        raise NotImplemented()


@click.command(help="PLUGIN HELP MESSAGE GOES HERE")
@click.pass_context
def new(ctx):
    """New plugin."""
    return Boo()


if __name__ == '__main__':
    new()
