# 🎯 Entorno Forecasting Retail - Guía de Uso

## ✅ Estado Actual

**Entorno:** `forecasting_retail`  
**Python:** 3.11.15  
**Estado:** ✅ Completamente funcional y coherente  
**Última actualización:** 2026-06-11

## 🚀 Inicio Rápido

### Opción 1: Usar Jupyter desde terminal

```bash
conda activate forecasting_retail
jupyter lab
```

Esto abrirá JupyterLab. Los notebooks usarán automáticamente este entorno.

### Opción 2: Usar desde VSCode

1. Abre VSCode
2. Presiona `Ctrl+Shift+P` (o `Cmd+Shift+P` en Mac)
3. Escribe: `Python: Select Interpreter`
4. Busca y selecciona `forecasting_retail`
5. Los notebooks ahora usarán este entorno

### Opción 3: Ejecución desde terminal

```bash
conda activate forecasting_retail
python script.py
```

## 📦 Paquetes Instalados

| Paquete | Versión | Propósito |
|---------|---------|-----------|
| **numpy** | 2.0.2 | Computación numérica |
| **pandas** | 2.2.3 | Manipulación de datos |
| **matplotlib** | 3.9.2 | Visualización estática |
| **seaborn** | 0.13.2 | Gráficos estadísticos |
| **pyjanitor** | 0.28.0 | ✅ Limpieza de datos |
| **openpyxl** | 3.1.5 | Lectura/escritura Excel |
| **sqlalchemy** | 2.0.36 | Conexiones SQL |
| **jupyter** | 1.1.1 | Interfaz Jupyter |
| **jupyterlab** | 4.2.5 | JupyterLab |
| **ipython** | 8.28.0 | Shell interactivo |

## ✅ Verificación

Para verificar que todo funciona correctamente:

```bash
python verify_environment.py
```

Deberías ver:
```
✅ ENTORNO LISTO PARA USAR
✅ DataFrame limpiado correctamente: ['nombre', 'edad']
```

## 📁 Archivos de Configuración

- **requirements.txt** - Dependencias para pip
- **environment.yml** - Configuración conda completa
- **verify_environment.py** - Script de verificación

## 🔄 Problemas Comunes

### El notebook dice "Kernel not found"
**Solución:**
```bash
conda activate forecasting_retail
python -m ipykernel install --user --name forecasting_retail
```

### Error "ModuleNotFoundError: No module named 'janitor'"
**Solución:**
```bash
conda activate forecasting_retail
pip install --upgrade pyjanitor
```

### Necesito instalar un nuevo paquete
```bash
conda activate forecasting_retail
pip install nombre-del-paquete
```

## 📋 Estructura del Proyecto

```
FORECASTING_RETAIL_I/
├── 01_Documentos/           # Documentación
├── 02_datos/                # Datos crudos
├── 03_notebooks/            # Jupyter notebooks ← Usar aquí
│   └── 01_Importacion_Datos.ipynb
├── 04_scripts/              # Scripts Python
├── 05_modelos/              # Modelos entrenados
├── 06_resultados/           # Resultados
├── 07_despliegue/           # Despliegue
├── requirements.txt         # ← Dependencias
├── environment.yml          # ← Configuración conda
├── SETUP.md                 # Guía de setup
├── verify_environment.py    # Script de verificación
└── README_ENTORNO.md        # Este archivo
```

## 🎓 Primer Pasos con Janitor

```python
import pandas as pd
import janitor

# Cargar datos
df = pd.read_csv('datos.csv')

# Limpiar nombres de columnas
df = df.clean_names()

# Eliminar espacios en blanco
df = df.remove_empty()

# Ver columnas
print(df.columns)
```

## 💾 Guardar/Restaurar Entorno

### Crear snapshot del entorno actual
```bash
conda list -n forecasting_retail > current_packages.txt
```

### Recrear entorno desde cero
```bash
conda env remove -n forecasting_retail -y
conda env create -f environment.yml
```

## 📞 Soporte

Si el entorno no funciona:
1. Ejecuta: `python verify_environment.py`
2. Revisa SETUP.md para instrucciones detalladas
3. Intenta recrear el entorno desde environment.yml

---

**Entorno creado:** 2026-06-11  
**Python:** 3.11  
**Status:** ✅ Producción
