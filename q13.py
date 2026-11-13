from scipy.io import savemat, loadmat
data = {"marks": [70, 80, 90]}
savemat("student_data.mat", data)
loaded = loadmat("student_data.mat")
print(loaded["marks"])