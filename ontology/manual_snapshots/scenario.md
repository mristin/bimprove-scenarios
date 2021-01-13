<rasaeco-meta>
{
    "title": "Manual Snapshots",
    "contact": "Dag Fjeld Edvardsen <dag.fjeld.edvardsen@catenda.no>, Marko Ristin <rist@zhaw.ch>, Ruprecht Altenburger <altb@zhaw.ch>",
    "relations": [
        { "target": "digital_reconstruction", "nature": "images" }
    ],
    "volumetric": [
        {
            "aspect_from": "as-observed", "aspect_to": "as-observed",
            "phase_from": "construction", "phase_to": "construction",
            "level_from": "site", "level_to": "site"
        }
    ]
}
</rasaeco-meta>


## Summary

This scenario covers the case when an <ref name="actor_management#actor" /> manually captures
an <ref name="digital_reconstruction#image" /> to document the state of the construction site.

### Definitions

<def name="GPS_location">

This is the 3D location of a world as measured by the 
[GPS](https://en.wikipedia.org/wiki/Global_Positioning_System) of the user's device. 

</def>

## Scenario

### As-observed

We provide a web page that the user can update the image to.

We rely on the timestamp and the <ref name="GPS_location" /> embedded in the image.

We convert the <ref name="GPS_location" /> to <ref name="evolving_plan#site_coordinate_system" />.
We assume that we pinned down the mapping between the <ref name="GPS_location" />s and 
<ref name="evolving_plan#site_coordinate_system" /> during the configuration of the system.

The source of the <ref name="digital_reconstruction#image" />s are related to the 
<ref name="actor_management#actor" /> who made the <ref name="digital_reconstruction#image" />s.

(There is some need for tuning in <scenarioref name="unique_resource_identification" />, but this
is as good as it gets for a first sketch.)

*The remaining sections intentionally left empty.*