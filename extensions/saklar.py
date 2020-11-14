def cek(v):
    return saklar.lampu


def on(v):
    saklar.lampu = "on"


def off(v):
    saklar.lampu = "off"


class saklar(object):
    lampu = "off"
