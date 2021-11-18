# Constants<sup>[1](#myfootnote1)</sup>

This subdirectory mostly contains several files named after US states.

It also contains a US state/abbreviations constant, that I found [here](https://gist.github.com/rogerallen/1583593), as well as a city/towns constant that makes references each file named after a US-state.

## Adding Files

Use cases for adding files to this directory include:

- Adding new states.

To **ADD** a new file to this directory so that the file is referenced properly in the rest of the code, please do the following:

1.  Name the file after the US state you wish to add, e.g., `michigan.py`.
2.  Open the newly-created file and create a list<sup>[2](#myfootnote2)</sup>. The list should be named **stateNameHere_MetroAreaHere**, like so:

        ```python
        MICHIGAN_DETROIT = [
            ...
        ]
        ```

3.  Add in as many cities/towns as you'd like to the list that you determine to be within the metropolitan area<sup>[3](#myfootnote3)</sup>. Each city/town should be a string, like so:

        ```python
        MICHIGAN_DETROIT = [
            "Ann Arbor",
            "Livonia",
            "Royal Oak",
            "Monroe",
            "Adrian",
            "Flint",
            ...
        ]
        ```

4.  If you wish to add multiple metropolitan areas to your newly-created state file, just create another list like so:

        ```python
        MICHIGAN_DETROIT = [
            "Ann Arbor",
            "Livonia",
            "Royal Oak",
            "Monroe",
            "Adrian",
            "Flint",
            ...
        ]

        MICHIGAN_KALAMAZOO = [
            "Kalamazoo",
            "Battle Creek",
            "Portage",
            "Albion",
            "Comstock Charter Township",
            ...
        ]
        ```

5.  Once you're satisfied, save the file you created.
6.  Next, open the `areas_and_cities.py` file (found in this directory).
7.  Add in the necessary `import` statement to the top of the `areas_and_cities.py` file so that it knows to reference your state file, like so:

        ```PYTHON
        from constants.illinois import *
        from constants.kentucky import *
        from constants.michigan import * # this is similar to what you would add
        from constants.minnesota import *
        from constants.missouri import *
        ```

8.  Then add in the relevant `keys` and `values` to the `AREAS_AND_CITIES` constant, like so:

        ```python
        AREAS_AND_CITIES = {
            "Springfield, KY": KENTUCKY_SPRINGFIELD,
            "Detroit, MI": MICHIGAN_DETROIT, # you would just add one key/value pair if you added one list
            "Kalamazoo, MI": MICHIGAN_KALAMAZOO, # multiple key/value pairs mean you created multiple lists
            "Minneapolis, MN": MINNESOTA_MINNEAPOLIS,
            "Kansas City, MO": MISSOURI_KANSAS_CITY,
            "Charlotte, NC": NORTH_CAROLINA_CHARLOTTE,
        ```

9.  Save your work.
10. That's it -- thank you! Open a pull request if you feel so inclined and I'll take a look.

## Editing Files

Use cases for editing existing files in this directory include:

- Adding a new geographic area to an existing state.
- Adding more cities to an existing geographic area within an existing state.

To **EDIT** an existing file in this directory so that the file is referenced properly in the rest of the code, please do the following:

1.  Open the file you wish to edit, e.g., `north_carolina.py`
2.  If you wish to add a new geographic area within the state named after the file, create a list<sup>[2](#myfootnote2)</sup>. The list should be named **stateNameHere_MetroAreaHere**, like so:

        ```python
        NORTH_CAROLINA_ASHEVILLE = [
            ...
        ]
        ```

3.  Add in as many cities/towns as you'd like to the list that you determine to be within the metropolitan area. Each city/town should be a string, like so:

        ```python
        NORTH_CAROLINA_ASHEVILLE = [
            "Biltmore Forest",
            "Black Mountain",
            "Montreat",
            ...
        ]
        ```

4.  If you wish to add multiple metropolitan areas to the file, just create another list like so:

        ```python
        NORTH_CAROLINA_ASHEVILLE = [
            "Asheville",
            "Biltmore Forest",
            "Black Mountain",
            "Montreat",
            ...
        ]

        NORTH_CAROLINA_FAYETTEVILLE = [
            "Fayetteville",
            "Eastover",
            "Falcon",
            "Godwin",
            "Hope Mills",
            ...
        ]
        ```

5.  Once you're satisfied, save the file you edited.
6.  Next, open the `areas_and_cities.py` file (found in this directory).
7.  Add in the necessary `import` statement to the top of the `areas_and_cities.py` file so that it knows to reference your state file **if it isn't there already**, like so:

        ```PYTHON
        from constants.new_mexico import *
        from constants.new_york import *
        from constants.north_carolina import * # this is similar to what you'd add
        from constants.ohio import *
        ```

8.  Then add in the relevant `keys` and `values` to the `AREAS_AND_CITIES` constant, like so:

        ```python
        AREAS_AND_CITIES = {
            ...
            "Minneapolis, MN": MINNESOTA_MINNEAPOLIS,
            "Kansas City, MO": MISSOURI_KANSAS_CITY,
            "Asheville, NC": NORTH_CAROLINA_ASHEVILLE, # you would just add one key/value pair if you added one list
            "Kalamazoo, MI": MICHIGAN_KALAMAZOO,
            "Fayetteville, NC": NORTH_CAROLINA_FAYETTEVILLE, # multiple key/value pairs mean you created multiple lists
            "Charlotte, NC": NORTH_CAROLINA_CHARLOTTE,
            "Durham, NC": NORTH_CAROLINA_DURHAM,
            ...
        ```

9.  Save your work.
10. That's it -- thank you! Open a pull request if you feel so inclined and I'll take a look.

<a name="myfootnote1">1</a>: This is more of a reminder for myself, but contributors are welcome to open a PR if they so desire.
<a name="myfootnote2">2</a>: Each list within the file represents a metropolitan area within the state after which the file is named.
<a name="myfootnote3">3</a>: If a city within a metropolitan area is outside of the metropolitan area's home state, please do not add it.
