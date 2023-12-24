
class GameProxy():

    @classmethod
    def set_context(cls, context):
        cls.__context = context

    @classmethod
    def add_sprite_group(cls, scene_object: object, group_flag): 
        cls.__context.groups[group_flag].add( scene_object )

