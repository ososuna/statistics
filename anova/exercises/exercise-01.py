from scipy import stats

data = [
  {
    'id': 'a',
    'data': [5, 2, 7, 6, 9, 2, 1, 8]
  },
  {
    'id': 'b',
    'data': [6, 5, 8, 6, 2, 2, 1, 9]
  },
  {
    'id': 'c',
    'data': [7, 7, 6, 5, 4, 2, 3, 1]
  },
  {
    'id': 'd',
    'data': [9, 6, 7, 1, 5, 9, 4, 6]
  },
  {
    'id': 'e',
    'data': [8, 10, 8, 4, 6, 6, 9, 9]
  },
]

sumA = sum(a)
sumB = sum(b)
sumC = sum(c)
sumD = sum(d)
sumE = sum(e)


avgA = sum(a)/len(a)
avgB = sum(b)/len(b)
avgC = sum(c)/len(c)
avgD = sum(d)/len(d)
avgE = sum(e)/len(e)


n = len(a) + len(b) + len(c) + len(d) + len(e)
n


x_tested = (sum(a) + sum(b) + sum(d) + sum(c) + sum(e)) / n
x_tested


x_testedA = [ (i-x_tested)**2 for i in a ]
x_testedB = [ (i-x_tested)**2 for i in b ]
x_testedC = [ (i-x_tested)**2 for i in c ]
x_testedD = [ (i-x_tested)**2 for i in d ]
x_testedE = [ (i-x_tested)**2 for i in e ]


avg_testedA = [ (i-avgA)**2 for i in a ]
avg_testedB = [ (i-avgB)**2 for i in b ]
avg_testedC = [ (i-avgC)**2 for i in c ]
avg_testedD = [ (i-avgD)**2 for i in d ]
avg_testedE = [ (i-avgE)**2 for i in e ]


gl = n-1
scTotal = sum(x_testedA) + sum(x_testedB) + sum(x_testedC) + sum(x_testedD) + sum(x_testedE)


# n gruops - 1
glEntre = 5-1
scEntre = (8*(avgA - x_tested)**2) + (8*(avgB - x_tested)**2) + (8*(avgC - x_tested)**2) + (8*(avgD - x_tested)**2) + (8*(avgE - x_tested)**2)
s2e = scEntre/glEntre


# n - n groups
glIntra = n-5
scIntra = sum(avg_testedA) + sum(avg_testedB) + sum(avg_testedC) + sum(avg_testedD) + sum(avg_testedE)
s2r = scIntra/glIntra


f = s2e/s2r
gl = [scEntre, scIntra]
criticValue =  stats.f.isf(0.05, scEntre, scIntra)
criticValue

