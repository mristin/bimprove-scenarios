<rasaeco-meta>
{
    "title": "Cost Tracking TODO",
    "contact": "TODO",
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

## TODO

Rewrite the scenario to make it more general.

Add contact.

For example, one salient point is the "IFC File" (in the summary), where I would have preferred that the scenario talks about the model "plan/main". Whether this model is stored as a file or not is in my opinion not relevant (it can be exported to a file if needed, but the "fileness" is not essential for this scenario).

I also have some questions about the "observed/main" model. For example, isn't the cost data actually part of the "plan/main"? Or the "plan/main" contains the estimates, while the observed model contains the actual costs? Shouldn't we archive the costs and forget about the "observed/main" as the latest costs can be always derived from "archived/observations"?

As far as I can tell, it's about a general IfcElement, not a particular IfcColumn?

## Summary
((NB: To be specific, we use a column in this example - but it can be almost any
building element and task conceptually.))

The Costing column scenario is about calculating the cost of an IfcColumn. 
Materials can be prefab concrete, steel (maybe length would need to be cut), possibly on-site fabrication, mass-timber, 
laminated timber.  The materials are available in the BIM-model, and this is stored in the 
IFC-file (In line with the standardized schema) together with its properties / quantities. An estimate in the tendering phase, the more 
detailed budget for the project contains info. Could be changes to the solution, for instance
from in-situ (onsite) to prefab columns. In the end the actual costs for each element (cost and
hours) will be captured. The costs would be known (?) at the subcontract-level where one
single column. Important to be certain that the cost estimate for the column is at the accepted
certainty level - for instance 90% or 95%. 

We can assume that you will know the cost for each element at the end.

Total cost for a column will include: Purchase of column or materials+production costs. 
Installation of the column, fire protection, insolation, added materials, covering, finish,
paint. In-situ: rebaring, creating the form, pouring concrete, hardening, Removing the forms,
finish. 

If there are changes, this would then involve the main contractor, the sub-contractor and 
the client. Changes could be based on unforseen curcomstances or by not having taking
everything into consideration from the start.

Interfaces: Main contractor talks with client, and talks with subcontractors. Sometimes
the client hires an expert company to do the day-to-day communication with the 
construction company - only major things are handled by the client themselves.

All of these interactions are regulated by a contract.

For every unit, the site manager (supported by the production manager) has a cost objective. Asks for different offers, but knows what
it typically should cost, but choose the best. Often balance between cost and quality.
Check the cost objective at least every month.

## Models

<model name="plan/main">

The as-planned BIM model provided after the planning phase and
updated throughout the construction.

It is going to be updated as the building grows.

This is the federated model of all the individual domain models (core is Site model, 
Structural model and Electrical model).

</model>

<model name="observed/main">

This model contains the actual cost status, captured in real time.
(NB: It is not given that this will be stored in an actual IFC model, but conceptually
it could be done like this)

</model>

<model name="archived/observations">

This model keeps track of actual <ref name="cost" />s having taken place.

</model>

## Definitions

<def name="cost_estimator">

This role does the cost estimating.

TODO: is it one person or multiple?

</def>

<def name="cost">

TODO: needs to be defined

</def>

<def name="notifiee">

TODO: needs to be defined

</def>

<def name="actual_cost">

TODO: needs to be defined

</def>

<def name="cost_estimate">

TODO: needs to be defined

</def>

<def name="tolerance">

TODO: needs to be defined

TODO: One for all costs? Or defined per cost? As a percentage? --> Alert: scope creep! 

</def>

## Scenario

### As-planned
The <ref name="cost_estimator"/> creates and updates the <ref name="cost_estimate"/>s.

### As-observed
The <ref name="cost_estimator"/>s data captures the actual costs based on agreements
and invoices.

### Divergence
The BIMprove system will keep track of estimated cost of a column, and will notify the Site manager
if the updated expected cost is significantly different. Then the site manager can consider
and action based on this (ask for more prices, or if very big difference consider redesign ... but this 
is very seldom). The steel cost can change a lot, and that can make a big impact on prices.
Also subcontractors often change prices once a year, and that can also influence costs a lot.

Some subcontractors gets paid based on how much they have produced 
in a time interval, for instance digging a hole for the building .. they then can get
paid for the number of m3 that is dug out in that interval. Other times the subcontractors
are paid per hour, but most of the time (80%) the pay is per delivered quantity (m2, m3 etc).

The quicker a cost-deviation is detected, the easier it will be to adjust based on that.

### Analytics
A good KPI can be if the actual costs is in line with the estimated costs. The KPI for 
cost-deviations is updated, both cost-deviation per week and variance. This is based
on date from <modelref name="archived/observations" />.

### Scheduling
Notify the <ref name="notifiee" />s if the <ref name="actual_cost" /> is not within
the <ref name="cost_estimate" /> +- <ref name="tolerance" /> when this is known.


### Safety
Intentionally left empty.


## External references
IFCcolumn: https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/FINAL/HTML/ifcsharedbldgelements/lexical/ifccolumn.htm