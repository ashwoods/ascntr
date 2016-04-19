import click
import tempfile

from datetime import datetime, date
from .utils import parse_cron

MAX_SIZE = 1024*1000


@click.command()
@click.argument('current_time')
def cli(current_time):
    hours, minutes = current_time.split(':')
    today = date.today()
    current_dt = datetime(today.year, today.month, today.day, int(hours), int(minutes))

    output = tempfile.SpooledTemporaryFile(max_size=MAX_SIZE)
    stdin = click.get_text_stream('stdin')

    #stdin = open('tests/sample.txt')
    for line in stdin:
        result = parse_cron(line, current_dt)
        if result:
            output.write(result)
    output.seek(0)
    click.echo(output.read())
    stdin.close()
