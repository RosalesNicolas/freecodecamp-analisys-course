import numpy as np

def calculate(vector):
    if len(vector) != 9:
        raise ValueError("List must contain nine numbers.")  # Lanza excepción si no son 9

    mat = np.array(vector).reshape((3, 3))  # Convierte el vector en 3x3
    
    dic = {
        'mean': [np.mean(mat, axis=0).tolist(), np.mean(mat, axis=1).tolist(), float(np.mean(mat))],
        'variance': [np.var(mat, axis=0).tolist(), np.var(mat, axis=1).tolist(), float(np.var(mat))],
        'standard deviation': [np.std(mat, axis=0).tolist(), np.std(mat, axis=1).tolist(), float(np.std(mat))],
        'max': [np.max(mat, axis=0).tolist(), np.max(mat, axis=1).tolist(), int(np.max(mat))],
        'min': [np.min(mat, axis=0).tolist(), np.min(mat, axis=1).tolist(), int(np.min(mat))],
        'sum': [np.sum(mat, axis=0).tolist(), np.sum(mat, axis=1).tolist(), int(np.sum(mat))]
    }
    
    # Imprime con formato similar al ejemplo
    print("{")
    for i, (k, v) in enumerate(dic.items()):
        comma = "," if i < len(dic) - 1 else ""  # Coma solo si no es el último
        print(f"    '{k}': {v}{comma}")
    print("}")

# Ejemplo
a = [0,1,2,3,4,5,6,7,8]
calculate(a)

