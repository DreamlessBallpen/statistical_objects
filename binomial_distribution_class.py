# We try creating a simple binomial distribution object
# where parameters can be input, and we can generate values depending on what we need.

import numpy as np
import pandas as pd


class BinomialDistSimulation:
    """ We create a Binomial Distribution with the number of trials and probability of success as initial parameters to
    set. This is in contrast to Excel's BINOM.DIST function, which directly calculates the probability of X successes in
    n trials, and as such, needing X directly as a parameter.

    Current parameter settings can be shown with print(BinomialDistSimulation object).
    """

    # Tested
    def __init__(self, p_success: float, n_trials: int):
        """ Probability of success should not exceed 1 """
        self.__p_success = p_success
        self.__n_trials = n_trials
        self.__results_list = pd.Series(data=None)

    # Tested
    def bernoulli_trial(self) -> bool:
        """ Returns the result of a simulated single trial """
        simulated = np.random.rand()
        return True if simulated < self.__p_success else False

    # Tested
    def __str__(self):
        """Customized the print() method for this object, for checking the parameters we have"""
        results = 'No values yet' if len(self.__results_list) == 0 else str(list(self.__results_list.values))
        text_output = 'Current value of parameters:\n\t' + \
                      'Probability of success: ' + str(self.__p_success) + '\n\t' + \
                      'Number of trials: ' + str(self.__n_trials) + '\n'

        # NOTE:
        #   Commented code below is the version if we want to print values from the generated distribution as well
        #   However, this isn't practical with a large number of trials.

        # results = 'No values yet' if len(self.__results_list) == 0 else str(list(self.__results_list.values))
        # text_output = 'Current value of parameters:\n\t' + \
        #    'Probability of success: ' + str(self.__p_success) + '\n\t' + \
        #    'Number of trials: ' + str(self.__n_trials) + '\n' + \
        #    'Current run: \n\t' + results + '\n'

        return text_output

    # Tested
    def get_p_success(self):
        return self.__p_success

    # Tested
    def set_p_success(self, p_success):
        self.__p_success = p_success

    # Tested
    def get_n_trials(self):
        return self.__n_trials

    # Tested
    def set_n_trials(self, n_trials):
        self.__n_trials = n_trials

    # Tested
    def generate_simulation_checks(self):
        """ Basic checks for now """
        if self.__n_trials < 1 or not isinstance(self.__n_trials, int):
            return False
        elif not isinstance(self.__p_success, float) or self.__p_success > 1 or self.__p_success < 0:
            return False
        else:
            return True

    # Tested
    def generate_simulation(self):
        if not self.generate_simulation_checks():
            print('Cannot generate simulation, check parameter values')
            return

        # We clear the results list first
        self.__results_list.drop(labels=list(self.__results_list.index))

        # Then run the bernoulli trials for n items
        for i in range(self.__n_trials):
            self.__results_list[i] = self.bernoulli_trial()

    # Tested
    def get_current_simulation(self):
        if len(self.__results_list) == 0:
            print('Warning: No current simulation. nan value returned')
            return np.nan
        return self.__results_list

    # Tested
    def return_current_tally(self):
        """Returns a pandas series object containing two indexes: success and fail, and the count of
        their respective values"""
        success = self.__results_list[self.__results_list == True].count()
        fail = self.__results_list[self.__results_list == False].count()
        index = ['success', 'fail']
        data = [success, fail]
        return pd.Series(data=data, index=index)
    
  # Tested
    def print_current_tally(self):
        print(self.return_current_tally())

# Sample code to run for a demonstration
coin_flips = BinomialDistSimulation(0.5, 10)
coin_flips.generate_simulation()
coin_flips.print_current_tally()

