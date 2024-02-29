#include <iostream>
#include <cassert>
#include <ctime>
#include <cstdlib>
#include <chrono>



void swap(long& a, long& b) {
    long temp = a;
    a = b;
    b = temp;
}


long* lomuto_partition_branchfree(long* first, long* last) {
    assert(first <= last);
    if (last - first < 2)
        return first;
    --last;
    if (*first > *last)
        swap(*first, *last);
    auto pivot_pos = first;
    auto pivot = *first;

    do {
        ++first;
        assert(first <= last);
    } while (*first < pivot);

    for (auto read = first + 1; read < last; ++read) {
        auto x = *read;
        auto less = -int(x < pivot);
        auto delta = less & (read - first);
        first[delta] = *first;
        read[-delta] = x;
        first -= less;
    }

    assert(*first >= pivot);
    --first;
    *pivot_pos = *first;
    *first = pivot;
    return first;
}


long* hoare_partition(long* first, long* last) {
    assert(first <= last);
    if (last - first < 2)
        return first;
    --last;
    if (*first > *last)
        swap(*first, *last);
    auto pivot_pos = first;
    auto pivot = *pivot_pos;
    for (;;) {
        ++first;
        auto f = *first;
        while (f < pivot)
            f = *++first;
        auto l = *last;
        while (pivot < l)
            l = *--last;
        if (first >= last)
            break;
        *first = l;
        *last = f;
        --last;
    }
    --first;
    swap(*first, *pivot_pos);
    return first;
}


long* lomuto_partition(long* first, long* last) {
    assert(first <= last);
    if (last - first < 2)
        return first;

    --last;
    if (*first > *last)
        swap(*first, *last);
    auto pivot_pos = first;
    auto pivot = *first;

    do {
        ++first;
    } while (*first < pivot);
    assert(first <= last);

    for (auto read = first + 1; read < last; ++read) {
        auto x = *read;
        if (x < pivot) {
            *read = *first;
            *first = x;
            ++first;
        }
    }

    assert(*first >= pivot);
    --first;
    *pivot_pos = *first;
    *first = pivot;
    return first;
}

int main() {
    /* В среднем Hoare отрабатывает быстрее всех
       Ломуто без ветвлений медленее всех получился
       Lomuto (branch-free) partition time: 0.0032556 seconds
       Lomuto partition time: 0.00523003 seconds
       Hoare partition time: 0.00194998 seconds
     */
    std::srand(std::time(nullptr));
    const int SIZE = 1000000;
    long arr[SIZE];
    for (int i = 0; i < SIZE; ++i) {
        arr[i] = std::rand() % 100;
    }

    long* first = arr;
    long* last = arr + SIZE - 1;

    // Измерение времени работы Lomuto без ветвлений
    auto start = std::chrono::high_resolution_clock::now();
    long* pivot_branchfree = lomuto_partition_branchfree(first, last);
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration_branchfree = end - start;
    std::cout << "Lomuto (branch-free) partition time: " << duration_branchfree.count() << " seconds" << std::endl;

    // Измерение времени работы обычного Lomuto
    std::copy(std::begin(arr), std::end(arr), first);
    start = std::chrono::high_resolution_clock::now();
    long* pivot_lomuto = lomuto_partition(first, last);
    end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration_lomuto = end - start;
    std::cout << "Lomuto partition time: " << duration_lomuto.count() << " seconds" << std::endl;

    // Измерение времени работы разбиения Хоара
    std::copy(std::begin(arr), std::end(arr), first);
    start = std::chrono::high_resolution_clock::now();
    long* pivot_hoare = hoare_partition(first, last);
    end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration_hoare = end - start;
    std::cout << "Hoare partition time: " << duration_hoare.count() << " seconds" << std::endl;
    return 0;
}

