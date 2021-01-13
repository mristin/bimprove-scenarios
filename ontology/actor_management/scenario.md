<rasaeco-meta>
{
    "title": "Actor Management",
    "contact": "Dag Fjeld Edvardsen <dag.fjeld.edvardsen@catenda.no>, Marko Ristin <rist@zhaw.ch>",
    "relations": [
        { "target": "evolving_plan", "nature": "actors" }
    ],
    "volumetric": [
        {
            "aspect_from": "as-planned", "aspect_to": "as-planned",
            "phase_from": "planning", "phase_to": "construction",
            "level_from": "site", "level_to": "office"
        }
    ]
}
</rasaeco-meta>

## Summary

This scenarios covers how the actors are managed in the system, their <ref name="role" />s and 
their relationships to other entities.

## Models

*Intentionally left empty.*

## Definitions

<def name="actor">

Actors are entities corresponding to people and organizations (legal, non-legal, imagined *etc.*).

The granularity of an actor is variable:
* a single person,
* a team of persons,
* an informal organization (such as a GitHub organization),
* a legal (formal) organization *etc.*

Some common actors include:
* Workers,
* Engineers,
* Installers,
* Manufacturers *etc.*

The actors are represented using corresponding IFC entities such as:
* `IfcActor`,
* `IfcPerson`,
* `IfcOrganization` *etc.*

The contact information about the actor is modeled as `IfcTelecomAddress` in `Addresses` property.

</def>

<def name="relationship">

An actor can be linked to many other entities in <modelref name="evolving_plan#bim3d" /> and
<modelref name="evolving_plan#bim_extended" />.

The relationships are modeled by using corresponding IFC entities such as:
* `IfcRelAssignsToActor`,
* `IfcRelAssignsToProduct`,
* `IfcOrganizationRelationship`
* ... and many others.

</def>

<def name="role">

The role of an <ref name="actor" /> in an arbitrary context, not necessarily information security 
context.

</def>

## Scenario

### As-planned

The <ref name="actor" />s and their <ref name="relationship" />s 
(as well as relationships between the <ref name="actor" />s to other entities) are captured in 
<modelref name="evolving_plan#bim_extended" />.

The system provides an application that allows the user to manage the <ref name="actor" />s and
their <ref name="relationship" />s.

This application should allow creating and viewing *arbitrary* relationships and actor 
<name ref="role" />s.

In contrast, more specific applications, such as those implemented for 
<scenarioref name="risk_management" /> and <scenarioref name="truck_guidance" />, should allow 
creating and viewing of the relationships in the manner more appropriate for the context of the 
application.

Additionally, this application is *not* a replacement for a much more low-level tool like
<ref name="evolving_plan#explorer" />.

(Note for implementation. For example, we can use Express or XSD to generate the code and the 
relevant part of user interface automatically. See 
[this buildingsmart table](https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/) 
.)

(Note about the relationships: We need to decide how we structure them. We might allow free-form
relationships, but they should not conflict with our internal relationships such as 
<ref name="risk_management#assignment" />. This is something that needs to evolve during the 
implementation and iterations of the system.)

(Note about the <ref name="role" />s: there are special pre-defined <ref name="role" />s, such as 
<ref name="risk_management#preventive_resource" />, that have consequences in terms of information 
security.

How we handle this pre-defined set of these <ref name="role" />s with special semantic is left out as an 
*important* implementation detail. We could not decide right now, 2021-01-15, how it should be
 handled.
 
For example, there might be a separate application, "role management", where you can add new 
<ref name="role" />s, but a certain set of pre-defined <ref name="role" />s can not be 
changed/removed. 
Additionally, the user should be warned if she creates a <ref name="role" /> with a similar name 
to the existing one (*e.g.*, with or without underscore).

The system might provide a set of common, frequently-used <ref name="role" />s at instantiation 
time of the system. These common <ref name="role" />s, however, *can* be modified/removed.

Check also [DICO agents](https://digitalconstruction.github.io/Agents/#overv) for an example of 
pre-defined <ref name="role" />s and relationships, capabilities *etc.* 
Perhaps we can map the interesting bits to IFC classes and use them to initialize the system.

Additionally, we can introduce these entities in <modelref name="evolving_plan#bim_extended" /> as
IFC "shadows" where we lock them and do not allow a user to modify them, similar how we plan to
deal with <ref name="role" />s conveying special semantic.)

**Actor list import**.
The system should provide an import of the complete list of <ref name="actor" />s from external
sources. (For example, an excel table or from Visilean.)  

This import is not a complete overwrite, but an extension to the existing <ref name="actor" />s.

The mapping of <ref name="actor" /> identifiers to the existing identifiers is the responsibility 
of the individual import tool.

*The remaining aspect sections intentionally left empty.*

## Test Cases

<test name="blank_state">

We test that the actor management works on empty data.

We install the system and do not populate anything.

</test>

<test name="recorded_state">

We record the data of a toy project.

We freeze the data.

We pre-define a set of actions (such as insert a new <ref name="actor" />, 
create a new <ref name="role" />, assign an <ref name="actor" /> to a <ref name="role" /> or 
to an organization *etc.*).

We record the effects, so that we can repeatedly test the behavior of the system in automatic way. 

</test>

<test name="big_data">

We generate automatically the data of a toy project to test that the system can handle the 
<acceptanceref name="magintude" />.

We only check if nothing crashes and perform a set of pre-defined actions.

(Implementation note: use a tool for property-based testing to generate data such as 
[https://en.wikipedia.org/wiki/QuickCheck](QuickCheck)) 

</test>

## Acceptance Criteria

<acceptance name="magintude">

We expect the system to handle the number of <ref name="actor" />s in the order of thousands 
(not millions).

We also expect the number of relationships to be in the order of tens of thousands 
(not in millions).

</acceptance>
