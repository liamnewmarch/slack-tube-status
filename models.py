from constants import LINE_COLOURS, STATUS_EMOJI


class Line:
    def __init__(self, line):
        self.key = line['id']
        self.name = line['name']
        self.statuses = line.get('lineStatuses', [])

    @property
    def color(self):
        return LINE_COLOURS.get(self.key, '000000')

    @property
    def disruptions(self):
        return ', '.join([
            Status(status).serialize() for status in self.statuses
        ])

    def serialize(self):
        return {
            'color': self.color,
            'text': f'{self.name}: {self.disruptions}',
        }


class Status:
    def __init__(self, status):
        self.severity = status['statusSeverity']
        self.description = status['statusSeverityDescription']

    @property
    def emoji(self):
        return STATUS_EMOJI.get(self.severity, '')

    def serialize(self):
        if self.emoji:
            return f'{self.emoji} {self.description}'
        return self.description


def transform_data(lines):
    return [Line(line).serialize() for line in lines]
