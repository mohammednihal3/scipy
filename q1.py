import numpy as np
from scipy import stats
marks = np.array([65, 70, 75, 80, 85, 90])
print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard deviation:", np.std(marks))
class_a = [70, 75, 80, 85, 90]
class_b = [60, 65, 70, 75, 80]
result = stats.ttest_ind(class_a, class_b)
print("T-statistic:", result.statistic)
print("P-value:", result.pvalue)