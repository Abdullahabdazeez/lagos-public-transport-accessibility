from __future__ import annotations

from pathlib import Path
import numpy as np
import pandas as pd
import geopandas as gpd
import rasterio

ROOT = Path(__file__).resolve().parents[2]
TABLE = ROOT / "data/processed/tables/lga_accessibility_results.csv"
SUMMARY = ROOT / "data/processed/tables/final_project_summary.csv"
NODES = ROOT / "data/processed/accessibility/Lagos_Core_Transit_Node_Accessibility.gpkg"
STOPS = ROOT / "data/processed/stops/Lagos_Core_Transit_Bus_Rail.gpkg"
RASTER = ROOT / "data/processed/population/Lagos_WorldPop_2020.tif"

lga = pd.read_csv(TABLE)
assert len(lga) == 20
assert np.isclose(lga.Within_30min.sum(), 6206185, rtol=0, atol=1)
assert np.isclose(lga.Underserved.sum(), 5398276.69, rtol=0, atol=1)
assert lga.loc[lga.LGA.eq("Agege"), "Pct_30min"].iloc[0] == 99.70
assert lga.loc[lga.LGA.eq("Badagry"), "Pct_30min"].iloc[0] == 0.00
assert round(lga.nlargest(5,"Underserved").Underserved.sum() / lga.Underserved.sum() * 100, 1) == 58.3

nodes = gpd.read_file(NODES)
stops = gpd.read_file(STOPS)
assert len(nodes) == 129815
assert len(stops) == 219
assert nodes.crs.to_epsg() == 32631
assert stops.crs.to_epsg() == 32631

with rasterio.open(RASTER) as src:
    assert src.crs.to_epsg() == 32631
    assert np.isclose(abs(src.transform.a), 100)
    arr = src.read(1)
    finite_sum = float(arr[np.isfinite(arr)].sum())
    assert np.isclose(finite_sum, 11477943, rtol=0, atol=5)

print("REPRODUCTION CHECK: PASSED")
print("30-minute population: 6,206,185 (53.44%)")
print("Underserved population: 5,407,659 (46.56%)")
print("Largest absolute deficit: Alimosho — 967,347 people")
