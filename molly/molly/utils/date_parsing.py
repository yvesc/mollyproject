import email.utils
import xml.utils.iso8601
from datetime import datetime, timedelta, tzinfo

class tz(tzinfo):
    def __init__(self, offset):
        self._offset = offset
    def utcoffset(self, dt):
        return timedelta(seconds=self._offset)
    def dst(self, dt):
        return timedelta(0)
    def __repr__(self):
        return "%02d%02d" % (self._offset//3600, (self._offset//60) % 60)

def rfc_2822_datetime(value):
    time_tz = email.utils.parsedate_tz(value)

    return datetime(*(time_tz[:6] + (0, tz(time_tz[9]))))

def iso_8601_datetime(value):
    return datetime.fromtimestamp(xml.utils.iso8601.parse(value))