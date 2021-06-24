import statics

from typing import Tuple

class Agent(object):
    object_id = 0

    def __init__(self,
                 name: str = None,
                 color: Tuple[float, float, float] = None,
                 is_faulty: bool = False,
                 fail_prob: float = 0.0) -> None:
        if name is None:
            name = 'Anonymous_Agent_' + str(Agent.object_id)
        if color is None:
            color = statics.get_pick_color(Agent.object_id)

        self.id = Agent.object_id
        self.name = name
        self.color = color
        self.is_faulty = is_faulty
        self.fail_prob = fail_prob
        Agent.object_id += 1

    def summary(self) -> None:
        print(f"""
#######################################################
#                    Agent Summary
# 
# ID: {self.id}
# Name: {self.name}
# Color: {self.color}
# Faulty: {self.is_faulty}
# Fail Probability: {self.fail_prob}
# 
#######################################################
        """)
