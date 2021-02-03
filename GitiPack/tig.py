import time


def ctig():
    global f
    f = open("GITI-Web-Go!.tig", 'a', encoding="UTF-8")
    f.write("————————————\n")
    ti = time.strftime("%Y-%m-%d %H:%M:%S\n", time.gmtime())
    f.write(ti)

def webg():
    f.write("Deal with: giti-web.github.io\n")

def ctime():
    return time.time()

def mtime():
    return time.ctime()

def stime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime())

# ——————————

def w(r):
    f.write(r)
    f.write('\n')

# ——————————

def jc(n):
    if n == 1:
        return 1
    else:
        return jc(n-1)*n

def pertion(l, s, e):
    w("进行全排列")
    if s == e:
        w(l)
    else:
        for i in range(s,e+1):
            l[s],l[i]=l[i],l[s]
            # 将这个元素和第一个元素交换
            pertion(l,s+1,e)
            l[s],l[i]=l[i],l[s]
            # 换回位置

