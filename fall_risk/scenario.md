<rasaeco-meta>
{
    "title": "Fall Risk Alert",
    "contact": "Dag Fjeld Edvardsen <dag.fjeld.edvardsen@catenda.no>, Miquel Cantero <mcantero@robotnik.es>, Manuel Menendez <manuel.menendez@vias.es>, Marko Ristin <rist@zhaw.ch>",
    "relations": [
    ],
    "volumetric": [
        {
            "aspect_from": "as-planned", "aspect_to": "divergence",
            "phase_from": "construction", "phase_to": "construction",
            "level_from": "zone", "level_to": "office"
        },
        {
            "aspect_from": "cost", "aspect_to": "analytics",
            "phase_from": "construction", "phase_to": "construction",
            "level_from": "zone", "level_to": "office"
        }
    ]
}
</rasaeco-meta>

## Summary

<img src='summary.png' alt="summary of the scenario" width="400" height="200" />

## Models

<model name="plan/main">

The as-planned BIM model provided after the planning phase and
updated throughout the construction.

It is going to be updated as the building grows.

This is the federated model of all the individual domain models.

</model>

<model name="observed/point_cloud">

The point cloud observed with the drones and the ground robots.

The coordinates are synchronized with the <modelref name="plan/main" />.

</model>

<model name="observed/pictures">

The pictures taken by the ground robots, drones and humans.

The coordinates are synchronized with the <modelref name="plan/main" />.
TODO: how is this synchronization done -- address it in as-observed aspect.

</model>

<model name="observed/qr_codes">

The observations of the QR codes: (the location, the time, the identifier of the 
<ref name="element"/>).

</model>

<model name="standard/risk_level">

Risk levels defined at the national and internation level.

</model>

## Definitions

<def name="installer">

The person who installed an <ref name="element"/>.

Uniquely identifiable by a contact (unstructured, can be e-mail, but also something completely 
arbitrarily such as a phone number or a company name).

In BIM:

```
IfcActor
```

</def>

<def name="alertee">

A person who needs to be alerted on his/her current risk level. 

</def>

<def name="element">

Any relevant building element from the <modelref name="plan/main"/>. 
It can be associated with <modelref name="observed/point_cloud" /> and 
<modelref name="observed/pictures" />.

In BIM:

```
IfcProduct
```

Every element needs to have a unique identifier. 

</def>

<def name="points_in_the_vicinity">

A subset of the points in the point cloud close to <ref name="element" />.

The vicinity is defined as a bounding box.

</def>

<def name="images_of_the_element">

A subset of the images that look at the <ref name="element" />.

We can compute their subset based on their coordinates and angle.

</def>

<def name="task">

Any `IfcTask` in the <modelref name="plan/main"/>

</def>

<def name="zone">

Any `IfcZone` in the <modelref name="plan/main"/>

</def>

<def name="preventive_resource">

Preventive resource is person who is in charge of the safety inside.

The preventive resource is in charge of a set of <ref name="task"/>.

Depending on the budget, there will be preventive resources in charge of 
one or more <ref name="zone" />s or <level name="site">the whole site</level>.

</def>

<def name="health_and_safety_manager">

<level name="site">Health & safety manager is in charge of the issues on the site.
The person is the boss of the health & safety of the site.</level>

</def>

<def name="risk_level">

This is the risk level according to different standards.
Refers to a concrete standard in <modelref name="standard/risk_level" />.

</def>

<def name="fall_risk">

A fall risk is an abstract entity.

It can be tied to a <ref name="zone"/> or to an <ref name="element"/>, but it doesn't need to.

The fall risk has a validity time span (which can also be open-ended).

The fall risk lives in <modelref name="plan/main" />.

</def>

## Scenario

### As-planned

We just use the federated model in <modelref name="plan/main" />.

<level name="site_office">The <modelref name="plan/main" /> data would need to be accessible from 
the office.</level>

### As-observed

All the observed data from <modelref name="observed/point_cloud" /> and
<modelref name="observed/pictures" /> lives in the same coordinate system as 
the federated model in <modelref name="plan/main" />. The mismatch errors between the coordinates
are possible (see the acceptance criterion <acceptanceref name="coordinate_error" />).

<level name="site_office">The observed data, <modelref name="observed/point_cloud" /> and
<modelref name="observed/pictures" />,  would need to be accessible from the office.</level>

### Divergence

**Start simple.** The <ref name="preventive_resource"/> and <ref name="health_and_safety_manager" />
manually inspect the <ref name="element"/>s and report absent/ill-placed to the system.

**Next step: QR code.** The QR code references the identifier of the <ref name="element"/>.
The observations of the QR code are stored in <modelref name="observed/qr_codes"/>.

Anybody authorized can add an observation of a QR code.

### Analytics

The overall view of the <ref name="fall_risk"/>s should be provided in a table.

The user can manually inspect further the related details such as associated <ref name="element"/>s.

### Scheduling

*This section is empty on purpose.*

### Safety

**Specification of the fall risks**.
The <ref name="preventive_resource"/> links the <ref name="element"/> with the 
<ref name="installer"/>.

<phase name="planning">The <ref name="health_and_safety_manager"/> inputs initially the 
<ref name="fall_risk"/>s manually.</phase>

The <ref name="preventive_resource"/> makes notes regarding an unsafe <ref name="element" />.
Both the <ref name="health_and_safety_manager"/> and <ref name="preventive_resource"/> can
insert new and change existing <ref name="fall_risk"/>s accordingly.

**Alerts**. The safety status <ref name="risk_level" /> is continuously displayed to 
<ref name="alertee"/>s in real-time based on the current <ref name="fall_risk"/>s and their 
location. 

The location of the actor is not stored in the backend. The update logic is running on the alertee's
device (*i.e*., a smart-watch) which sends repeated queries to the backend. 
The backend does not track the alertee.

## Test Cases

<test name="safely_test_proximity_to_danger">

We mount an user device on a long stick and come closer and closer to the danger zone.
We observe the distance to the danger zone and verify that the alarm is triggered on an appropriate
proximity (judged by the <ref name="health_and_safety_manager"/>).

The system states as well as the device data are recorded and re-used for repeated automatic 
testing. 

</test>

<test name="blind_test_removed_item">

Remove a safety item and inform the workers. Check that the responsible person could find out
that it is missing using the system. 

</test> 

<test name="analytics_correct_on_an_example">

Record 3 complete states of the whole system and freeze them. Manually compute the expected
analytics. Check that the output of the system coincides with the manually computed analytics.

</test>

## Acceptance Criteria

<acceptance name="coordinate_error">

Over repeated runs (*e.g.,* over the days), there will be randomized errors between the
coordinates in <modelref name="plan/main" /> and
<modelref name="observed/point_cloud" /> and
<modelref name="observed/pictures" />, including the drift and systematic errors. 

We have to see *after* the experiments whether these errors are tolerable for this
scenario.

Our expectation is that the error is below 1 meter, rarely 2 meters. 
We do not have precise statistics at the moment (2021-01-09).

</acceptance>

TODO: how fast should the safety status change?
TODO: how many queries per second will the system actually need to handle (3 scenarios: small construction site, medium construction side, large construction site)
TODO: --> polling can be expensive. 