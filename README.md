
# Rendimiento Maximo de Throughput en Servidores Web

## Universidad de La Salle
Ingenieria de Software - Calculo Diferencial

## Descripcion
Este proyecto estudia el rendimiento de un servidor web en funcion
del numero de hilos concurrentes mediante un modelo matematico.

Se utiliza calculo diferencial para encontrar el punto de
rendimiento maximo y analizar el comportamiento del servidor.

## Modelo matematico

T(x) = 500x / (1 + 0.0025x^2)

## Resultados principales

- Numero optimo de hilos: 20
- Throughput maximo: 5000 transacciones por segundo
- Primera derivada en el maximo: 0
- Segunda derivada en el maximo: -12.5

## Tecnologias utilizadas

- Python
- Matplotlib
- HTML
- CSS
- Google Colab
- GitHub

## Ejecucion del proyecto

1. Instalar Python.
2. Instalar Matplotlib con:

   pip install matplotlib

3. Ejecutar desde la carpeta principal:

   python codigo/simulacion.py

El programa generara la grafica en la carpeta resultados.

## Autores

Integrante 1
Integrante 2

## Universidad de La Salle
Proyecto Final de Calculo Diferencial
