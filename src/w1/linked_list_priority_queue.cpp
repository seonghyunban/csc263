#include <iostream>
#include <list>

template <typename T> struct Node {
  T data;
  Node *next;

  Node(T val) : data(val), next(nullptr) {}
};

template <typename T> class LinkedList {
private:
  Node<T> *head;

public:
  // Constructor
  LinkedList() : head(nullptr) {}

  ~LinkedList() {
    Node<T> *current = head;
    Node<T> *nextNode;
    while (current != nullptr) {
      nextNode = current->next;
      delete current;
      current = nextNode;
    }
  }

  void insert(T val) {
    Node<T> *newNode = new Node<T>(val);

    if (head == nullptr) {
      head = newNode;
    } else {
      Node<T> *curr = head;
      while (curr->next != nullptr) {
        curr = curr->next;
      }
      curr->next = newNode;
    }
  }

  void remove(T val) {
    Node<T> *curr = head;

    if (head == nullptr) {
      return;
    } else if (curr->data == val) {
      head = head->next;
    } else {
      while (curr->next != nullptr && curr->next->data != val) {
        curr = curr->next;
      }

      // we know curr.next == null or curr.next.data == val
      if (curr->next != nullptr) {
        curr->next = curr->next->next;
      }
    }
  }

  T index(int ind) {
    Node<T> *curr = head;
    int i = 0;
    while (curr != nullptr && i < ind) {
      i += 1;
      curr = curr->next;
    }

    // we know curr == null or i == ind
    if (curr == nullptr) {
      return -1;
    } else {
      return curr->data;
    }
  }
};

int main() {
  LinkedList<int> linky;
  linky.insert(1);
  linky.insert(2);
  linky.insert(3);
  linky.insert(4);
  linky.insert(5);
  linky.insert(6);
  std::cout << linky.index(0) << " ";
  std::cout << linky.index(1) << " ";
  std::cout << linky.index(2) << " ";
  std::cout << linky.index(3) << " ";
  std::cout << linky.index(4) << " ";
  std::cout << linky.index(5) << " ";

  linky.remove(1);

  std::cout << linky.index(0) << " ";
  std::cout << linky.index(1) << " ";
  std::cout << linky.index(2) << " ";
  std::cout << linky.index(3) << " ";
  std::cout << linky.index(4) << " ";
  std::cout << linky.index(5) << " ";

}