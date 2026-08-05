from __future__ import annotations

from pathlib import Path
import numpy as np
import pandas as pd
import geopandas as gpd
import rasterio
from rasterio.transform import xy
from scipy.spatial import cKDTree

ROOT = Path(__file__).resolve().parents[2]
POP = ROOT / "data/processed/population/Lagos_WorldPop_2020.tif"
NODES = ROOT / "data/generated/Lagos_Core_Transit_Node_Accessibility.gpkg"
LGAS = ROOT / "data/processed/boundaries/Lagos_LGA_Boundaries.gpkg"
OUT = ROOT / "data/generated/Lagos_LGA_Accessibility_Recreated.csv"
MAX_CONNECTOR_M = 500.0

nodes = gpd.read_file(NODES).to_crs(32631)
node_xy = np.column_stack((nodes.geometry.x, nodes.geometry.y))
tree = cKDTree(node_xy)

with rasterio.open(POP) as src:
    arr = src.read(1)
    valid = np.isfinite(arr) & (arr > 0)
    rows, cols = np.where(valid)
    xs, ys = xy(src.transform, rows, cols, offset="center")
    pop = arr[valid].astype(float)
    crs = src.crs

points = gpd.GeoDataFrame(
    {"Population": pop}, geometry=gpd.points_from_xy(xs, ys), crs=crs
).to_crs(32631)

dist, idx = tree.query(np.column_stack((points.geometry.x, points.geometry.y)), k=1)
points["Connector_m"] = dist
points["Transit_Walk_Min"] = np.where(
    dist <= MAX_CONNECTOR_M, nodes.iloc[idx]["Transit_Walk_Min"].to_numpy(), np.nan
)
points["Within_30min"] = points["Transit_Walk_Min"].le(30)
points["Underserved"] = ~points["Within_30min"]

lgas = gpd.read_file(LGAS).to_crs(32631).rename(columns={"shapeName":"LGA"})
joined = gpd.sjoin(points, lgas[["LGA","geometry"]], predicate="within", how="left")
summary = joined.groupby("LGA").apply(
    lambda x: pd.Series({
        "Population": x.Population.sum(),
        "Within_30min": x.loc[x.Within_30min, "Population"].sum(),
        "Underserved": x.loc[x.Underserved, "Population"].sum(),
    }), include_groups=False
).reset_index()
summary["Pct_30min"] = 100 * summary.Within_30min / summary.Population
summary["Pct_Underserved"] = 100 * summary.Underserved / summary.Population
summary.to_csv(OUT, index=False)
print(f"Saved recreated summary to {OUT}")
