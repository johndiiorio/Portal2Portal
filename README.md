# Portal2Portal #
Compiler for a portal-controlled esolang with dynamic 2D program input

### Portal2Portal explained: ###

##### Commands: #####
```<``` Move pointer left

```>``` Move pointer right

```+``` Increment tape under pointer

```-``` Decrement tape under pointer

```.``` Output character under tape (ASCII)

```(x1, y1, x2, y2)``` Spawn two linked portals, one at ```x1, y1```, one at ```x2,y2```, that conserve program momentum

```{x1, y1, x2, y2}``` Spawn two linked portals, one at ```x1, y1```, one at ```x2,y2```, that reverse program momentum

```[x, y]``` Delete portal at location ```x, y```

##### Information: #####

Begin each command string with ```x,y:``` to insert them at coordinates ```x,y```. Separate each command string with ```|```

The program begins reading to the right at location ```0, 0```. Portals are only entered if the tape data under the pointer is not zero. If a portal is spawned on an existing command, that command is replaced with the portal. The program halts if it enters an unlinked portal.

### How to run: ###
Place the program in the ```main.py``` file and run ```python main.py```

### Contact: ###
This esolang and compiler is under development, and not yet ready for release.

Help contribute by sending me an [email](mailto:johnzdiiorio@gmail.com), opening a GitHub issue, or making a pull request.