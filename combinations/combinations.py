import sys
import itertools
import argparse

def main(**kwargs):
    
    name = 'combinations.txt'  # Name of text file coerced with +.txt
    print('Creating new text file %s' % name) 

    try:
        file = open(name, 'w')   # Trying to create a new file or open one

        possibilities = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        num_digits = kwargs['num_digits'][0];
        num_pos = 62**num_digits
        print 'You should get %s results.' % num_pos
        print 'Be warned that above 5 digits, depending on your machine, this may take a while.'

        # Define a word length and create all possible combinations with repetition (i.e. AB -and- BA) for that word
        index = 1;
        while(index <= num_digits):
            combinations = itertools.combinations_with_replacement(possibilities, index)
            for comb in combinations:
                s = "".join(comb)
                file.write(s+'\n')
            index +=1

        print "Process completed."
        file.close()

    except:
        print('Something went wrong! Can\'t tell what?')
        sys.exit(0) # quit Python

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Given a length, will return all combinations with repetition of 0-9, a-z, A-Z.')
    parser.add_argument('num_digits', metavar='N', type=int, nargs='+',
                   help='Length of combinations (i.e. 6 for all combinations up to 6 digits)')
    args = parser.parse_args()
    main(**vars(args))