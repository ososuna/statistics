# Here Ivan xd
from scipy.stats import chi2_contingency 
  
data = [[207, 282, 241], [234, 242, 232]] 
stat, p, dof, expected = chi2_contingency(data) 
  
alpha = 0.05
print("p value is " + str(p)) 
if p <= alpha: 
    print('Dependent(reject H0)') 
else: 
    print('Independent(H0 holds true)')
