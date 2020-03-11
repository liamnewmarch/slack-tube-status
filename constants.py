# Line identifiers
BAKERLOO = 'bakerloo'
CENTRAL = 'central'
CIRCLE = 'circle'
DISTRICT = 'district'
DLR = 'dlr'
ELIZABETH = 'elizabeth'
HAMMERSMITH_AND_CITY = 'hammersmith-city'
JUBILEE = 'jubilee'
LONDON_OVERGROUND = 'london-overground'
METROPOLITAN = 'metropolitan'
NORTHERN = 'northern'
PICCADILLY = 'piccadilly'
TFL_RAIL = 'tfl-rail'
VICTORIA = 'victoria'
WATERLOO_AND_CITY = 'waterloo-city'


# Service status codes
SUSPENDED = 2
PART_SUSPENDED = 3
SEVERE_DELAYS = 6
MINOR_DELAYS = 9
PART_CLOSED = 11
SERVICE_CLOSED = 20


LINE_COLOURS = {
    BAKERLOO: '894e24',
    CENTRAL: 'dc241f',
    CIRCLE: 'ffce00',
    DISTRICT: '007229',
    DLR: '00afad',
    ELIZABETH: '6950a1',
    HAMMERSMITH_AND_CITY: 'd799af',
    JUBILEE: '6a7278',
    LONDON_OVERGROUND: 'e86a10',
    METROPOLITAN: '751056',
    NORTHERN: '000000',
    PICCADILLY: '0019a8',
    TFL_RAIL: '0019a8',
    VICTORIA: '00a0e2',
    WATERLOO_AND_CITY: '76d0bd',
}


STATUS_EMOJI = {
    SUSPENDED: ':no_entry:',
    PART_SUSPENDED: ':no_entry:',
    SEVERE_DELAYS: ':bangbang:',
    MINOR_DELAYS: ':warning:',
    PART_CLOSED: ':no_entry:',
    SERVICE_CLOSED: ':no_entry:',
}
