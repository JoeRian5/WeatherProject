
def calc_mean(numbers):
    '''
    Calculate and Returns the mean from the list of numbers (e.g. average Temperature/Humidity)

    List of the values - numbers
    Returns the mean of numbers

    '''

    return sum(numbers)/len(numbers)



def calc_median(numbers):
    '''
    Calculates and returns the median from the list of numbers (median - i.e. the 'Middle value')

    list of values - numbers
    Returns the median of values

    '''

    sorted_numbers = sorted(numbers)

    mid_index = int(len(sorted_numbers)/2)

    # odd number of values
    if len(sorted_numbers) % 2 ==1:
        median = sorted_numbers[mid_index]
    else:
        median = sum(sorted_numbers[mid_index-1:mid_index])/2
        #even number of values
    return median

