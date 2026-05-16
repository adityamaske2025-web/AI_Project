import tkinter as tk
from PIL import Image, ImageDraw
import numpy as np
import tensorflow as tf

# Load trained model
model = tf.keras.models.load_model("digit_model.h5")

# Create window
window = tk.Tk()
window.title("Digit Recognition AI")

# Create drawing canvas
canvas = tk.Canvas(window, width=280, height=280, bg='white')
canvas.pack()

# Create image for drawing
image = Image.new("L", (280, 280), color=255)
draw = ImageDraw.Draw(image)

# Draw function
def paint(event):
    x1, y1 = (event.x - 8), (event.y - 8)
    x2, y2 = (event.x + 8), (event.y + 8)

    canvas.create_oval(x1, y1, x2, y2, fill='black')
    draw.ellipse([x1, y1, x2, y2], fill=0)

canvas.bind("<B1-Motion>", paint)

# Predict function
def predict():
    img = image.resize((28, 28))

    img_array = np.array(img)

    img_array = img_array / 255.0
    img_array = 1 - img_array

    img_array = img_array.reshape(1, 28, 28)

    prediction = model.predict(img_array)

    digit = np.argmax(prediction)

    confidence = np.max(prediction) * 100

    label.config(
    text=f"Prediction: {digit} ({confidence:.2f}%)"
)

# Clear canvas
def clear():
    canvas.delete("all")

    draw.rectangle([0, 0, 280, 280], fill=255)

    label.config(text="Draw a digit")

# Buttons
predict_button = tk.Button(window, text="Predict", command=predict)
predict_button.pack()

clear_button = tk.Button(window, text="Clear", command=clear)
clear_button.pack()

# Prediction label
label = tk.Label(window, text="Draw a digit")
label.pack()

window.mainloop()