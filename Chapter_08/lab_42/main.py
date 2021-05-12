from sequence_gen_class import SequenceGen 

if __name__ == "__main__":
    seq = SequenceGen(1, 2, 10)
    seq_iterator = iter()
    # print(next(seq))
    # print(next(seq))
    # print(next(seq))

    for i in seq:
        if(i < 10):
            print(i)