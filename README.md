# Blender Scripts

### text_and_objects_waves.py
Turns text objects into up and down-oscilating characters. Also works for multiple text objects.
Basically, the text object will be converted to mesh, the characters will be separated into individual objects, the characters will be bound to vertices from an invisible mesh object that is also created, and a wave modifier will be applied to this invisible mesh, causing the characters to oscilate according to the wave modifier. You can change the settings in the wave modifier to get different results.

If multiple non-text objects are selected, these objects will be bound to the mesh and oscilate up and down.
