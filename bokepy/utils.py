import boke
import timeit


def time_estimator(data,
                   function,
                   units='seconds',
                   sampling_fraction=1000):

    '''

    Estimates the time it takes to perform a given function
    with a given dataset.

    '''

    # load the method
    method_to_call = getattr(boke, function)

    sampling_fraction = sampling_fraction
    estimate_corrector = 1.1

    sample_size = round(len(data) / sampling_fraction)
    start_time = timeit.default_timer()

    out = method_to_call(data[:sample_size])
    end_time = timeit.default_timer()
    estimate_seconds = (end_time - start_time) * sampling_fraction
    estimated_time = round(estimate_seconds * estimate_corrector, -1)

    if units is 'minutes':
        estimated_time = estimated_time / 60
        print("It will take roughly %d minutes" % estimated_time)
    else:
        print("It will take roughly %d seconds" % estimated_time)
