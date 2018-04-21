from numpy.random import randint




def get_random_distances(n, limit):
    return randint(low=1,high=limit,size=n)


def unbalanced_distance(distances):
    print(distances)
    B=list(set(range(1,len(distances)+1))-set(distances))
    print(B)
    result= sum(abs(x-y) for x in B for y in  distances)
    print(result)
    return result

def main():
    unbalanced_distance(get_random_distances(10,200))

if __name__ == '__main__':
    main()