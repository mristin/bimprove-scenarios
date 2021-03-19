<rasaeco-meta>
{
    "title": "Topic Management",
    "contact": "Dag Fjeld Edvardsen <dag.fjeld.edvardsen@catenda.no>, Marko Ristin <rist@zhaw.ch>",
    "relations": [
        { "target": "uxv_recording", "nature": "focus spots" }
    ],
    "volumetric": [
        {
            "aspect_from": "as-planned", "aspect_to": "analytics",
            "phase_from": "planning", "phase_to": "construction",
            "level_from": "device/person", "level_to": "office"
        }
    ]
}
</rasaeco-meta>

## Summary

This scenario is about providing a communication platform for BIMprove system.

## Models

<model name="topics">

This model lists all the available <ref name="topic" />s, <ref name="topic_board" />s and
<ref name="comment" />s.

</model>

<model name="notification_protocols">

This model comprises all the defined and pre-defined <ref name="notification_protocol" />s.

</model>

## Definitions

<def name="topic">

A topic is an issue, a problem or a communication thread.

It consists of a subject, a description and the <ref name="comment" />s.

A topic is associated with:
* exactly one <ref name="requester" />, 
* zero or one <ref name="assignee" />,
* the creation time stamp, 
* the dead line (as a time stamp), 
* <ref name="stage" /> and
* zero, one or more <ref name="label" />s. 

A topic is accompanied with <ref name="comment" />s.

</def>

<def name="topic_board">

A topic board (called "project" in <ref name="BCF" />) is a collection of <ref name="topic" />s.

A topic board can have different access rights as well as different semantics.

For example, there is a special topic board for <ref name="on-site_logistics#delivery" />s.

</def>

<def name="requester">

The <ref name="actor_management#actor" /> who created/requested a <ref name="topic" /> to be 
focused on.

</def>

<def name="assignee">

The <ref name="actor_management#actor" /> who is responsible for a <ref name="topic" />.

</def>

<def name="stage">

The stage is a phase or a milestone of a <ref name="topic" />.

This is usually a stage in the building life cycle.

For example, "planning", "construction" or more fine-grained like a phase in the
<ref name="scheduling#phase_plan" />. 

</def>

<def name="label">

A label is a free-form category of a <ref name="topic" />.

</def>

<def name="comment">

A comment introduces additional information about a topic.

A <ref name="viewquery" /> can be optionally attached to a comment.

Comments are usually free-form.

There are also specially structured comments.
For example, we use comments to represent the status change of a 
<ref name="on-site_logistics#delivery" />.

</def>

<def name="viewquery">

A viewquery is an encoding of the camera position, the view angle and the query from 
<scenarioref name="virtual_inspection" />.

Note that the viewquery as we refer to here is *not* the <ref name="BCF_viewpoint" /> as
usually exported in a <ref name="BCF" />.
The <ref name="BCF_viewpoint" /> is much sparser than <ref name="viewquery" />.

</def>

<def name="BCF_viewpoint">

This is the viewpoint as exported in a <ref name="BCF" />.

This includes:
* camera position,
* selected objects (from <modelref name="evolving_plan#bim3d" />), and
* visible objects (from <modelref name="evolving_plan#bim3d" />).

</def>

<def name="BCF">

The BCF is a format for structuring <ref name="topic" />s as defined by building Smart:
https://www.buildingsmart.org/standards/bsi-standards/bim-collaboration-format-bcf/

</def>

<def name="notifiee">

The notifiee is an <ref name="actor_management#actor" /> that is notified when there are new 
<ref name="comment" />s on a <ref name="topic" />.

</def>

<def name="notification_protocol">

The notification protocol specifies the <ref name="notifiee" /> as well as the channels used
for the notification.

For example, notify person `A` over `e-mail` with severity `high`.
The protocol can also include an optional trigger (`if late` *etc.*).

The notification protocol is associated with a single delivery.

This is a non-IFC entity and lives in <modelref name="notification_protocols" />.

</def>

## Scenario

We use <scenarioref name="virtual_inspection" />, <scenarioref name="scheduling" />, 
<scenarioref name="truck_guidance" />,
<scenarioref name="risk_management" /> and other scenarios 
as "explorers" (or "browsers").

These "explorers" give us links to the instances and entities as 
<ref name="unique_resource_identification#identifier" />s.

**References**. 
We link the <ref name="unique_resource_identification#identifier" />s through <ref name="topic" />s
to structure the communication.
This includes both the elements from <modelref name="evolving_plan#bim3d" /> and
<modelref name="evolving_plan#bim_extended" /> as well as our BIMprove-specific entities such as
<ref name="risk_management#risk" />.

For example, if there is a problem with a <ref name="uxv_recording#UXV" />, we can reference
it with a  <ref name="unique_resource_identification#identifier" /> in the <ref name="topic" />'s 
subject, description of a <ref name="comment" />.

**Management**.
BIMprove system provides an application for creating and managing the <ref name="topic" />s and
adding the <ref name="comment" />s.

If a comment is attached a <ref name="viewquery" />, the user should be able to follow it through
to <scenarioref name="virtual_inspection" />.

The topic management does not provide the modification of a <ref name="viewquery" />.
If you need to modify a <ref name="viewquery" />, you have to use 
<scenarioref name="virtual_inspection" />. 
For example, you can use an existing <ref name="viewquery" /> as the starting point.

The <ref name="topic" /> is assigned access rights based on individual 
<ref name="actor_management#actor" />s and/or <ref name="actor_management#role" />s.

The <ref name="topic" /> is also optionally assigned a <ref name="notification_protocol" />. 

The management of <modelref name="notification_protocols" /> is part of a separate application and
the <ref name="notification_protocol" />s can be referenced through 
<ref name="unique_resource_identification#identifier" />.

**Topic from a task**.
The user can create a <ref name="topic" /> from an arbitrary <ref name="scheduling#task_shadow" />
using <scenarioref name="scheduling" />.

There is also a more structured task-to-topic translation for specific tasks such as
<ref name="on-site_logistics#delivery" />s.

**Export to <ref name="BCF" />**.
The <ref name="topic" />s are exportable to <ref name="BCF" />.

The export can be either to:
* a BCF file, or
* directly to a [BCF API](https://github.com/buildingSMART/BCF-API).

Special care has to be taken to convert <ref name="viewquery" />s to <ref name="BCF_viewpoint" />s.
For example, the query itself can be left as a string in the comment though it can not be
included as-is in the <ref name="BCF_viewpoint" />.
Additionally, the elements selected by the <ref name="viewquery" /> need to be converted to an 
explicit list in the <ref name="BCF_viewpoint" />.

**Ingress of <ref name="comment" />s**.
If time permits, a nice-to-have: when a <ref name="notifiee" /> is notified,
the <ref name="notifiee" /> can respond to a notification and the reply should be imported
directly as a <ref name="comment" />.

This is easy for e-mails (*e.g.* by including special fields in the e-mail header referencing the
<ref name="topic" />), and a bit more involving for SMS and other channels.

**An example workflow with a <ref name="viewquery" />**.
An example workflow for creating a <ref name="topic" /> involves:
1) Create the <ref name="topic" />, write the subject and the description.

   The subject and the description can include arbitrary references as
   <ref name="unique_resource_identification#identifier" />s.
2) Go to <scenarioref name="virtual_inspection" /> and select the relevant elements.

   Use <scenarioref name="virtual_inspection" /> to create a <ref name="viewquery" /> and
   attach it automatically to the <ref name="topic" />.

*The aspect sections intentionally left empty.*

## Test Cases

<test name="property-based_test">

We automatically generate <ref name="topic" />s and assign them to 
<ref name="actor_management#actor" />s randomly.

We also randomly generate <ref name="comment" />s.
Some of the generated <ref name="comment" />s have <ref name="viewquery" />s attached.

The generated data should be of expected <acceptanceref name="magnitude" />. 

The generated data is frozen prior to ingress (*e.g.*, before the API calls), so that we can
reproduce the test.

We test that we can:
* list the <ref name="scheduling#task" />s,
* list the <ref name="comment" />s,
* view the <ref name="viewquery" />s *etc.*

</test>

## Acceptance Criteria

<acceptance name="magnitude">

We need to handle thousands of <ref name="topic" />s and hundreds of 
<ref name="comment" />s per <ref name="topic" />. 

</acceptance>
