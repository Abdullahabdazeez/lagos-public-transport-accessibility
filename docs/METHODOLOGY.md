# Methodology

## 1. Scope and study area

The analysis covers Lagos State and its 20 Local Government Areas. All spatial data are standardised to WGS 84 / UTM Zone 31N (EPSG:32631).

The project measures **walking accessibility to OSM-mapped formal/core public-transport access points**. It does not attempt to represent Lagos mobility in its entirety. Danfo minibuses, okada motorcycles, keke tricycles and other informal/paratransit services are not comprehensively represented in the retained transit dataset.

## 2. Transit-data audit

The retained transit layers were audited directly rather than interpreted from filenames alone. The final formal/core access foundation contains **219 bus/BRT/rail access points**. Explicit review found no comprehensive danfo, minibus, okada, keke or paratransit representation.

## 3. Walking network

The validated OpenStreetMap walking graph contains **129,815 nodes**. Its largest connected component contains 98.67% of graph nodes. Formal/core transit points were snapped to the network and assigned to graph components.

Multi-source shortest-path analysis was used to calculate the minimum walking time from network nodes to the nearest mapped formal/core transit access point. A walking speed of **4.8 km/h** was used where edge travel-time values were not already available.

## 4. Population integration

WorldPop 2020 is used as the population foundation. Positive-population raster cells are represented by cell centroids and connected to the nearest walking-network node.

Population is never discarded because it fails to connect within a chosen threshold. Instead, population outside the connector is retained explicitly as `Network_Gap`. Population connected to a walking component without a mapped formal-transit point is retained separately as `Connected_But_No_Formal_Transit_Path`.

## 5. Connector sensitivity

The original **500 m** population-to-network connector was reconstructed and retained as the reference scenario for comparability. It was tested against **250 m, 750 m and 1,000 m** alternatives.

The connector is treated as a modelling assumption between a population-cell centroid and the analysed walking graph, not as a universal acceptable walking-distance standard.

## 6. Accessibility thresholds

Accessibility is reported at four cumulative walking-time thresholds:

- 15 minutes
- 30 minutes
- 45 minutes
- 60 minutes

The 30-minute threshold is retained as the principal reference for comparison with the original project, but interpretation is not restricted to a single threshold.

## 7. LGA aggregation and service-gap typology

Population accessibility is aggregated by LGA. The final interpretation separates:

- structural walking-network gaps; and
- time-based formal-transit gaps where a valid graph path exists but walking time exceeds the reference threshold.

This distinction prevents network-connection failures from being conflated with long travel times.

## 8. Robustness

Statewide and LGA-level accessibility results were compared across the 250–1,000 m connector scenarios. The statewide 30-minute accessible share varies by less than one percentage point across the tested connectors, supporting retention of 500 m as the reference scenario while preserving the alternatives as sensitivity bounds.

## 9. Interpretation

The final 46.56% result refers to population that is more than 30 minutes from mapped formal/core transit or lies within a structural formal-network gap under the reference 500 m connector.

It must **not** be interpreted as the share of Lagos residents without transport. Informal/paratransit mobility remains outside the comprehensive coverage of the retained dataset.
