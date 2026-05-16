import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
import matplotlib.pyplot as plt

# Load dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize images
x_train = x_train / 255.0
x_test = x_test / 255.0

# Show one image
plt.imshow(x_train[0], cmap='gray')
plt.title(f"Digit: {y_train[0]}")
plt.show()

# Build AI model
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# Compile model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train AI
model.fit(x_train, y_train, epochs=5)

# Test AI
loss, accuracy = model.evaluate(x_test, y_test)

#Save model
model.save("digit_model.h5")

print("Accuracy:", accuracy)

# Predict
prediction = model.predict(x_test)

# Show image
plt.imshow(x_test[0], cmap='gray')

predicted_digit = prediction[0].argmax()

plt.title(f"Predicted: {predicted_digit}")

print("Predicted Digit:", predicted_digit)
print("Actual Digit:", y_test[0])

plt.show()

