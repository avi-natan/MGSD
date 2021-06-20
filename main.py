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
    * barinel_avi
      - args: {'method_for_calculating_priors': str 
                                                <priors_one,
                                                priors_static,
                                                priors_amir,
                                                priors_paper,
                                                priors_intersections1,
                                                priors_intersections2>}
    * barinel_amir
      - args: {'method_for_calculating_priors': str <priors_one,
                                                priors_static,
                                                priors_amir,
                                                priors_paper,
                                                priors_intersections1,
                                                priors_intersections2>}
      
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
                      {'method_for_calculating_priors': 'priors_intersections2'},
                      'wasted_effort',
                      {})

    # Make sure that the file with the same name is located inside the
    # 'simulations_config_files' directory
    # mgsd.run_algorithm()
    mgsd.run_algorithm(config_filename='benchmark1.json')


if __name__ == '__main__':
    print_hi('MGSD')
    sandbox()
