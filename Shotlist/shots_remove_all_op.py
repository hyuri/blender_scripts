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

# Shot Remove Operator
class ShotsRemoveAll(bpy.types.Operator):
	bl_idname = "shotlist.shots_remove_all"
	bl_label = "Remove All Shots"
	bl_description = "Remove All Shots"
	bl_options = {"UNDO"}
	
	def execute(self, context):
		SHOTLIST.remove_all()
			
		self.report({"INFO"}, "All Shots Have Been Removed")
		return {"FINISHED"}