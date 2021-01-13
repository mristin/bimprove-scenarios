<rasaeco-meta>
{
    "title": "Thermal Inspection",
    "contact": "Alberto Palomero <Alberto.Palomero@hrs.ch>, Dag Fjeld Edvardsen <dag.fjeld.edvardsen@catenda.no>, Marko Ristin <rist@zhaw.ch>, Ruprecht Altenburger <altb@zhaw.ch>",
    "relations": [
    ],
    "volumetric": [
        {
            "aspect_from": "as-planned", "aspect_to": "as-observed",
            "phase_from": "construction", "phase_to": "construction",
            "level_from": "site", "level_to": "site"
        },
        {
            "aspect_from": "analytics", "aspect_to": "analytics",
            "phase_from": "construction", "phase_to": "construction",
            "level_from": "site", "level_to": "site"
        }
    ]
}
</rasaeco-meta>

## Summary

This scenario explores how we can observe the thermal state of the construction site.

## Models

*Intentionally left empty.*

## Definitions

<def name="thermal_spot">

This is a spot for which we would like to record the temperature.

</def>

<def name="thermal_image">

A thermal image is an captured by a 
[thermographical sensor](https://en.wikipedia.org/wiki/Thermography).

The image is stored as a JPEG with the sensor range as additional meta-data in the 
[EXIF](https://en.wikipedia.org/wiki/Exif) (see 
<modelref name="digital_reconstruction#images" />).

</def>

## Scenario

### As-planned

The user defines the <ref name="thermal_spot" /> as a <ref name="uxv_recording#focus_spot" />.

As <ref name="uxv_recording#focus_spot" /> is a <ref name="topic_management#topic" />, special
information about the <ref name="thermal_spot" /> are indicated as 
<ref name="topic_management#comment" />s.

### As-observed

**Capturing**.
The <ref name="uxv_recording#operator" /> takes into account the <ref name="thermal_spot" />s when
planning a <ref name="uxv_recording#mission" />.

Apart from specifying the <ref name="thermal_spot" /> as a 
<ref name="uxv_recording#point_of_interest" />, the <ref name="uxv_recording#operator" /> should
also include thermal cameras in the list of desired <ref name="uxv_recording#sensor" />s. 

We assume that we use a dual camera that records both the <ref name="thermal_image" />s as well
as RGB <ref name="digital_reconstruction#image" />s.

The thermal images are stored in <modelref name="digital_reconstruction#images" /> .

**Inspection**.
We inspect the <ref name="thermal_inspection#thermal_image" />s of the <ref name="thermal_spot" />s:
* Pick a time range,
* Pick a spatial filter (zone, bounding box and other spatial filters, 
  see <scenarioref name="virtual_inspection" />); these spatial filters refer to the location where
  the image was taken and *not* of where the temperature was observed,
* Pick a temperature threshold (above, below *etc.*; the complexity of these threshold queries is
  to be discussed during the implementation).

The relevant <ref name="thermal_inspection#thermal_image" />s are presented in a list of triples:
* <ref name="thermal_image" />,
* the corresponding <ref name="digital_reconstruction#image" />, and
* the location and the view angle where the image has been taken.

(If time permits, we also present an overlay of the <ref name="thermal_image" /> over
a RGB <ref name="digital_reconstruction#image" />.)

The user can jump straight to <scenarioref name="virtual_inspection" /> to inspect the position
and the view angle further.

*The other aspect sections intentionally left empty.*

### Analytics

For the filtered images, we provide summary statistics:
* Number of images above threshold 

## Test Cases

<test name="test_for_magnitude">

We automatically generate dummy RGB and <ref name="thermal_image" />s.

They are randomly spread over the time and space.

We make random queries (spatial and temporal) and test that the retrieval time
is on the order of 10s of seconds.

</test>

## Acceptance Criteria

<acceptance name="magnitude">

The system needs to handle the a lower-digit millions of the <ref name="thermal_image" />s.

</acceptance>
