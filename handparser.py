import tensorflow as tf
import pipeline


def learn():
    # Import data
    train_labels, train_data = pipeline.pipetrain
    test_labels, test_data = pipeline.pipetest

    # Create model
    x = tf.placeholder(tf.float32, [None, 3600])
    w = tf.Variable(tf.zeros([3600, 3]), name='w')
    b = tf.Variable(tf.zeros([3]), name='b')
    y = tf.matmul(x, w) + b

    # Define loss/optimizer
    y_ = tf.placeholder(tf.float32, [None, 3])

    # Cross-entropy/training steps
    cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
    t_step = tf.train.GradientDescentOptimizer(0.4).minimize(cross_entropy)

    sess = tf.InteractiveSession()
    tf.global_variables_initializer().run()
    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    saver = tf.train.Saver()

    # Train
    for i in range(1101):  # TODO Recheck loops for new images
        sess.run(t_step, feed_dict={x: train_data, y_: train_labels})
        if i % 50 == 0:  # TODO Modify step for loop change
            saver.save(sess, 'model\my_training', global_step=i)
            tr_acc = accuracy.eval(feed_dict={x: train_data, y_: train_labels})
            print("step %d, accuracy %g" % (i, tr_acc))

    # Results
    print(accuracy.eval(feed_dict={x: test_data, y_: test_labels}))
    sess.close()


if __name__ == '__main__':
    learn()
