def quicksort(sequenza):
    # caso terminale
    if len(sequenza) <= 1:
        return sequenza
    # caso ricorsivo
    else:
        #1. scelta pivot
        pivot = sequenza[0]
        #2. dividere sequenza secondo il pivot
        # sequenza_smaller = []
        # sequenza_pivot = []
        # sequenza_larger = []
        # for i in sequenza:
        #     # il numero è < pivot
        #     if i < pivot:
        #         sequenza_smaller.append(i)
        #     # il numero è uguale al pivot
        #     elif i == pivot:
        #         sequenza_pivot.append(i)
        #     # il numero > pivot
        #     else:
        #         sequenza_larger.append(i)

        sequenza_smaller = [n for n in sequenza if n < pivot]
        sequenza_pivot = [n for n in sequenza if n == pivot]
        sequenza_larger = [n for n in sequenza if n > pivot]

        #3. la soluzione è data da: ordinare il vettore smaller + il vettore = pivot
        # + ordinare il vettore larger
        return (quicksort(sequenza_smaller)
                + sequenza_pivot
                + quicksort(sequenza_larger))


if __name__ == '__main__':
    sequenza = [9, 3, 2, 6, 8, 5, 199]
    print(quicksort(sequenza))