from sequence_gen_class import SequenceGen
from exceptions.sequnence_invalid_argument_exception_class import SequenceInvalidArgumentException 

def ex_1():
    seq = SequenceGen(1, 2, 10)

    # seq_iterator = iter()
    # print(next(seq))
    # print(next(seq))
    # print(next(seq))

    for i in seq:
        if(i < 10):
            print(i)
        else:
            break

def ex_2():
    try:
        seq = SequenceGen(1, 11, 10)
    except SequenceInvalidArgumentException as e:
        print(e)

if __name__ == "__main__":
    ex_2()
