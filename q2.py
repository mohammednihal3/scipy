from scipy.optimize import minimize

def cost(x):
    return x[0]**2 - 10*x[0] + 40

result = minimize(cost, x0=[0], bounds=[(0, 100)])
print("Best quantity:", result.x[0])
print("Minimum cost:", result.fun)