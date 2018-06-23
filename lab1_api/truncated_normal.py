import tensorflow as tf
initial = tf.truncated_normal(shape=[3,3], mean=0, stddev=1, dtype=tf.float32, seed=1321)
print(tf.Session().run(initial))
