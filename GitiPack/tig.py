import time


def tig(object):
    global f
    f = open("GITI-Web-Go!.tig", 'a', encoding="UTF-8")
    f.write("————————————\n")
    ti = time.strftime("%Y-%m-%d %H:%M:%S\n", time.gmtime())
    f.write(ti)

def webg(self):
    f.write("Deal with: giti-web.github.io\n")
