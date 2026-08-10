# Formal Public-Transport Accessibility and Spatial Service Gaps in Lagos, Nigeria

## A Network-Based Population Accessibility Assessment

**Author:** Abdullah Abdazeez Ayomide

---

## Abstract

Lagos has an extensive and highly varied transport system in which formal mass-transit services operate alongside widespread informal mobility services. This study assesses walking accessibility to mapped formal/core public-transport access points across Lagos State using a pedestrian network and gridded population data. The analysis is explicitly limited to OpenStreetMap-mapped formal/core bus, Bus Rapid Transit and rail access points and therefore does not represent the full Lagos mobility system, particularly danfo minibuses, okada motorcycles, keke tricycles and other informal/paratransit services.

A total population of 11,613,844 was analysed using a walking-network model. A 500 m population-to-network connector was retained as the reference scenario, while 250 m, 750 m and 1,000 m connectors were evaluated as sensitivity scenarios. Accessibility was measured at 15-, 30-, 45- and 60-minute walking thresholds.

The results show that 2,557,743 people (22.02%) are within 15 minutes of mapped formal/core transit, 6,206,326 (53.44%) within 30 minutes, 8,350,756 (71.90%) within 45 minutes and 9,232,088 (79.49%) within 60 minutes. Under the reference scenario, 5,407,518 people (46.56%) are more than 30 minutes from mapped formal/core transit or are located within a structural walking-network gap.

Peripheral Local Government Areas show particularly weak formal-transit accessibility. However, these results should not be interpreted as evidence that residents lack transport generally because informal mobility systems are not comprehensively represented in the retained dataset. The findings instead identify spatial gaps in Lagos's mapped formal/core public-transport system and provide a basis for targeted formal-transit planning and network expansion.

## 1. Introduction

Lagos is Nigeria's largest metropolitan region and one of Africa's most complex urban transport environments. Movement across the city depends on a combination of formal mass-transit infrastructure and widespread informal mobility services. Formal systems include regulated bus services, Bus Rapid Transit corridors and rail services, while a large share of everyday mobility is also provided through danfo minibuses, motorcycle taxis, tricycles and other paratransit operations.

Because these systems are not represented equally in open geospatial datasets, accessibility studies can easily overstate transport deprivation if mapped formal-transit locations are treated as if they represent the complete mobility system. This study therefore focuses specifically on accessibility to mapped formal/core public-transport access points.

The objective is to identify where residents have strong or weak walking access to the mapped formal/core system and to examine how results change under multiple walking-time thresholds and population-to-network connector assumptions. The analysis is intended as a formal-transit planning assessment rather than a complete measurement of transport availability in Lagos.

## 2. Study Area

The study covers the 20 Local Government Areas of Lagos State, Nigeria. Lagos combines a dense urban core with rapidly developing suburban and peripheral areas. Population concentration, road-network structure and transit infrastructure vary considerably across the state, producing substantial differences in access to formal public transport.

The analysis uses a total population of 11.61 million based on the calibrated WorldPop 2020 population surface retained in the project. Accessibility is evaluated across the state's walking-network representation and mapped formal/core transit access points.

## 3. Data and Methodology

The analysis combines four principal spatial components: Local Government Area boundaries, WorldPop 2020 gridded population data, an OpenStreetMap-derived walking network and mapped formal/core transit access points.

The retained formal/core transit dataset contains 219 access points representing mapped bus, Bus Rapid Transit and rail locations. Explicit review of the source attributes found no comprehensive representation of danfo, okada, keke or other informal/paratransit modes. This limitation is treated as a fundamental scope condition rather than a minor data caveat.

Population raster cells were connected to their nearest walking-network nodes. The original 500 m connector was reconstructed and reproduced the previous project benchmark almost exactly. Because the connector distance is a modelling assumption rather than a universal walking standard, sensitivity tests were also completed at 250 m, 750 m and 1,000 m.

Walking times were calculated using the pedestrian network at a walking speed of 4.8 km/h. Multi-source shortest-path analysis measured the shortest walking time from each network node to the nearest mapped formal/core transit access point.

Accessibility was evaluated at 15-, 30-, 45- and 60-minute thresholds. Population that could not connect to the walking network within the tested connector distance was retained as a network gap rather than removed from the denominator. Population connected to a walking-network component with no mapped formal-transit access point was also retained separately as a structural gap.

## 4. Results

The final analysis includes 11,613,844 people across Lagos State.

At the 15-minute threshold, 2,557,743 people (22.02%) are within walking distance of mapped formal/core transit. Accessibility increases to 6,206,326 people (53.44%) within 30 minutes, 8,350,756 (71.90%) within 45 minutes and 9,232,088 (79.49%) within 60 minutes.

The reference 30-minute result therefore leaves 5,407,518 people (46.56%) either more than 30 minutes from mapped formal/core transit or within a structural walking-network gap.

The additional thresholds show why the original binary 30-minute interpretation was incomplete. While only just over half of the population reaches mapped formal/core transit within 30 minutes, almost 72% is within 45 minutes and almost 80% is within 60 minutes. The accessibility problem is therefore strongly sensitive to the travel-time standard used for interpretation.

### 4.1 Connector Sensitivity

The connector sensitivity test shows that statewide results are relatively stable once network topology and formal-transit component reachability are treated correctly. Across connector distances from 250 m to 1,000 m, the 30-minute accessible population varies by less than one percentage point.

The 500 m connector is therefore retained as the reference scenario because it reproduces the original project model and allows direct comparison with the earlier results. It should not be interpreted as an objectively correct or universally acceptable walking distance. The alternative connector scenarios are retained as uncertainty bounds.

### 4.2 Peripheral LGA Accessibility

The strongest formal-transit service gaps occur in peripheral parts of Lagos. Badagry records effectively no population within the 30-minute threshold, while Epe is also almost entirely beyond the reference 30-minute walking threshold. Ibeju-Lekki also shows very limited formal-transit accessibility.

Ikorodu presents a different pattern. Its walking-network connection is relatively strong, but only about one-quarter of its population is within 30 minutes of the mapped formal/core transit system. Its formal-access gap is therefore driven mainly by walking time to formal-transit locations rather than by basic network disconnection.

These findings should not be interpreted as indicating that these LGAs lack transport altogether. Informal mobility systems are known to play a substantial role in peripheral Lagos but are not comprehensively represented in the retained OpenStreetMap formal/core transit dataset.

## 5. Discussion

The results show a strong spatial inequality in access to Lagos's mapped formal public-transport system. Central and mature urban areas generally perform better, while several peripheral LGAs show much larger formal-transit service gaps.

The reconstruction also demonstrates the importance of distinguishing between transport accessibility and formal-transit accessibility. A model based primarily on mapped formal bus, Bus Rapid Transit and rail access points cannot support a general statement that residents beyond the threshold are transport deprived. Such a claim would ignore the important role of informal mobility.

The 46.56% figure should therefore be interpreted as the share of the analysis population that is more than 30 minutes from mapped formal/core transit or located within a structural walking-network gap under the reference connector. It is not the share of residents without transport.

This distinction is particularly important in Badagry, Epe, Ibeju-Lekki and Ikorodu, where informal and paratransit mobility is likely to reduce actual transport isolation even when formal-transit accessibility remains weak.

## 6. Planning Implications

The analysis identifies where expansion of Lagos's formal public-transport system may have the greatest spatial value.

Planning priorities include strengthening formal transit coverage in peripheral growth areas, improving pedestrian access to existing formal-transit corridors, integrating formal mass-transit planning with feeder services and recognising the role of informal mobility in network design.

Rather than treating informal operators as invisible, future accessibility studies should seek to integrate reliable danfo, keke and other paratransit route or stop information where defensible datasets become available.

The results can support corridor prioritisation, transit-oriented development planning, feeder-network design and accessibility monitoring. They should be combined with service frequency, affordability, travel reliability, safety and socioeconomic information before investment decisions are made.

## 7. Limitations

The most important limitation is modal representation. The transit dataset primarily represents mapped formal/core bus, Bus Rapid Transit and rail access points. Danfo minibuses, okada motorcycles, keke tricycles and other informal/paratransit systems are not comprehensively represented. The results therefore measure formal-transit accessibility rather than total transport accessibility.

The walking-network model also relies on OpenStreetMap completeness and assumes a constant walking speed. It does not explicitly account for road-crossing difficulty, pedestrian infrastructure quality, personal mobility constraints, weather, security or local barriers.

The population-to-network connector is a modelling assumption. Although sensitivity analysis shows the statewide 30-minute result is stable across the tested 250–1,000 m range, individual LGAs can show greater local sensitivity.

The study also measures proximity to transit access points rather than actual service performance. It does not include waiting time, service frequency, fare affordability, vehicle capacity, congestion, reliability or transfers.

## 8. Conclusion

This study assessed walking accessibility to mapped formal/core public transport across Lagos State using a population-weighted pedestrian-network model.

The final results show that 22.02% of the population is within 15 minutes of mapped formal/core transit, 53.44% within 30 minutes, 71.90% within 45 minutes and 79.49% within 60 minutes.

Under the reference 500 m population-to-network connector, 46.56% of the analysis population is more than 30 minutes from mapped formal/core transit or within a structural walking-network gap.

The main contribution of the reconstruction is not simply the updated statistics, but the correction of their interpretation. The results describe gaps in Lagos's mapped formal public-transport system and should not be interpreted as evidence that the same population lacks transport generally.

The analysis therefore provides a more defensible spatial basis for formal-transit expansion, pedestrian-access improvement and future multimodal accessibility assessment.

## Author Contribution

The author developed the geospatial problem formulation, reconstructed the walking-network accessibility model, evaluated connector sensitivity, interpreted the spatial service gaps and prepared the final planning recommendations and visual outputs.

The analysis, cartography and interpretation were developed as an independent geospatial-planning project.
