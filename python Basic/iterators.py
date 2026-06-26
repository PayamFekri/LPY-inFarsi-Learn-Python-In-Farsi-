#<iter> = iter(<collection>)
#<iter> = iter(<function>, to_exclusive)     # Sequence of return values until 'to_exclusive'.
#<el>   = next(<iter> [, default])           # Raises StopIteration or returns 'default' on end.

my_list = [3,9,5,4,6,10,1,12]
my_iter = iter(my_list)