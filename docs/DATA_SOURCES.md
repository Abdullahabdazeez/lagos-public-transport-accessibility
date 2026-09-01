# Data sources

| Dataset | Provider | Resolution / scale | Use |
|---|---|---|---|
| Lagos administrative boundaries | geoBoundaries / project-prepared layers | ADM1 and ADM2 | State and LGA reporting units |
| Public transport features | OpenStreetMap | Vector points | Bus, rail, ferry and other transit features |
| Pedestrian street network | OpenStreetMap | Vector graph | Network-based walking-time analysis |
| WorldPop 2020 | WorldPop | 100 m | Population exposure and accessibility aggregation |

## Archived-data note

The full walk-network GeoPackage and GraphML files were omitted from GitHub because they are approximately 60 MB and 146 MB. A sample network is included, and the full network can be regenerated using the provided script. OpenStreetMap is dynamic, so regenerated data may differ from the project snapshot.

The project raster contains approximately 11.48 million people when finite cell values are summed. The project workflow used a normalised statewide population total of 11.61 million; 11.54 million people were successfully assigned to LGAs, representing 99.40% of the analysis total.
