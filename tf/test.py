# coding:utf-8
import os
import tempfile
import tensorflow as tf
import matplotlib.pyplot as plt


def os_path():
    path = os.path.join(tempfile.gettempdir(), 'def.json')
    print(path)


def border_test():
    # 读取三通道图片
    input_image = tf.io.gfile.GFile('./data/img/01.png', 'rb').read()
    # 图片编码
    image_data = tf.image.decode_png(input_image)
    # tensorflow的浮点型
    image_show = tf.image.convert_image_dtype(image_data, dtype=tf.float32)
    # #原来的单张图片为三维（height,width,channel）而下文中卷积核定义为四维（batchsize，height,width,channel），因此通过该方法在0维添加一维，相当于将原来的单张图片三维数据放在一个另一个集合中从而形成四维
    image_batch = tf.expand_dims(image_show, axis=0)

    kernel = tf.constant(
        [
            [
                [-1.0, -1.0, -1.0], [0, 0, 0], [1.0, 1.0, 1.0]
            ],
            [
                [-2.0, -2.0, -2.0], [0, 0, 0], [2.0, 2.0, 2.0]
            ],
            [
                [-1.0, -1.0, -1.0], [0, 0, 0], [1.0, 1.0, 1.0]
            ]
        ],
        shape=[3, 3, 3, 1], dtype=tf.float32)
    with tf.compat.v1.Session() as sess:
        sess.run(image_show)
        conv2d = tf.nn.conv2d(image_batch, kernel, [1, 1, 1, 1], padding='SAME')
        # 激活措施加均值操作将颜色值置于（0~255）以内的区间
        activation_map = sess.run(tf.minimum(tf.nn.relu(conv2d), 255))
        print(activation_map.shape)
        # 注意该步骤将得到的四维np.array数据还原为三维。plt显示的前提
        encoded_image = activation_map.reshape([250, 200, 1])
        active = tf.image.convert_image_dtype(1 - encoded_image, dtype=tf.float32)
        print('dimensions', active)
        grayscale_reshape = tf.reshape(active, [250, 200])
        plt.imshow(grayscale_reshape.eval(), cmap='gray')
        plt.show()


if __name__ == '__main__':
    border_test()
