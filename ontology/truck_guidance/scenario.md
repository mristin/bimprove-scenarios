<rasaeco-meta>
{
    "identifier": "truck_guidance",
    "title": "Truck guidance",
    "relations": [
    ],
    "volumetric": [
        {
            "aspect_from": "as-planned", "aspect_to": "scheduling",
            "phase_from": "construction", "phase_to": "construction",
            "level_from": "zone", "level_to": "office"
        }
    ]
}
</rasaeco-meta>

## Summary

This scenario concerns truck drivers arriving at the construction site to deliver cargo.

## Models

### plan/main

The as-planned BIM model provided after the planning phase and
updated throughout the construction.

It is going to be updated as the building grows.

This is the federated model of all the individual domain models (core is Site model,
Structural model and Electrical model).

### observed/main
This model contains the real time delivery status.

### archived/observations
This keeps track of accomplished <ref name="delivery" />s.

## Definitions

### planner_role
planner_role is for all people who are allowed to change a <ref name="delivery"/>.

### delivery
Delivery is an `IfcTask`, which has a text, a `ScheduleStart` and `ScheduleFinish` (both `IfcTaskTime`. It can be associated with
a location `IfcZone`. The cargo is a text property of the delivery ("10 windows, 2 doors").

The delivery is assigned to a <ref name="driver"/>, a <ref name="entry_point" /> and
<ref name="exit_point" /> and a <ref name="contact_person" />.

### contact_person
The person who should be contacted if the <ref name="driver" /> have questions.

### pickup_person
The person responsible for picking up the cargo.



### entry_point
The `IfcZone` where the truck should enter through.


### exit_point
The `IfcZone` where the truck should leave through.

### driver
The driver is an `IfcActor`.

### delivery_status
Consideration for architecture: we need to introduce a custom class to represent the
delivery status (label and depending on the label, last_location and last_observed_time).

### notifiee
The notifiee is an `IfcActor` that is notified when the delivery status is updated.


## Scenario

### As-planned
The <ref name="planner_role"/> creates and updates the <ref name="delivery"/>s.

### As-observed
The <ref name="driver"/>'s device tracks the gps location, but does not send it to the system.

### Divergence
The  device will guide the <ref name="driver" /> to the location on the site where the
<ref name="delivery" /> should take place. The <ref name="driver" /> updates the status of
the delivery.

The <ref name="notifiee" />s are notified when the status of the delivery is updated.

### Analytics
The KPI for delivery-in-time is updated, both delivery in number per week and variance. This is based
on date from <modelref name="archived/observations" />.

The <ref name="planner_role" /> decides under which status to archive the delivery (for KPI).

### Scheduling
Notify the <ref name="notifiee" />s if the <ref name="delivery" /> is not ready when the pickup-time
has passed.

### Safety
Intentionally left empty.
