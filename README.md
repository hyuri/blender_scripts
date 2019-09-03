# Blender Scripts

### text_and_objects_waves.py
Turns text objects into up and down-oscilating characters. Also works for multiple text objects.

Basically, the text object will be converted to mesh, the characters will be separated into individual objects, then bound to vertices from an invisible mesh object that is also created, and, finally, a wave modifier will be added to this invisible mesh, causing the characters to oscilate according to the wave modifier. You can change the wave modifier settings to get different results.

If multiple non-text objects are selected, these objects will be bound to the mesh and oscilate up and down.

Although updated to work in Blender 2.8, this is an old script and made obsolete with things like Animation Nodes. But you can actually do some pretty interesting things with it, like hooking some drivers to a Simple Bend modifier to make the letters bend or twist.
