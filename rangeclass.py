from logging.handlers import RotatingFileHandler
import logging

console = logging.StreamHandler()
to_file = RotatingFileHandler('logging.log', maxBytes=1024, backupCount=2)

formatter = logging.Formatter('%(asctime)s - %(loglevel)s - %(message)s', datefmt='%y-%m-%d %H:%M:%S')


logger = logging.getLogger('My Logger')
logger.setLevel(logging.INFO)
logger.addHandler(to_file)
logger.addHandler(console)


class range_examp:

    def __init__(self, end, step=1):
        logger.info('Initializing the range_examp class')
        self.current = 0
        self.end = end
        self.step = step
    
    def __iter__(self):
        logger.info('In side the iter function of the range_examp class')

        return self
    
    def __next__(self):
        logger.info('Inside the next function of the range_examp class')

        if self.current >=self.end:
            raise StopIteration()
        else:
            return_val = self.current
            self.current += self.step
            return return_val

''' 
Same behaviour using generator
'''


def range_gen(end):
    current = 0
    while current < end:
        yield current
        current +=1





def main():
    # for i in range_gen(5):
    #     print(i)
    while True:

        for i in range_examp(5):
            print(i)

if __name__=='__main__':
    main()