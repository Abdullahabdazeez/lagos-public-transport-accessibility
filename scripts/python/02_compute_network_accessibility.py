from __future__ import annotations

from pathlib import Path
import networkx as nx
import osmnx as ox
import geopandas as gpd
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
GRAPH = ROOT / "data/generated/Lagos_Walk_Network.graphml"
STOPS = ROOT / "data/processed/stops/Lagos_Core_Transit_Bus_Rail.gpkg"
OUTPUT = ROOT / "data/generated/Lagos_Core_Transit_Node_Accessibility.gpkg"
WALK_SPEED_M_PER_MIN = 80.0  # 4.8 km/h

G = ox.load_graphml(GRAPH)
for _, _, _, data in G.edges(keys=True, data=True):
    data["walk_min"] = float(data["length"]) / WALK_SPEED_M_PER_MIN

stops = gpd.read_file(STOPS).to_crs(G.graph["crs"])
source_nodes = set(ox.distance.nearest_nodes(G, X=stops.geometry.x, Y=stops.geometry.y))

# Reverse the directed graph so one multi-source run returns node-to-stop travel time.
travel = nx.multi_source_dijkstra_path_length(G.reverse(copy=False), source_nodes, weight="walk_min")

nodes, _ = ox.graph_to_gdfs(G)
nodes["Transit_Walk_Min"] = nodes.index.map(travel)
nodes["Access_Class"] = pd.cut(
    nodes["Transit_Walk_Min"], bins=[-1,5,10,15,30,float("inf")],
    labels=["0–5 min","5–10 min","10–15 min","15–30 min",">30 min"]
)
nodes.reset_index().to_file(OUTPUT, layer="Node_Accessibility", driver="GPKG")
print(f"Saved node accessibility to {OUTPUT}")
