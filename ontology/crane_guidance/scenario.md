<rasaeco-meta>
{
    "title": "Crane guidance",
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
        },
        {
            "aspect_from": "scheduling", "aspect_to": "scheduling",
            "phase_from": "construction", "phase_to": "construction",
            "level_from": "device/person", "level_to": "site"
        },
        {
            "aspect_from": "safety", "aspect_to": "safety",
            "phase_from": "construction", "phase_to": "construction",
            "level_from": "site", "level_to": "site"
        },
        {
            "aspect_from": "analytics", "aspect_to": "analytics",
            "phase_from": "construction", "phase_to": "construction",
            "level_from": "machine/crew", "level_to": "machine/crew"
        }
    ]
}
</rasaeco-meta>

## Summary

This scenario examines how crane operators can lift and deliver the cargo around the construction 
site.

## Models

<model name="crane_log">

This log contains the observed <ref name="crane_state" />s corresponding to the
<ref name="crane" />s.
 
</model>

<model name="cranes">

This model lists all the <ref name="crane" />s available in the system.

</model>

## Definitions

<def name="pickup_location">

This is an `IfcZone` where the <ref name="on-site_logistics#delivery" /> needs to be picked up.

</def>

<def name="attaching_slinger">

The <ref name="actor_management#actor" /> who will attach 
the <ref name="on-site_logistics#delivery" /> to the crane at the <ref name="pickup_location" />. 

</def>

<def name="detaching_slinger">

The <ref name="actor_management#actor" /> who will take off 
the <ref name="on-site_logistics#delivery" /> from the crane at 
the <ref name="on-site_logistics#delivery_location" />. 

A detaching slinger can be identical with a <ref name="attaching_slinger" />.

</def>

<def name="crane_delivery">

A crane delivery defines how the <ref name="on-site_logistics#delivery" /> should be transported
within the construction site by a <ref name="crane" />.

Each crane delivery is associated with:
* a <ref name="pickup_location" /> and 
  the corresponding one or more <ref name="attaching_slinger" />s,
* the <ref name="on-site_logistics#delivery_location" /> and 
  the corresponding one or more <ref name="detaching_slinger" />s, and
* the <ref name="crane" />,
* the <ref name="crane_supervisor" />, and 
* the <ref name="crane_operator" />

</def>

<def name="crane_operator">

The crane operator is an <ref name="on-site_logistics#operator" /> who controls the <ref name="crane" />.

</def>

<def name="crane_supervisor">

Crane supervisor is an <ref name="actor_management#actor" /> 
who helps the <ref name="crane_operator" /> by guiding her during 
the <ref name="on-site_logistics#delivery" />.

She has the final authority.

</def>

<def name="crane_coordinator">

The crane coordinator is an <ref name="actor_management#actor" /> who supervises that
the <ref name="crane_operator" />s do not crash into each other.

</def>

<def name="crane">

The crane is defined as `IfcTransportElement` and stored in <modelref name="cranes" />.

Its state is tracked as <ref name="crane_state" /> and stored in <modelref name="crane_log" />. 

</def>

<def name="crane_state">

The crane state captures the state of the crane, including:
* a timestamp of the observation,
* position of the trolley, and
* the height of the hook block (if available).

</def>

## Scenario

### As-planned

<level name="site">The <ref name="on-site_logistics#planner_role" /> specifies the 
<ref name="on-site_logistics#delivery" />s (with additional information
defined) as <ref name="crane_delivery" />s.</level>

### As-observed

<level name="machine">The position of the crane's arm is continuously tracked 
as <ref name="crane_state" /> in <modelref name="crane_log" />.</level>

### Divergence

<level name="machine">

The  device will guide the <ref name="crane_operator" /> and the 
<ref name="crane_supervisor" /> to the <ref name="on-site_logistics#delivery_location" />.

Since the <ref name="crane_delivery" /> is very dynamic, we explicitly do not provide a mechanism
to signal the <ref name="attaching_slinger" />s and <ref name="detaching_slinger" />s when the
<ref name="crane_delivery" /> arrived, as these actors would have a visual contact anyhow.

</level>

### Scheduling

<level name="site">

For a given time range, the <ref name="on-site_logistics#planner_role" /> should be able to inspect
the plan of the <ref name="crane_delivery" />s as association between the <ref name="crane" />s,
<ref name="crane_operator" />s, <ref name="crane_supervisor" />s and 
<ref name="scheduling#task" />s (if available). 

</level>

### Safety

<level name="site">

The <ref name="crane_coordinator" /> ensures visually that the <ref name="crane_operator" />s do not crash.

In addition, the system should warn the <ref name="crane_coordinator" /> if two crane arms are about
to collide.

</level>

### Analytics

<level name="machine">

As we track the crane movements in <modelref name="crane_log" />, the system should report the
<ref name="crane" /> utilisation over time.

The details are to be discussed during the implementation (*e.g.*, what time units and how we
can measure it).

</level>


## Test Cases

Please see the test cases of <scenarioref name="on-site_logistics" />.

## Acceptance Criteria

Please see the acceptance criteria of <scenarioref name="on-site_logistics" />.
