class Collection
    def initialize
        @data = []
    end

    def add(element)
        @data << element
    end

    def insert_at(index, element)
        return false if index < 0 || index > @data.length
        @data.insert(index, element)
        true
    end

    def swap(i, j)
        return false if i < 0 || j < 0 || i >= @data.length || j >= @data.length
        @data[i], @data[j] = @data[j], @data[i]
        true
    end

    def length
        @data.length
    end

    def get(i)
        return nil if i < 0 || i >= @data.length
        @data[i]
    end
end

class Sorter
    def sort1(kolekcja) # Bubble Sort
        n = kolekcja.length
        for i in 0...n
            for j in 0...(n - i - 1)
                if kolekcja.get(j) > kolekcja.get(j + 1)
                    kolekcja.swap(j, j + 1)
                end
            end
        end
    end

    def sort2(kolekcja) # Selection Sort
        n = kolekcja.length
        for i in 0...n
            min_index = i
            for j in (i + 1)...n
                if kolekcja.get(j) < kolekcja.get(min_index)
                    min_index = j
                end
            end
            kolekcja.swap(i, min_index) if min_index != i
        end
    end
end

# Bubble Sort ma najgorszy przypadek i średnią złożoność czasową O(n^2)
# Selection Sort ma również najgorszy przypadek i średnią złożoność czasową O(n^2)
# Bubble Sort jest zwykle wolniejszy niż Selection Sort ze względu na liczbę wykonywanych operacji swap


