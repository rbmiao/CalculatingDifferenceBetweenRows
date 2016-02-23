
def main():
    import random
    data = open("random_numbers.txt", "w" ) #open file in append mode
    for i in range(1000):
        line = str(random.randint(100, 500))
        data.write( "%d %d\n" %  (int(i+1), int(line)))
##        print(i+1, line)

    data.close()
    print('1000 random numbers have been written')

main()
