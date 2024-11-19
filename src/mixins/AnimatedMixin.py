"""
Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the AnimatedMixin.
"""

from gale.animation import Animation

class AnimatedMixin:
    def generate_animations(self, animation_defs):
        for animation_id, values in animation_defs.items():
            animation = Animation(
                values["frames"],
                values.get("interval", 0),
                loops=values.get("loops"),
            )
            self.animations[animation_id] = animation

    def change_animation(self, animation_id):
        new_animation = self.animations[animation_id]
        if new_animation != self.current_animation:
            self.current_animation = new_animation
            self.current_animation.reset()
            self.frame_index = self.current_animation.get_current_frame()

    def update(self, dt):
        self.current_animation.update(dt)
        self.frame_index = self.current_animation.get_current_frame()