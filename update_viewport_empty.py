import bpy
import mathutils

_viewport_sync_handler = None

def update_viewport_empty():
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            for space in area.spaces:
                if space.type == 'VIEW_3D':
                    region_3d = space.region_3d
                    view_matrix = region_3d.view_matrix.inverted()

                    empty = bpy.data.objects.get("Viewport_Empty")
                    if empty:
                        empty.matrix_world = view_matrix
                    break

def draw_callback_px():
    update_viewport_empty()

class VIEW3D_OT_enable_viewport_sync(bpy.types.Operator):
    """Enable live viewport sync to empty"""
    bl_idname = "view3d.enable_viewport_sync"
    bl_label = "Enable Viewport Empty Sync"

    def execute(self, context):
        global _viewport_sync_handler
        if _viewport_sync_handler is None:
            _viewport_sync_handler = bpy.types.SpaceView3D.draw_handler_add(
                draw_callback_px, (), 'WINDOW', 'POST_VIEW'
            )
            self.report({'INFO'}, "Viewport sync enabled.")
        else:
            self.report({'INFO'}, "Viewport sync already active.")
        return {'FINISHED'}

class VIEW3D_OT_disable_viewport_sync(bpy.types.Operator):
    """Disable viewport sync"""
    bl_idname = "view3d.disable_viewport_sync"
    bl_label = "Disable Viewport Empty Sync"

    def execute(self, context):
        global _viewport_sync_handler
        if _viewport_sync_handler is not None:
            bpy.types.SpaceView3D.draw_handler_remove(_viewport_sync_handler, 'WINDOW')
            _viewport_sync_handler = None
            self.report({'INFO'}, "Viewport sync disabled.")
        else:
            self.report({'INFO'}, "Viewport sync was not active.")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(VIEW3D_OT_enable_viewport_sync)
    bpy.utils.register_class(VIEW3D_OT_disable_viewport_sync)

def unregister():
    bpy.utils.unregister_class(VIEW3D_OT_enable_viewport_sync)
    bpy.utils.unregister_class(VIEW3D_OT_disable_viewport_sync)

if __name__ == "__main__":
    register()
    bpy.ops.view3d.enable_viewport_sync()
