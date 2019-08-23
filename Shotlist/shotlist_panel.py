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

import bpy

from . shotlist import SHOTLIST
from . shotlist_operators import ShotsLoadExisting, ShotsAdd, ShotsRemoveAll, MarkersToggleLock


# Main Panel
class ShotlistPanel(bpy.types.Panel):
	bl_idname = "SHOTSLIST_PT_ShotlistPanel"
	bl_label =  "Shotlist"
	bl_category = "View"

	switch = 1
	bl_space_type = "VIEW_3D" if switch else "PROPERTIES"
	bl_region_type = "UI" if switch else "WINDOW"
	bl_context = "" if switch else "data"
	
	@classmethod
	def poll(cls, context):
		# Only display this panel in object mode
		return context.mode == "OBJECT"

	def draw(self, context):
		layout = self.layout

		# Get active Scene
		self.scene = context.scene
		
		# Get active object
		self.obj = context.object

		info_row = layout.box().row(align=True)

		# If we have an active object
		if self.obj:
			if self.obj.type == "CAMERA":
				# Active active label
				info_row.label(text=self.obj.name, icon="OUTLINER_OB_CAMERA")

			else:
				# Active obj label
				info_row.label(text=self.obj.name, icon="OBJECT_DATA")

		# If no active object
		else:
			# Info
			info_row.label(text="[ No Active Camera ]", icon="RESTRICT_SELECT_ON")
		
		# Current Frame Label
		info_row.label(text=str(self.scene.frame_current), icon="TIME")

		# ShotsAdd Row
		shots_add_row = layout.row(align=True)

		# shots_add_row.props(props, "new_shot_name", icon="TIME", icon_only=False, emboss=False)

		# ShotsAdd Button
		shots_add_row.operator(ShotsAdd.bl_idname, text="Add Shot", icon="SEQUENCE")

		layout.separator()

		# Props
		props = context.scene.shot_props
		
		# Box
		box = layout.box()
		
		if not props.expand:
			# Hide Shots
			shots_header = box.row(align=True)

			shots_header.prop(props, "expand", icon="TRIA_RIGHT",  icon_only=True, emboss=False)
			
			# Shots Title
			shots_header.label(icon="SEQUENCE", text=f"{str(len(SHOTLIST))}")

		else:
			# Show Shots
			shots_header = box.row(align=False)
			shots_header.prop(props, "expand", icon="TRIA_DOWN", icon_only=True, emboss=False)
			
			# List of Shots
			if SHOTLIST:
				# SearchBar
				# box.row().prop(props, "search", text="Search", icon="VIEWZOOM")
			
				# Scroll
				shots_header.prop(props, "scroll", text="Shot")
				
				sorted_shots = []
				for shot in SHOTLIST:
					sorted_shots.append(shot)
					sorted_shots = sorted(sorted_shots, key=lambda shot: shot.start)
				
				for shot in sorted_shots:
					box.row().label(text=f"{str(shot.start)} | {str(shot.name)} | {str(shot.camera.name)}")
				
				# # Shots Title
				# box.row().label(icon="SEQUENCE", text=f"{str(len(SHOTLIST))}")
				
				layout.separator()

				# MarkersLockToggle Row
				lock_text = "Unlock Markers" if context.scene.tool_settings.lock_markers else "Lock Markers"
				lock_icon = "LOCKED" if context.scene.tool_settings.lock_markers else "UNLOCKED"
				layout.row().operator(MarkersToggleLock.bl_idname, text=lock_text, icon=lock_icon)
				
				layout.row().operator(ShotsLoadExisting.bl_idname, text="Rescan Timeline", icon="FILE_REFRESH")

				layout.separator()

				layout.row().operator(ShotsRemoveAll.bl_idname, text="Remove All Shots", icon="CANCEL")
			
			else:
				# ShotsLoadExisting Button
				box.row().operator(ShotsLoadExisting.bl_idname, text="Scan Timeline", icon="FILE_REFRESH")