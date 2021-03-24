<rasaeco-meta>
{
    "title": "Logistics",
    "contact": "Dag Fjeld Edvardsen <dag.fjeld.edvardsen@catenda.no>, Marko Ristin <rist@zhaw.ch>",
    "relations": [
        { "target": "topic_management", "nature": "deliveries" }
    ],
    "volumetric": [
        {
            "aspect_from": "as-planned", "aspect_to": "scheduling",
            "phase_from": "construction", "phase_to": "construction",
            "level_from": "machine/crew", "level_to": "office"
        },
        {
            "aspect_from": "safety", "aspect_to": "analytics",
            "phase_from": "construction", "phase_to": "construction",
            "level_from": "machine/crew", "level_to": "office"
        }
    ]
}
</rasaeco-meta>

## Summary

This scenario looks into how the cargo is transported to, from and within a construction site.

## Models

<model name="logs">

These are the <ref name="topic_management#topic" />s corresponding to the
<ref name="delivery" />s.

The <ref name="delivery_update" />s are converted to structured
<ref name="topic_management#comment" />s.

The <ref name="topic_management#comment" />s are appended to the
<ref name="topic_management#topic" /> corresponding to a <ref name="delivery" />.

</model>

<model name="status_labels">

The list of possible labels for a delivery status.

</model>

## Definitions

<def name="planner_role">

Planner <ref name="actor_management#role" /> is for all people who are allowed to change a
<ref name="delivery"/>.

</def>

<def name="delivery_location" >

The delivery location is the `IfcZone` where the cargo should be delivered.

</def>

<def name="delivery">

Delivery is a <ref name="topic_management#topic" /> which has a description, a `Deadline` and a
 `Priority`.

The delivery can be associated optionally with a <ref name="delivery_location" />.

The cargo is described as a text property of the delivery ("10 windows, 2 doors").

The delivery is assigned to an <ref name="operator"/> and associated with:
* a <ref name="delivery_location" />,
* a <ref name="contact_person" />, and
* a <ref name="scheduling#task" /> (if available).

The <ref name="topic_management#topic" /> follows a pre-defined format.

The deliveries live in a semantically pre-defined <ref name="topic_management#topic_board" />.

</def>

<def name="contact_person">

The <ref name="actor_management#actor" /> who should be contacted if the <ref name="operator" /> 
have questions.

</def>

<def name="operator">

The operator is an <ref name="actor_management#actor" /> who executes the <ref name="delivery" />.

Depending on the vehicle, this can be a truck driver or a crane operator *etc.*

</def>

<def name="delivery_update">

A structured <ref name="topic_management#comment" /> representing the update of the delivery status:
* label (as an enum string, referring to <modelref name="status_labels" />),
* datetime, and
* an optional field `location` (as a GPS location).

The delivery updates live in <modelref name="logs" />.

The system should not allow the user to change the corresponding comment in
the <ref name="topic_management#topic" />.

</def>

## Scenario

The labels for a <ref name="delivery_update" /> are pre-defined during the system configuration
in <modelref name="status_labels" />.

### As-planned

The tasks are imported from external <<ref name="scheduling#last_planner_system" /> such as Visilean
(see <scenarioref name="scheduling" />).

Since it is too difficult to enrich the task information with the delivery-relevant information
(such as selecting the <ref name="operator" /> and the <ref name="delivery_location" />), 
we have to provide an application that allows the user to add this extra information.

The <ref name="planner_role"/> converts the corresponding task into a <ref name="delivery"/>
(a structured <ref name="topic_management#topic" />) and enriches it with the extra information.

The <ref name="planner_role"/> can also update manually the status of the delivery (*e.g.*, to
cancel it) by adding <ref name="delivery_update" />s (as structured
<ref name="topic_management#comment" />).

The updates of the delivery status are kept track in the <modelref name="logs" />.

### Analytics

<level name="site">

The KPI for delivery-in-time is updated, both delivery in number per week and variance.

The KPIs are based on the data from the <modelref name="logs" />.

Since <ref name="delivery" /> is a <ref name="topic_management#topic" />, many messages are
structured as <ref name="delivery_update" />. However, unstructured messages are also possible.
The unstructured messages should be ignored when computing the KPIs.

The <ref name="planner_role" /> usually sets the last status of the delivery which is then used
to determine how the <ref name="delivery" /> is counted in the KPIs (*e.g.*, "on time", "delayed"
*etc.*).

</level>

### Scheduling

The notifications regarding the unmet deadlines are handled by the
<scenarioref name="topic_management" />.


## Test Cases

<test name="navigation_correct_on_examples">

To be discussed. What is the easiest way to record a couple of scenarios so that we can
repeatedly and automatically test them?

</test>

## Acceptance Criteria

To be discussed. 
What are the practically accepted refresh rates for the navigation?
How much polling will be involved -- how many requests per second will the system face
in low, normal and high usage?

What is the acceptable delay with sending out the messages? Can this be a bottleneck? How many
messages per second in low, normal and high usage?
