import time


class tig(object):
    def __init__(self):
        global f
        f = open("GITI-Web-Go!.tig", 'a', encoding="UTF-8")
        f.write("————————————\n")
        ti = time.strftime("%Y-%m-%d %H:%M:%S\n", time.gmtime())
        f.write(ti)

class webg():
    def __init__(self):
       f.write("Deal with: giti-web.github.io\n")

tig()
webg()
