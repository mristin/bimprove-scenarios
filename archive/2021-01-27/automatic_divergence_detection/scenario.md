<rasaeco-meta>
{
    "title": "Divergence Detection TODO",
    "contact": "Dag, Gabor, Marko, Ruprecht TODO",
    "relations": [
    ],
    "volumetric": []
}
</rasaeco-meta>

Divergence: as-built vs as-planned, 3D

You have 2 BIM models, <modelref name="evolving_plan#bim3d" /> and 
<modelref name="digital_reconstruction#as-built" />.

We want to detect mistakes/errors.

you never have the equivalence (floating point numbers).

This is about the *automatic* divergence detection.

Spatial tolerances. --> Only geometry.

We need to define the *tolerance* in the *context*.

In different phases and difference disciplines, we have different *tolerances*.

The <modelref name="evolving_plan#bim3d" /> is already a federation of the domain-specific
models.

Plan vs as-built

We define tolerance per element.

The system checks the tolerances.

There are standards for tolerances.

1.0000000000m

0.9m

We can have a default tolerance (*e.g.*, 2cm).
We can have per-element tolerances overriding the default tolerance.


Example: an inclined wall



## Summary

First priority: just use manual inspection

If time permits, nice-to-have: automatic divergence detection.
We will have a rule based system, but not details yet.



## Models


## Definitions


## Scenario

### As-planned


### As-observed


### Divergence


### Analytics


### Scheduling


### Safety


## Test Cases


## Acceptance Criteria
