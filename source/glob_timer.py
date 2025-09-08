import pygame


class Timer:
    def __iter__(self):
        for name in self.timers.keys():
            yield

    def ended(self, name, looping=False):
        if looping:
            return (
                self.timers[name]["Current_time"] <= 0
                and self.loops[name]["Current_state"]
                >= self.loops[name]["Initial_state"]
            )
        else:
            return self.timers[name]["Current_state"] <= 0

    def renew_time(self, name, new_amount=None):
        if new_amount is None:
            self.timers[name]["Current_state"] = self.timers[name]["Initial_state"]
        else:
            self.timers[name]["Current_time"] = new_amount
            self.timers[name]["Initial_state"] = new_amount

    def decrease_timer(
        self, name, frames_to_0=None, dec_speed=1, looping=False, loop_amount=-1
    ):
        if name not in self.timers:
            self.add_timer(name, frames_to_0)

        if frames_to_0 is not None:
            self.timers[name]["Initial_time"] = frames_to_0
            if self.timers[name]["Current_time"] > frames_to_0:
                self.timers[name]["Current_time"] = frames_to_0

            self.timers[name]["Current_time"] -= dec_speed

            if loop_amount != -1 and loop_amount != self.loops[name]["Initial_state"]:
                self.loops[name]["Initial_state"] = loop_amount

            if self.timers[name]["Current_time"] < 0:
                if not looping:
                    self.timers[name]["Current_time"] = 0
                else:
                    self.increase_loop(name, loop_amount)

    def increase_loop(self, name, loop_amount=-1):
        if loop_amount == -1:
            self.timers[name]["Current_time"] = self.timers[name]["Initial_state"]

        else:
            if self.loops[name]["Current_state"] >= self.loops[name]["Initial_state"]:
                self.timers[name]["Current_time"] = 0
            else:
                self.loops[name]["Current_state"] += 1
                self.timers[name]["Current_time"] = self.timers[name]["Initial_time"]

            return self

    def add_timer(self, name, active_frames):
        self.timers[name] = {
            "Initial_time": active_frames,
            "Current_time": active_frames,
        }
        self.loops[name] = {"Initial_state": 1, "Current_state": 1}

    def __init__(self, global_timer):
        self.timers = {}
        self.loops = {}
