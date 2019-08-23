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


# Toggle Markers Operator
class MarkersToggleLock(bpy.types.Operator):
	bl_idname = "shotlist.markers_lock_toggle"
	bl_label = "Lock/Unlock Markers"
	bl_description = "Toggle Lock Markers in the timeline"
	bl_options = {"UNDO"}
	
	def execute(self, context):
		lock_markers = bpy.context.scene.tool_settings.lock_markers
		bpy.context.scene.tool_settings.lock_markers = False if lock_markers else True
		
		self.report({"INFO"}, f"Markers Locked/Unlocked")
		return {"FINISHED"}