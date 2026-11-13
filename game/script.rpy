## The Catalog, in Ren'Py: the route select. Every route registers its own card
## (vn_register_route in its route.rpy); nothing here changes when a route is added.

label start:
    scene black
    $ vn_route = None
    ## no Back/Save/... over the route select: there's no story to save yet
    $ quick_menu = False
    call screen vn_route_select
    $ quick_menu = True
    jump expression _return
