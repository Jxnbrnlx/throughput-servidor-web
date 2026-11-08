
import os
import numpy as np
import matplotlib.pyplot as plt

# Datos de referencia del procesador
procesador = "Intel Core i9-13900T"
nucleos = 24
hilos_procesador = 32
cpu_mark = 42839
tdp = 35

# Modelo matematico hipotetico
A = 1000
hilos_optimos = hilos_procesador

def throughput(x):
    return (A * x) / (1 + (x / hilos_optimos)**2)

def primera_derivada(x):
    return A * (1 - (x / hilos_optimos)**2) / (
        1 + (x / hilos_optimos)**2
    )**2

def segunda_derivada(x):
    return (
        -2 * A * x / hilos_optimos**2
        * (3 - (x / hilos_optimos)**2)
        / (1 + (x / hilos_optimos)**2)**3
    )

# Resultados
rendimiento_maximo = throughput(hilos_optimos)

print("===== PROCESADOR =====")
print("Modelo:", procesador)
print("Nucleos:", nucleos)
print("Hilos:", hilos_procesador)
print("CPU Mark:", cpu_mark)
print("TDP:", tdp, "W")

print("\n===== RESULTADOS DEL MODELO =====")
print("Hilos optimos:", hilos_optimos)
print("Throughput maximo:", round(rendimiento_maximo, 2), "TPS")
print("Primera derivada:", primera_derivada(hilos_optimos))
print("Segunda derivada:", segunda_derivada(hilos_optimos))

print("\n===== TABLA DE RENDIMIENTO =====")
for x in range(0, 65, 4):
    print(x, "|", round(throughput(x), 2), "TPS")

# Generar grafica
hilos = np.linspace(0, 64, 300)
rendimientos = throughput(hilos)

os.makedirs("resultados", exist_ok=True)

plt.figure(figsize=(10, 6))
plt.plot(hilos, rendimientos, label="Throughput estimado")
plt.scatter(
    hilos_optimos,
    rendimiento_maximo,
    color="red",
    label="Maximo rendimiento"
)

plt.axvline(
    hilos_optimos,
    color="gray",
    linestyle="--",
    label="32 hilos"
)

plt.title("Throughput estimado - Intel Core i9-13900T")
plt.xlabel("Numero de hilos concurrentes")
plt.ylabel("Transacciones por segundo (TPS)")
plt.legend()
plt.grid(True)

plt.savefig("resultados/grafica.png", dpi=300)
plt.show()
