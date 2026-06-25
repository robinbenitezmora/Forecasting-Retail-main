#!/usr/bin/env python
"""
Script para verificar que el entorno forecasting_retail está correctamente configurado.
Ejecutar con: python verify_environment.py
"""

import sys
from pathlib import Path

def check_package(name, min_version=None):
    """Verificar si un paquete está instalado."""
    try:
        module = __import__(name)
        version = getattr(module, '__version__', 'desconocida')
        print(f"✅ {name:20} {version}")
        return True
    except ImportError:
        print(f"❌ {name:20} NO INSTALADO")
        return False

def main():
    print("\n" + "="*60)
    print("VERIFICACIÓN DEL ENTORNO: forecasting_retail")
    print("="*60 + "\n")

    print("Python:", sys.version.split()[0])
    print("\nLibrerías instaladas:\n")

    packages = [
        'numpy',
        'pandas',
        'matplotlib',
        'seaborn',
        'janitor',
        'openpyxl',
        'sqlalchemy',
        'dotenv',
        'jupyter',
        'ipykernel',
    ]

    all_ok = all(check_package(pkg) for pkg in packages)

    print("\n" + "="*60)
    if all_ok:
        print("✅ ENTORNO LISTO PARA USAR")
    else:
        print("⚠️  Algunas librerías no están instaladas")
    print("="*60 + "\n")

    # Prueba funcional
    print("Prueba funcional de janitor + pandas:")
    try:
        import pandas as pd
        import janitor

        df = pd.DataFrame({'nombre': ['Alice', 'Bob'], 'edad': [25, 30]})
        df_limpio = df.clean_names()
        print(f"✅ DataFrame limpiado correctamente: {list(df_limpio.columns)}")
    except Exception as e:
        print(f"❌ Error en prueba funcional: {e}")

    print()

if __name__ == '__main__':
    main()
