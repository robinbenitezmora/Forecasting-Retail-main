#!/usr/bin/env python
"""Test que todos los imports del notebook funcionan correctamente."""

import sys

# Test imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dotenv import load_dotenv
import janitor
import os
from pathlib import Path
import openpyxl
import sqlalchemy as sa

print("✅ TODOS LOS IMPORTS FUNCIONAN CORRECTAMENTE")
print(f"✅ Janitor versión: {janitor.__version__}")
print(f"✅ Pandas versión: {pd.__version__}")
print(f"✅ NumPy versión: {np.__version__}")
print("\n✅ El notebook está listo para usar")
