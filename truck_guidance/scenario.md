<rasaeco-meta>
{
    "title": "Truck guidance",
    "contact": "Dag Fjeld Edvardsen <dag.fjeld.edvardsen@catenda.no>, Marko Ristin <rist@zhaw.ch>",
    "relations": [
        { "target": "on-site_logistics", "nature": "specific" }
    ],
    "volumetric": [
        {
            "aspect_from": "as-planned", "aspect_to": "as-planned",
            "phase_from": "construction", "phase_to": "construction",
            "level_from": "machine/crew", "level_to": "site"
        },
        {
            "aspect_from": "as-observed", "aspect_to": "divergence",
            "phase_from": "construction", "phase_to": "construction",
            "level_from": "machine/crew", "level_to": "machine/crew"
        }
    ]
}
</rasaeco-meta>

## Summary

This scenario concerns truck drivers arriving at the construction site to deliver cargo.

This is a specification of the <scenarioref name="on-site_logistics" /> where the cargo is
delivered by trucks.

## Models

*Intentionally left empty.*

## Definitions

<def name="pickup_person">

The person, an ``IfcPerson``, responsible for picking up the cargo.

</def>

<def name="entry_point">

The `IfcZone` where the truck should enter through.

</def>

<def name="exit_point">

The `IfcZone` where the truck should leave through.

</def>

<def name="truck_delivery">

A truck delivery defines how the <ref name="on-site_logistics#delivery" /> should be brought on
the construction site by the truck.

Each truck delivery is associated with the <ref name="entry_point" /> and <ref name="exit_point" />
so that other entrances and exits do not get congested. 

</def>

<def name="driver">

The driver is a more specific <ref name="on-site_logistics#operator" /> for 
<ref name="truck_delivery" />s.

</def>

## Scenario

### As-planned

<level name="site">The <ref name="on-site_logistics#delivery" />s are specified with additional information
defined as <ref name="truck_delivery" />s.</level>

### As-observed

<level name="machine">

The <ref name="driver"/>'s device tracks the GPS location, but does not send
it to the system.

The location is only used to navigate the driver.

</level>

### Divergence

<level name="machine">The  device will guide the <ref name="driver" /> to the
<ref name="on-site_logistics#delivery_location" />.</level>

<level name="machine">

The <ref name="topic_management#topic" /> body includes a link
(authorized for the whole internet) that the <ref name="driver" /> can click on to update
the current location of the delivery and another link to signal that
the <ref name="on-site_logistics#delivery" /> arrived.

The <ref name="driver" /> can choose to include his/her current GPS location
in the <ref name="on-site_logistics#delivery_update" /> (*e.g.*, when following the link for the arrival).

The updates of the delivery status are kept track in the
<modelref name="on-site_logistics#logs" />.

</level>

## Test Cases

Please see the test cases of <scenarioref name="on-site_logistics" />.

## Acceptance Criteria

Please see the acceptance criteria of <scenarioref name="on-site_logistics" />.
