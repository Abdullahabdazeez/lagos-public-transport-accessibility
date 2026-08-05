from __future__ import annotations
from pathlib import Path
import json, sys
import numpy as np
import pandas as pd
import geopandas as gpd
import rasterio

ROOT=Path(__file__).resolve().parents[1]
fail=[]
required=[
 'README.md','project.json','LICENSE','CITATION.cff','requirements.txt',
 'assets/project-cover.png','assets/repository-social-preview.png',
 'data/processed/boundaries/Lagos_LGA_Boundaries.gpkg',
 'data/processed/stops/Lagos_Core_Transit_Bus_Rail.gpkg',
 'data/processed/accessibility/Lagos_Core_Transit_Node_Accessibility.gpkg',
 'data/processed/tables/lga_accessibility_results.csv',
 'outputs/maps/01_30min_accessibility_by_lga.png',
 'scripts/python/reproduce_summary.py'
]
for rel in required:
    if not (ROOT/rel).is_file(): fail.append(f'Missing: {rel}')
for p in ROOT.rglob('*'):
    if p.is_file() and '.git' not in p.parts:
        mb=p.stat().st_size/1024/1024
        if mb>24: fail.append(f'Browser-upload risk: {p.relative_to(ROOT)} ({mb:.1f} MB)')
try:
    meta=json.loads((ROOT/'project.json').read_text())
    if meta.get('underserved_percent')!=46.56: fail.append('Incorrect underserved percentage')
except Exception as e: fail.append(f'project.json error: {e}')
try:
    lga=pd.read_csv(ROOT/'data/processed/tables/lga_accessibility_results.csv')
    if len(lga)!=20: fail.append('Expected 20 LGAs')
    if not np.isclose(lga.Within_30min.sum(),6206185,atol=1): fail.append('Within-30 total mismatch')
    if lga.loc[lga.LGA.eq('Agege'),'Pct_30min'].iloc[0] != 99.70: fail.append('Agege result mismatch')
except Exception as e: fail.append(f'Table validation error: {e}')
try:
    stops=gpd.read_file(ROOT/'data/processed/stops/Lagos_Core_Transit_Bus_Rail.gpkg')
    nodes=gpd.read_file(ROOT/'data/processed/accessibility/Lagos_Core_Transit_Node_Accessibility.gpkg')
    if len(stops)!=219: fail.append('Core transit count mismatch')
    if len(nodes)!=129815: fail.append('Node count mismatch')
    if stops.crs.to_epsg()!=32631 or nodes.crs.to_epsg()!=32631: fail.append('CRS mismatch')
except Exception as e: fail.append(f'Vector validation error: {e}')
try:
    with rasterio.open(ROOT/'data/processed/population/Lagos_WorldPop_2020.tif') as src:
        if src.crs.to_epsg()!=32631: fail.append('Raster CRS mismatch')
        if not np.isclose(abs(src.transform.a),100): fail.append('Raster resolution mismatch')
except Exception as e: fail.append(f'Raster validation error: {e}')
if fail:
    print('REPOSITORY VALIDATION: FAILED')
    for x in fail: print('-',x)
    sys.exit(1)
print('REPOSITORY VALIDATION: PASSED')
print('Required files, statistics, feature counts, CRS, raster resolution and upload sizes are valid.')
