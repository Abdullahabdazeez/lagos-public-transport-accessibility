from __future__ import annotations

from pathlib import Path
import geopandas as gpd
import osmnx as ox

ROOT = Path(__file__).resolve().parents[2]
BOUNDARY = ROOT / "data/processed/boundaries/Lagos_State_Boundary.gpkg"
OUTPUT = ROOT / "data/generated/Lagos_Walk_Network.graphml"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

boundary = gpd.read_file(BOUNDARY).to_crs(4326)
polygon = boundary.geometry.unary_union

# OSM is dynamic; this regenerates a current network rather than the archived snapshot.
G = ox.graph_from_polygon(polygon, network_type="walk", simplify=True, retain_all=True)
G = ox.project_graph(G, to_crs="EPSG:32631")
ox.save_graphml(G, OUTPUT)
print(f"Saved {len(G.nodes):,} nodes and {len(G.edges):,} directed edges to {OUTPUT}")
