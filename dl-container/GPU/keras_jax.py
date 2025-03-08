import os

# This guide can only be run with the jax backend.
os.environ["KERAS_BACKEND"] = "jax"

import jax

# We import TF so we can use tf.data.
import tensorflow as tf
import keras
import numpy as np

def get_model():
    inputs = keras.Input(shape=(784,), name="digits")
    x1 = keras.layers.Dense(64, activation="relu")(inputs)
    x2 = keras.layers.Dense(64, activation="relu")(x1)
    outputs = keras.layers.Dense(10, name="predictions")(x2)
    model = keras.Model(inputs=inputs, outputs=outputs)
    return model


model = get_model()

# Prepare the training dataset.
batch_size = 32
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train = np.reshape(x_train, (-1, 784)).astype("float32")
x_test = np.reshape(x_test, (-1, 784)).astype("float32")
y_train = keras.utils.to_categorical(y_train)
y_test = keras.utils.to_categorical(y_test)

# Reserve 10,000 samples for validation.
x_val = x_train[-10000:]
y_val = y_train[-10000:]
x_train = x_train[:-10000]
y_train = y_train[:-10000]

# Prepare the training dataset.
train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))
train_dataset = train_dataset.shuffle(buffer_size=1024).batch(batch_size)

# Prepare the validation dataset.
val_dataset = tf.data.Dataset.from_tensor_slices((x_val, y_val))
val_dataset = val_dataset.batch(batch_size)

# Instantiate a loss function.
loss_fn = keras.losses.CategoricalCrossentropy(from_logits=True)

# Instantiate an optimizer.
optimizer = keras.optimizers.Adam(learning_rate=1e-3)

def compute_loss_and_updates(trainable_variables, non_trainable_variables, x, y):
    y_pred, non_trainable_variables = model.stateless_call(
        trainable_variables, non_trainable_variables, x, training=True
    )
    loss = loss_fn(y, y_pred)
    return loss, non_trainable_variables

grad_fn = jax.value_and_grad(compute_loss_and_updates, has_aux=True)

@jax.jit
def train_step(state, data):
    trainable_variables, non_trainable_variables, optimizer_variables = state
    x, y = data
    (loss, non_trainable_variables), grads = grad_fn(
        trainable_variables, non_trainable_variables, x, y
    )
    trainable_variables, optimizer_variables = optimizer.stateless_apply(
        optimizer_variables, grads, trainable_variables
    )
    # Return updated state
    return loss, (
        trainable_variables,
        non_trainable_variables,
        optimizer_variables,
    )

# Build optimizer variables.
optimizer.build(model.trainable_variables)

trainable_variables = model.trainable_variables
non_trainable_variables = model.non_trainable_variables
optimizer_variables = optimizer.variables
state = trainable_variables, non_trainable_variables, optimizer_variables

# Training loop
for step, data in enumerate(train_dataset):
    data = (data[0].numpy(), data[1].numpy())
    loss, state = train_step(state, data)
    # Log every 100 batches.
    if step % 100 == 0:
        print(f"Training loss (for 1 batch) at step {step}: {float(loss):.4f}")
        print(f"Seen so far: {(step + 1) * batch_size} samples")
