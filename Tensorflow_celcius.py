import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras

celsius = np.array([-100,-40,-10,0,8,15,22,38,0,200,50,349,140,105,100,
                    -25,-24,-23,-22,-21,-20,-19,-18,-17,-16,
                    -15,-14,-13,-12,-11,-10,-9,-8,-7,-6,
                    -5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10], dtype=float)

fahrenheit = np.array([-148,-40,-14,32,46,59,72,100,32,392,122,660.2,284,221,212,
                       -13,-11.2,-9.4,-7.6,-5.8,-4,-2.2,-0.4,1.4,3.2,
                       5,6.8,8.6,10.4,12.2,14,15.8,17.6,19.4,21.2,23,
                       24.8,26.6,28.4,30.2,32,33.8,35.6,37.4,39.2,41,42.8,44.6,46.4,48.2,50], dtype=float)


#capa = tf.keras.layers.Dense(units=1, input_shape=[1])
#modelo = tf.keras.Sequential([capa])

oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])
oculta2 = tf.keras.layers.Dense(units=3)
salida = tf.keras.layers.Dense(units=1)
modelo = tf.keras.Sequential([oculta1,oculta2,salida])

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

print("Comenzando entrenamiento")
historial = modelo.fit(celsius,fahrenheit, epochs=1000,verbose=False)
print("Modelo entrenando")

plt.xlabel("Epoca")
plt.ylabel("Magnitud de perdida")
plt.plot(historial.history["loss"])


# Predicting Fahrenheit temperature for 0 Celsius
celsius_to_predict = np.array([100])
predicted_fahrenheit = modelo.predict(celsius_to_predict)[0][0]
print("Predicted Fahrenheit temperature for 0 Celsius is:", predicted_fahrenheit, "F")
