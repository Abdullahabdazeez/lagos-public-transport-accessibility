# Methodology

## 1. Boundary preparation

Lagos State and its 20 LGAs were projected to WGS 84 / UTM Zone 31N (EPSG:32631). Geometry validity and area were checked before spatial analysis.

## 2. Transit-data preparation

OpenStreetMap public-transport features were classified into bus, rail, ferry and other public-transport modes. Duplicate or co-located records were consolidated using spatial clustering. The final datasets contain 219 core bus/rail points and 348 multimodal points.

## 3. Walk-network analysis

A walk network was assembled from OpenStreetMap. The validated graph contained 129,815 nodes and 327,234 directed edges. Its largest weakly connected component contained 128,084 nodes, or 98.67% of the graph.

Core transit points were snapped to the nearest network node. Edge length was converted to walking time using a constant speed of 4.8 km/h. Multi-source shortest-path analysis produced the minimum walking time from each node to the nearest core transit access point.

## 4. Population integration

WorldPop 2020 cells were represented by their centre coordinates and connected to the nearest analysed network node where the connector distance did not exceed 500 m. Each cell inherited the node's walking time. Population outside the connector threshold or above 30 minutes was classified as underserved.

## 5. Aggregation

Population was summarised within 5, 10, 15 and 30 minutes and by LGA. LGA planning-priority classes were assigned from the proportion and absolute number of underserved residents.

## 6. Interpretation

The analysis measures geographic access to mapped transit points. It does not evaluate timetables, fares, service quality, congestion, transfer time, personal safety or disability-specific walking conditions.
