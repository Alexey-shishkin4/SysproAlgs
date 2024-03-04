#include <iostream>


template<typename T>
class DynamicArray {
private:
    T* arr;
    int capacity;
    int length;

    void realloc(int newCapacity) {
        T* newArr = new T[newCapacity];
        for (int i = 0; i < length; ++i) {
            newArr[i] = arr[i];
        }
        delete[] arr;
        arr = newArr;
        capacity = newCapacity;
    }

public:
    DynamicArray() : arr(nullptr), capacity(0), length(0) {}

    ~DynamicArray() {
        delete[] arr;
    }

    void append(const T& element) {
        if (length == capacity) {
            int newCapacity = (capacity == 0) ? 1 : capacity * 2;
            realloc(newCapacity);
        }
        arr[length++] = element;
    }

    void remove() {
        if (length == 0) {
            std::cout << "Array is empty" << std::endl;
            std::terminate();
        }
        length--;
        if (length <= capacity / 4) {
            int newCapacity = (capacity == 1) ? 1 : capacity / 2;
            realloc(newCapacity);
        }
    }

    T& operator[](int index) {
        if (index < 0 || index >= length) {
            std::cout << "Index out of range" << std::endl;
            std::terminate();
        }
        return arr[index];
    }
};


int main() {
    return 0;
}
