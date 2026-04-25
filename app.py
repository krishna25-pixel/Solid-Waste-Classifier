import gradio as gr
import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("model.keras")

classes = ["Electronics", "Organic", "Plastic", "Rubber", "Waste Wood"]

def predict(image):
    img = image.resize((224, 224))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    preds = model.predict(img)[0]
    return {classes[i]: float(preds[i]) for i in range(5)}

gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs="label"
).launch()