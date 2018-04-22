def efficient(x,y,L,R):
    if L < (x ** y) <= R:
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    efficient(3,2,5,7)