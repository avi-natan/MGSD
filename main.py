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
    """
    Available parameters
    ====================
    
    Methods that determine a simulation success/fail:
    * percentage_free_ca
      - args: {'threshold': float}
    
    Methods that determine the agents success/fail:
    * reach_final_res
      - args: {}
      
    Methods that determine how to populate the spectra:
    * agent_pass_fail_contribution
      - args: {'invert_for_success': bool}
      
    Methods for calculating diagnoses and their probabilities:
    * ochiai
      - args: {}
    * barinel
      - args: {}
    * barinel_amir
      - args: {}
      
    Methods for evaluating the algorithm:
    * wasted_effort
      - args: {}
    * precision_recall
      - args: {}
    
    """
    mgsd: MGSD = MGSD('percentage_free_ca',
                      {'threshold': 0.85},
                      'reach_final_res',
                      {},
                      'agent_pass_fail_contribution',
                      {'invert_for_success': True},
                      'barinel_amir',
                      {},
                      'wasted_effort',
                      {})
    mgsd.run_algorithm()


if __name__ == '__main__':
    print_hi('MGSD')
    sandbox()
