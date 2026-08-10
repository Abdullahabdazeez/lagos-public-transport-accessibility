# Lagos Formal Public-Transport Accessibility and Service-Gap Analysis

## Overview

How easily can Lagos residents reach the city's **mapped formal/core public-transport network** on foot?

This project uses a validated OpenStreetMap walking network, WorldPop 2020 population data and **219 mapped formal/core bus, BRT and rail access points** to evaluate spatial accessibility across Lagos State.

The reconstructed analysis reports accessibility at **15, 30, 45 and 60 minutes** and explicitly tests the population-to-network connector at **250 m, 500 m, 750 m and 1,000 m**.

> **Important scope:** this is a formal/core public-transport accessibility analysis. Danfo minibuses, okada motorcycles, keke tricycles and other informal/paratransit services are not comprehensively represented. The results therefore identify gaps in access to the mapped formal/core transit system, not the absence of transport generally.

## Research Question

**How accessible is Lagos's mapped formal/core public-transport network to residents, and where are the largest spatial service gaps?**

## Study Area

Lagos State, Nigeria — 20 Local Government Areas.

## Analytical Foundation

| Project detail | Final specification |
|---|---|
| Population baseline | WorldPop 2020 |
| Analysis population | 11,613,844 |
| Formal/core transit access points | 219 |
| Walking-network nodes | 129,815 |
| Walking speed | 4.8 km/h |
| Reference population-to-network connector | 500 m |
| Connector sensitivity | 250 m, 500 m, 750 m, 1,000 m |
| Accessibility thresholds | 15, 30, 45, 60 minutes |
| Projection | WGS 84 / UTM Zone 31N (EPSG:32631) |

## Key Findings

- **2,557,743 people (22.02%)** are within 15 minutes' walk of mapped formal/core transit.
- **6,206,326 people (53.44%)** are within 30 minutes.
- **8,350,756 people (71.90%)** are within 45 minutes.
- **9,232,088 people (79.49%)** are within 60 minutes.
- **5,407,518 people (46.56%)** are more than 30 minutes from mapped formal/core transit or lie within a structural walking-network gap under the 500 m reference connector.
- The statewide 30-minute result is robust across the tested 250–1,000 m connector scenarios.
- Badagry records a **100.00% formal-transit service gap** under the 30-minute reference threshold; Epe records **99.99%**.
- Ikorodu records a **74.98% formal-transit service gap**, driven primarily by walking time rather than structural network disconnection.

## What the 46.56% Result Means

The **46.56%** figure does **not** mean that 46.56% of Lagos residents lack transport.

It means that, under the 500 m reference connector, that population is either:

1. more than 30 minutes' walk from the mapped formal/core transit network; or
2. within a structural walking-network gap relative to the mapped formal/core transit system.

This distinction is especially important in peripheral LGAs where informal mobility plays a major role.

## Methodology

1. Standardised Lagos State and 20 LGA boundaries in EPSG:32631.
2. Audited the retained OSM transit layers and confirmed the formal/core modal scope.
3. Reconstructed the 129,815-node pedestrian network and its connected components.
4. Snapped the 219 formal/core transit access points to the network.
5. Reconstructed WorldPop population-to-network connection.
6. Tested **250 m, 500 m, 750 m and 1,000 m** connector scenarios.
7. Retained population outside a connector threshold explicitly as `Network_Gap` rather than dropping it from the denominator.
8. Separated population connected to walking components without mapped formal transit from ordinary time-based accessibility gaps.
9. Calculated multi-source shortest walking times to the nearest mapped formal/core transit point.
10. Reported accessibility at **15, 30, 45 and 60 minutes**.
11. Aggregated results by LGA and separated structural from time-based formal-transit gaps.
12. Tested statewide and LGA-level sensitivity before locking the final interpretation.

## Connector Sensitivity

The original 500 m population-to-network connector was reconstructed rather than accepted uncritically. The reference 30-minute result remained stable when the connector was varied from 250 m to 1,000 m, so **500 m is retained for comparability**, while the alternative connectors remain documented sensitivity scenarios.

The connector is a modelling device between population-cell centroids and the analysed walking graph; it is not presented as a universal walking-distance standard.

## Peripheral Lagos

Peripheral LGAs show some of the weakest access to the mapped formal/core network:

- **Badagry:** 0.00% within 30 minutes; 100.00% formal-access gap.
- **Epe:** 0.01% within 30 minutes; 99.99% formal-access gap.
- **Ibeju-Lekki:** 3.46% within 30 minutes; 96.54% formal-access gap.
- **Ikorodu:** 25.02% within 30 minutes; 74.98% formal-access gap.

These figures must be interpreted as **formal-transit service gaps**, not general transport deprivation, because informal/paratransit services are incompletely represented.

## Planning Relevance

The outputs can support:

- formal transit network expansion;
- first/last-mile planning;
- pedestrian access improvements;
- feeder-service design;
- transit-oriented development screening;
- prioritisation of peripheral growth areas; and
- future integration of formal and informal mobility datasets.

They should be combined with service frequency, affordability, reliability, safety, transfers and socioeconomic information before investment decisions are made.

## Limitations

The largest limitation is **modal representation**. The mapped transit foundation primarily represents formal/core bus, BRT and rail access points. Danfo, okada, keke and other informal/paratransit systems are not comprehensively represented.

The model also assumes a constant walking speed and does not explicitly represent pedestrian-environment quality, crossing difficulty, personal mobility constraints, waiting time, fares, frequency, capacity, congestion, transfers or reliability. WorldPop is a modelled population surface rather than a household census.

See [`docs/LIMITATIONS.md`](docs/LIMITATIONS.md) for the full limitation register.

## Final Outputs

The validated reconstruction includes final formal-transit accessibility maps, multi-threshold charts, connector-robustness results, LGA service-gap typology, final GIS data and the concluded technical report.

## Author

**Abdullah Abdazeez Ayomide**  
Geo-spatial Planner | GIS & Remote Sensing Analyst | Environmental & Urban Planning Researcher

## Citation and Licence

Citation metadata is provided in [`CITATION.cff`](CITATION.cff). Code and original documentation are released under the repository licence. External datasets remain subject to their respective providers' terms.
