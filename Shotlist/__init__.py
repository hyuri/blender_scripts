# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""
Blender Add-on to Set and Manage Camera Shots.
"""

bl_info = {
	"name": "Shotlist (Alpha)",
	"author": "Hyuri Pimentel",
	"description": "Set and Manage Camera Shots",
	"blender": (2, 81, 0),
	"version": (0, 0, 1),
	"location": "View3D > Properties > Shotlist",
	"support": "COMMUNITY",
	"warning": "",
	"category": "3D View"
}

import bpy


from . shotlist import SHOTLIST
from . shotlist_operators import OPERATORS
from . shotlist_panel import ShotlistPanel


class ShotlistMenu(bpy.types.Menu):
	bl_idname = "SHOTLIST_MT_ShotlistMenu"
	bl_label = "Shotlist"

	def draw(self, context):
		layout = self.layout

		for op in OPERATORS:
			layout.operator(op.bl_idname)

def menu_func(self, context):
	self.layout.menu(ShotlistMenu.bl_idname)


class ShotProps(bpy.types.PropertyGroup):
	expand: bpy.props.BoolProperty(
		default=True,
		description="Expand, to display your shots"
	)
	
	search: bpy.props.StringProperty(
		default="",
		description="Search shots by name"
	)

	new_shot_name: bpy.props.StringProperty(
		default="",
		description="New Shot Name"
	)
	
	scroll: bpy.props.IntProperty(
		default=1,
		min=1,
		max=len(SHOTLIST),
		description="Navigate through your shots"
	)

def register():
	# Operators
	for op in OPERATORS:
		bpy.utils.register_class(op)

	# Panel
	bpy.utils.register_class(ShotlistPanel)

	# Menu
	bpy.utils.register_class(ShotlistMenu)
	bpy.types.VIEW3D_MT_object.append(menu_func)

	# Props
	bpy.utils.register_class(ShotProps)
	bpy.types.Scene.shot_props = bpy.props.PointerProperty(type=ShotProps)

	# ShotsLoadExisting Button
	# OPERATORS[0]().execute(context=bpy.context)

def unregister():
	# Operators
	for op in OPERATORS:
		bpy.utils.unregister_class(op)

	# Panel
	bpy.utils.unregister_class(ShotlistPanel)

	# Menu
	bpy.utils.unregister_class(ShotlistMenu)
	bpy.types.VIEW3D_MT_object.remove(menu_func)

	# Props
	bpy.utils.unregister_class(ShotProps)

	if bpy.context.scene.get("shot_props"):
		del bpy.context.scene["shot_props"]

	try:
		del bpy.types.Scene.shot_props
	except:
		pass

if __name__ == "__main__":
	OPERATORS[0]().execute(context=bpy.context)
	register()

# classes = (
# 	ShotsLoadExisting,
# 	ShotsAdd,
# 	ShotsRemoveAll,
# 	ShotlistPanel,
# )

# register, unregister = bpy.utils.register_classes_factory(classes)