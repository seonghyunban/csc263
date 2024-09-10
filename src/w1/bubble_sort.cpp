#include <iostream>
#include <ostream>

void bubbleSort(int arr[], int n) {

  for (int i = 0; i < n - 1 ; i++) {

    for (int j = 0; j < n - 1 - i; j++) {

      if (arr[j] > arr[j + 1]) {

        int temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
}

void printArray(int arr[], int n) {
  std::cout << "[";
  for (int i = 0; i < n; i++) {
    std::cout << arr[i];
    if (i != n - 1) {
      std::cout << ", ";
    }
  }
  std::cout << "]" << std::endl;
}

int main() {
  int arr[] = {7, 9, 1, 4, 8, 3, 2, 5, 6, 0};
  int n = 10;

  std::cout << "Original Array: ";
  printArray(arr, n);

  bubbleSort(arr, n);
  std::cout << "Sorted Array: ";
  printArray(arr, n);
}
