import bpy

# TODO:
# Make rig parent creation into its own function
# Solidify thickness formula: text extrude * 2


def main():
    selected_objs = bpy.context.selected_objects

    text = True

    if text:
        for obj in selected_objs:
            # Break text down into letters
            letters = text_breakdown(obj)

            # Generate rig for letters
            generate_rig(letters)

    else:
        # Generate rig for selected objs
        generate_rig(selected_objs)


# Generate rig
def generate_rig(objs):
    mesh_verts = []
    
    for obj in objs:
        mesh_verts.append(obj.location)
    
    # Create rig, solo select and hide it from viewport
    rig = create_obj("LettersRig", (0, 0, 0), mesh_verts)
    rig.hide_select = False
    solo_select(rig)
    bpy.ops.object.origin_set(type="ORIGIN_GEOMETRY")
    
    # Create rig Parent
    bpy.ops.object.add(location=rig.location) # Create Empty object at rig's position
    rig_parent = bpy.context.object # Assign newly created Empty object to rig_parent
    rig_parent.name = "LettersRigParent"
    #rig_parent.show_name = True
    rig_parent.empty_display_type = "CUBE"
    rig_parent.empty_display_size = 2.0
    
    # Parent Vertices
    for i, obj in enumerate(objs):
        obj.parent = rig
        obj.parent_type = "VERTEX"
        obj.parent_vertices[0] = i

        solo_select(obj)
        bpy.ops.object.location_clear()
    
    rig.parent = rig_parent

    solo_select(rig)
    bpy.ops.object.location_clear()
    bpy.ops.object.modifier_add(type="WAVE")
    #rig.hide_select = True
    rig.hide_set(True)
    
    #bpy.context.space_data.context = "MODIFIER"


def text_breakdown(obj):
    # Convert text to mesh
    if obj.type == "FONT":
        solo_select(obj)
        bpy.ops.object.convert(target="MESH")

    bpy.ops.mesh.separate(type="LOOSE")
    bpy.ops.object.origin_set(type="ORIGIN_GEOMETRY")

    return bpy.context.selected_objects


def create_obj(name, origin, verts):
    # Create mesh, object, and set origin
    mesh = bpy.data.meshes.new(f"{name}Mesh")
    obj = bpy.data.objects.new(name, mesh)
    obj.location = origin

    # Link object to scene
    bpy.context.collection.objects.link(obj)

    # Create mesh from given verts. Either edges or faces should be []
    mesh.from_pydata(verts, [], [])

    # Update mesh with new data
    mesh.update(calc_edges=True)

    return obj


# Select Single Object
def solo_select(obj):
    for selected_obj in bpy.context.selected_objects:
        selected_obj.select_set(False)
    
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj


main()


if __name__ == "__main__":
    pass
