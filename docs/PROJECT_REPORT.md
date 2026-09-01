# Project Report: Lagos Formal Public-Transport Accessibility

## Background

Lagos has a large and complex transport system, but access to the mapped formal network is not evenly distributed. I developed this project to estimate how easily residents can reach mapped formal/core bus, BRT and rail access points on foot and to identify where the largest service gaps appear.

The analysis is deliberately limited to the mapped formal/core system. Informal and paratransit services such as danfo, okada and keke are not comprehensively represented, so the results should not be read as a measure of total transport availability.

## What I did

I combined three main elements: a pedestrian street network, WorldPop 2020 population data and **219 mapped formal/core transit access points**.

I calculated walking time to the nearest mapped transit point and reported accessibility at 15, 30, 45 and 60 minutes. I also kept population locations that could not be connected reliably to the walking graph instead of dropping them from the analysis.

Because the way population cells are connected to a network can affect accessibility estimates, I tested connector distances of 250 m, 500 m, 750 m and 1,000 m. The 500 m version is retained as the reference model because the statewide 30-minute result remained stable across the alternatives.

## What I found

Under the reference model:

- **22.02%** of the analysed population is within 15 minutes of mapped formal/core transit;
- **53.44%** is within 30 minutes;
- **71.90%** is within 45 minutes; and
- **79.49%** is within 60 minutes.

At the 30-minute threshold, **5,407,518 people (46.56%)** are either farther than 30 minutes from mapped formal transit or affected by a structural walking-network gap.

Peripheral LGAs show some of the weakest formal-network access. Badagry records a 100% formal-transit service gap under the 30-minute reference threshold, while Epe is almost the same. Ikorodu also has a large gap, but its pattern is driven more by walking time than by structural network disconnection.

## What the result means

The analysis highlights where the mapped formal network is relatively hard to reach. That can support early thinking about formal-network expansion, feeder services, first/last-mile improvements and better walking connections to transit.

The result does **not** mean that everyone outside the 30-minute threshold lacks transport. Informal mobility is an important part of Lagos travel and is not fully represented here.

## Important limitations

The biggest limitation is modal coverage. The model also assumes a constant walking speed and does not directly include service frequency, waiting time, fares, reliability, congestion, transfer burden, pedestrian quality or personal mobility constraints.

WorldPop is a modelled population surface rather than a household census.

## What I would add next

The strongest extension would be a combined formal-and-informal transit dataset. Adding service frequency and fare information would also make the accessibility measure closer to what travellers actually experience.

A second useful extension would be to connect the service-gap results with employment, schools, healthcare and other destination data rather than measuring access to the transit network alone.

## Main outputs

The final maps are in [`assets/maps`](../assets/maps/), with charts in [`assets/charts`](../assets/charts/). The repository also contains the LGA summaries, connector-sensitivity results and validation documentation.

## Final note

This project reinforced an important distinction for me: an accessibility model is only as meaningful as the system it represents. Clear scope is therefore part of the analysis, not an afterthought.
