# MGSD - Multi Game SFL based Diagnosis
from mgsd import MGSD

def print_hi(name: str) -> None:
    print(f'Hi, {name}')

def sandbox() -> None:
    """
    Sandbox for testing
    :return: nothing
    """

    # # Testing constructors
    # tests.test_empty_constructors()
    # tests.test_board_constructors()
    # tests.test_agent_constructors()
    # tests.test_simulation_constructors()

    # # Testing colors
    # tests.test_simulation_agent_colors()

    # # Testing custom scenarios creation
    # tests.test_custom_scenarios_creation()

    # # Testing simulation
    # tests.test_simulate()

    # # Running the algorithm
    mgsd: MGSD = MGSD()
    mgsd.run_algorithm()


if __name__ == '__main__':
    print_hi('MGSD')
    sandbox()
