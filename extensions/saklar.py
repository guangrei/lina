def cek():
    return saklar.lampu


def on():
    if saklar.lampu == "on"
        return "gagal menyalakan lampu bosq, lampu sudah nyala!"
    else:
        saklar.lampu = "on"
        return "berhasil menyalakan lampu bosq"


def off():
    if saklar.lampu == "off"
        return "gagal mematikan lampu bosq, lampu sudah mati!"
    else:
        saklar.lampu = "on"
        return "berhasil mematikan lampu bosq"


class saklar(object):
    lampu = "off"
