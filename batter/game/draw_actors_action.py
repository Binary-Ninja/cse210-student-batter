from .action import Action


class DrawActorsAction(Action):
    def __init__(self, output_service):
        self.output_service = output_service

    def execute(self, cast):
        self.output_service.clear_screen()
        for actors in cast.values():
            self.output_service.draw_actors(actors)
        self.output_service.flush_buffer()
