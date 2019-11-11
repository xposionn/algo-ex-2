from typing import List


class Agent:
    def value(option: int) -> float:
        return 1.0


def isParetoImprovement(agents: List[Agent], option1: int, option2: int):
    existsImprove = False
    for agent in agents:
        diff = agent.value(option1) - agent.value(option2)
        if diff > 0:
            existsImprove = True
        if diff < 0:
            return False

        return existsImprove


def isParetoOptimal(agents: List[Agent], option1: int, allOptions: List[int]):
    for option in allOptions:
        if isParetoImprovement(agents, option, option1):
            return False
    return True
