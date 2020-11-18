 

"""
Please note, this code is only for python 3+. If you are using python 2+, please modify the code accordingly.
"""
import tensorflow as tf
import numpy as np
tf.compat.v1.disable_eager_execution()

# create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3

### create tensorflow structure start ###
Weights = tf.Variable(tf.random.uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights*x_data + biases

loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.compat.v1.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.compat.v1.initialize_all_variables()
### create tensorflow structure end ###

sess = tf.compat.v1.Session()
sess.run(init)          # Very important

for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(Weights), sess.run(biases))


# 原来函数是这样写的：

# optimizer = tf.train.GradientDescentOptimizer
# 报错： AttributeError: module 'tensorflow_core._api.v2.train' has no attribute 'GradientDescentOptimizer'

# 此时应改为：

# optimizer = tf.compat.v1.train.GradientDescentOptimizer
# ————————————————
# 版权声明：本文为CSDN博主「小小谢先生」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/xiewenrui1996/article/details/102522887