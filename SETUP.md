# Setup del Entorno Forecasting Retail

## Entorno Conda Creado ✅

**Nombre del entorno:** `forecasting_retail`
**Python:** 3.11
**Estado:** Limpio y coherente

## Librerías Instaladas

### Core Data Science
- `numpy==2.0.2` - Computación numérica
- `pandas==2.2.3` - Manipulación de datos
- `matplotlib==3.9.2` - Visualización
- `seaborn==0.13.2` - Gráficos estadísticos

### Limpieza y Procesamiento de Datos
- `pyjanitor==0.28.0` - Métodos de limpieza para pandas ✅
- `openpyxl==3.1.5` - Lectura/escritura de Excel
- `sqlalchemy==2.0.36` - ORM y conexiones SQL

### Utilidades
- `python-dotenv==1.0.1` - Variables de entorno
- `pandas-flavor==0.8.1` - Decoradores para pandas
- `requests==2.32.3` - Solicitudes HTTP

### Jupyter & Notebooks
- `jupyter==1.1.1` - Interfaz Jupyter
- `jupyterlab==4.2.5` - JupyterLab
- `ipython==8.28.0` - IPython
- `ipykernel==6.29.5` - Kernel para Jupyter

## Cómo Usar el Entorno

### Activar el entorno
```bash
conda activate forecasting_retail
```

### Ejecutar Jupyter con este entorno
```bash
jupyter lab
# o
jupyter notebook
```

### Ejecutar scripts Python
```bash
conda run -n forecasting_retail python script.py
```

### Instalar nuevas librerías (dentro del entorno activo)
```bash
conda activate forecasting_retail
pip install nombre-paquete
```

## Notas Técnicas

✅ **Compatibilidad:** pyjanitor 0.28.0 es completamente compatible con pandas 2.2.3
✅ **Python 3.11:** Versión estable para data science
✅ **Reproducibilidad:** Archivos de configuración disponibles:
   - `requirements.txt` - Dependencias pip
   - `environment.yml` - Configuración conda completa

## Verificar que todo funciona

Desde una terminal con el entorno activo:
```bash
python -c "import janitor; import pandas; print('✅ Todo funciona correctamente')"
```

## Solucionar Problemas

### Si aparece error de janitor
```bash
pip install --upgrade pyjanitor
```

### Recrear el entorno desde cero
```bash
conda env remove -n forecasting_retail
conda create -n forecasting_retail python=3.11
conda run -n forecasting_retail pip install -r requirements.txt
```

---
**Fecha de creación:** 2026-06-11
**Versión:** 1.0
