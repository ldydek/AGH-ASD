# u - węzeł drzewa
# f(u) - wartość najlepszej imprezy w poddrzewie zakorzenionym w "u"
# g(u) - jak wyżej, ale tym razem mamy zagwarantowane, że "u" nie idzie na imprezę
# Rozwiązanie: f(root)

class Employee:
    def __init__(self, fun):
        self.fun = fun
        self.emp = []
        self.f = -1
        self.g = -1


def company_party(a):
    return ff(a)


def gf(v):
    if v.g != -1:
        return v.g
    v.g = 0
    for u in v.emp:
        v.g += ff(u)
    return v.g


def ff(v):
    if v.f != -1:
        return v.f
    f1 = gf(v)
    f2 = v.fun
    for u in v.emp:
        f2 += gf(u)
    v.f = max(f1, f2)
    return v.f


a = Employee(50)
b = Employee(10)
c = Employee(25)
d = Employee(40)
e = Employee(15)
f = Employee(0)
g = Employee(25)
h = Employee(0)
i = Employee(0)
j = Employee(0)
k = Employee(0)
l = Employee(0)
m = Employee(5)
n = Employee(70)
o = Employee(15)
p = Employee(10)
r = Employee(6)
s = Employee(17)
t = Employee(500)
u = Employee(20)
w = Employee(10)
z = Employee(100)
a.emp.append(b)
a.emp.append(c)
a.emp.append(d)
b.emp.append(e)
b.emp.append(f)
b.emp.append(g)
f.emp.append(h)
f.emp.append(i)
i.emp.append(j)
i.emp.append(k)
i.emp.append(l)
d.emp.append(m)
d.emp.append(n)
d.emp.append(o)
d.emp.append(p)
m.emp.append(r)
m.emp.append(s)
o.emp.append(t)
o.emp.append(u)
t.emp.append(w)
w.emp.append(z)
print(company_party(a))
