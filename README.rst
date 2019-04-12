consistency_analysis - Consistency Analysis is a Python 3
=========================================================


What is consistency_analysis?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Consistency Analysis is a Python 3 package tha implemnts
constraint-based modeling methods to perform gap analysis 
in genome-scale metabolic models of any organism.

The the package was developed on the top of cobrapy: 

- https://github.com/opencobra/cobrapy/

and implement the unconnected modules approach proposed in [1]. 
The package includes a single module (unconnected_modules.py) 
were the class UmFinder is implemented. 

The UmFinder allows to identify:
- blocked reactions
- gap metabolites 
- the set of unconnected modules 

as defined in [1].

[1] Ponce-de-Leon, M., Montero, F., Peretó (2013). Solving gap metabolites and blocked
        reactions in genome-scale models: application to the metabolic network of Blattabacterium cuenoti.
        BMC Systems Biology, 7(1), 114. http://doi.org/10.1186/1752-0509-7-11


License
-------

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License or the Lesser GNU
General Public License as published by the Free Software Foundation,
either version 2 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
Public License for more details.
