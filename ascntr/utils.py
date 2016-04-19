import time
from datetime import datetime, timedelta


def parse_cron(line, current_dt):

    tokens = line.split(' ')
    if len(tokens) < 3:
        return ''
    minutes, hours, command = tokens[0], tokens[1], ''.join(tokens[2:])
    line_dt = datetime(current_dt.year, current_dt.month, current_dt.day, 0, 0)
    extra_hour = 0

    try:
        hours = int(hours)
    except ValueError:
        hours = current_dt.hour

    try:
        minutes = int(minutes)
    except ValueError:
        if (hours == current_dt.hour) or (hours == current_dt.hour):
            minutes = current_dt.minute
        else:
            minutes = 0
    else:
        if 0 < minutes < current_dt.minute and (hours >= current_dt.hour):
            extra_hour = 1

    minute_delta = timedelta(hours=extra_hour, minutes=minutes)

    if hours < current_dt.hour:
        hour_delta = timedelta(days=1, hours=hours)
    else:
        hour_delta = timedelta(hours=hours)
    line_dt = line_dt + minute_delta + hour_delta
    day = 'today' if line_dt.day == current_dt.day else 'tomorrow'

    return '{:%-H:%M} {} - {}'.format(line_dt, day, command)
