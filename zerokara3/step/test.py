import numpy as np
x = np.array(1)
print(x.ndim) # スカラ

x = np.array([1, 2, 3])
print(x.ndim) # ベクトル

x = np.array([[1, 2, 3], [4, 5, 6]])
print(x.ndim) # 行列
