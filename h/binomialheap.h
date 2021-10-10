#ifndef BinomialHeap_h
#define BinomialHeap_h
#include <iostream>
#include <list>
#include <set>
#include <vector>
#include <math.h>

class BinomialHeap
{
public:
    class Node
    {
    public:
        double value;
        Node *parent;
        std::list<Node *> children;
        Node();
        Node(double);
        Node(double value, Node &parent, std::list<Node *> children);
        size_t get_order() const;
        void set_order(size_t count);
        static bool is_min_heap(Node &);
        static bool is_max_heap(Node &);
        static Node *merge(Node *, Node *);
        friend std::ostream &operator<<(std::ostream &out, Node &n);
        friend bool operator<(Node &n1, Node &n2) { return n1.value < n2.value; };
        friend bool operator>(Node &n1, Node &n2) { return n1.value > n2.value; };
        friend bool operator==(Node &n1, Node &n2) { return n1.value == n2.value; };
        friend bool operator<=(Node &n1, Node &n2) { return n1.value <= n2.value; };
        friend bool operator>=(Node &n1, Node &n2) { return n1.value >= n2.value; };
        void swap(Node *);
        Node operator=(double v)
        {
            this->value = v;
            swap(this);
            return (*this);
        };
    private:
        size_t order = 0;};
    BinomialHeap();
    BinomialHeap(double num, double func(double num));
    BinomialHeap(const BinomialHeap &);
    BinomialHeap(std::initializer_list<double>);
    ~BinomialHeap();
    BinomialHeap operator=(const BinomialHeap &);
    BinomialHeap *insert(double);
    BinomialHeap *insert(Node *);
    struct cmp
    {
        bool operator()(const BinomialHeap::Node *a, const BinomialHeap::Node *b) const
        {
            return a->get_order() < b->get_order();
        }
    };
    std::set<Node *, cmp> roots;
    double pop();
    bool empty() { return N == 0; };
    void clear();
    void show();
    std::set<Node *, cmp>::iterator head;
    size_t get_roots_length() { return roots.size(); };
    size_t get_length() { return N; };
    void merge(const BinomialHeap &);
    std::vector<Node *> Nodes;
    void append(Node *);
    Node *make_copy(Node *);
    Node& operator[](size_t _order);
    Node *find_order(Node *, int);
    size_t co{};
private:
    size_t N = 0;
};
#endif