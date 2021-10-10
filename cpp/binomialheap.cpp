#include "binomialheap.h"

BinomialHeap::Node ::Node(double _value, Node &_parent, std::list<Node *> _children)
{
    value = _value;
    parent = &_parent;
    children = _children;

    parent->children.push_front(this);

    for (auto &i : children)
    {
        i->parent = this;
    }
}

BinomialHeap ::Node ::Node(double a)
{
    value = a;
    parent = nullptr;
}

BinomialHeap ::Node ::Node() : Node(0) {}

size_t BinomialHeap ::Node::get_order() const
{
    size_t o{};
    if (children.size() == 0)
        o = 0;
    else
    {
        o = 1;
        size_t child_order = 0;
        for (auto &i : children)
        {
            if (i->get_order() > child_order)
                child_order = i->get_order();
        }
        o += child_order;
    }
    return o;
}

void BinomialHeap::Node::set_order(size_t _count)
{
    _count = _count + 0; // I don't know what count does though !!!
    order = this->get_order();
}

bool BinomialHeap ::Node ::is_max_heap(Node &check)
{
    size_t counter{};
    for (auto &i : check.children)
    {
        if (check.value > i->value && is_max_heap(*i))
            counter++;
    }
    if (counter == check.children.size())
        return true;
    else
        return false;
}

bool BinomialHeap ::Node::is_min_heap(Node &check)
{
    size_t counter{};
    for (auto &i : check.children)
    {
        if (check.value < i->value && is_min_heap(*i))
            counter++;
    }
    if (counter == check.children.size())
        return true;
    else
        return false;
}

std::ostream &operator<<(std::ostream &out, BinomialHeap::Node &n)
{
    if (n.parent == nullptr)
        out << "{ Value = " << n.value << " , "
            << "Parent = empty"
            << " , "
            << "Order = " << n.get_order() << " }" << std::endl;
    else
        out << "{ Value = " << n.value << " , "
            << "Parent = " << n.parent->value << " , "
            << "Order = " << n.get_order() << " }" << std::endl;
    return out;
}

BinomialHeap::Node *BinomialHeap::Node::merge(Node *_n1, Node *_n2)
{
    if (_n1->get_order() != _n2->get_order())
        throw std::logic_error("Can't merge these nodes !!");
    else
    {
        if (_n1->value < _n2->value)
        {
            _n2->parent = _n1;
            _n1->children.push_back(_n2);
        }
        else
        {
            _n1->parent = _n2;
            _n2->children.push_back(_n1);
        }
    }
    if (_n1->get_order() > _n2->get_order())
        return _n1;
    else
        return _n2;
}

BinomialHeap::BinomialHeap()
{
    N = 0;
}

BinomialHeap::BinomialHeap(double num, double func(double num))
{
    for (size_t i{1}; i < num + 1; i++)
    {
        double alpha = func(i);
        BinomialHeap::insert(alpha);
        head = roots.begin();
    }
}

BinomialHeap::BinomialHeap(std::initializer_list<double> list)
{
    for (auto &i : list)
    {
        insert(i);
    }
    head = roots.begin();
}

void BinomialHeap::show()
{
    for (auto &i : roots)
    {
        std::cout << *i << std::endl;
    }
}

BinomialHeap *BinomialHeap::insert(double v)
{
    Node *nn = new Node(v);
    insert(nn);
    return this;
}

BinomialHeap *BinomialHeap::insert(Node *ins)
{
    if (roots.empty())
    {
        roots.insert(ins);
        head = roots.begin();
        N++;
        return this;
    }
    else
    {
        size_t c{};
        for (auto &i : this->roots)
        {
            if (i->get_order() != ins->get_order())
            {
                c++;
            }
            else
            {
                roots.erase(i);
                Node *on = (BinomialHeap::Node::merge(i, ins));
                return insert(on);
            }
        }
        if (c == roots.size())
        {
            roots.insert(ins);
            head = roots.begin();
        }
        N++;
        return this;
    }
}

BinomialHeap::Node *BinomialHeap::make_copy(Node *nd)
{
    co++;
    Node *md = new Node(nd->value);
    for (auto &k : nd->children)
    {
        Node *copied_child = make_copy(k);
        md->children.push_back(copied_child);
        (copied_child->parent) = md;
    }
    return md;
}

BinomialHeap ::BinomialHeap(const BinomialHeap &bh)
{
    N = bh.N;
    for (auto &i : bh.roots)
    {
        this->roots.insert(make_copy(i));
    }
    head = this->roots.begin();
}

void BinomialHeap::merge(const BinomialHeap &bm)
{
    BinomialHeap bf(bm);
    std::set<Node *>::reverse_iterator it;
    for (it = bf.roots.rbegin(); it != bf.roots.rend(); ++it)
    {
        insert(*it);
    }
    N = 0;
    for (auto &i : roots)
    {
        int m = i->get_order();
        N += pow(2, m);
    }
    bf.roots.clear();
}

double BinomialHeap::pop()
{
    if (N == 0 || this->roots.empty())
        throw std::logic_error("Can't pop when the heap is empty!!");

    double min = std::numeric_limits<double>::max();
    Node *mini = nullptr;

    for (auto &i : this->roots)
    {
        if (i->value < min)
        {
            min = i->value;
            mini = i;
        }
    }

    if (mini->children.size() == 0)
    {
        roots.erase(mini);
    }
    else
    {
        roots.erase(mini);
        for (auto &i : mini->children)
        {
            insert(i);
        }
    }
    return min;
}

void BinomialHeap::append(Node *nd)
{
    if (nd->children.size() == 0)
        Nodes.push_back(nd);
    else
    {
        Nodes.push_back(nd);
        for (auto &i : nd->children)
            append(i);
    }
}

void BinomialHeap::clear()
{
    for (auto i : this->roots)
        append(i);
    for (auto &j : this->Nodes)
    {
        if (j != nullptr)
        {
            delete j;
            j = nullptr;
            N--;
        }
    }
    this->roots.clear();
}

BinomialHeap BinomialHeap::operator=(const BinomialHeap &bhop)
{
    BinomialHeap op(bhop);
    this->clear();
    for (auto &i : op.roots)
    {
        std::cout << *i;
        this->roots.insert(i);
    }
    this->head = roots.begin();
    this->N = op.N;
    op.roots.clear();
    return *this;
}
BinomialHeap::Node& BinomialHeap::operator[](size_t _order)
{
    for(auto &i:this->roots)
    {
        if(i->get_order()==_order)
            return *i;
    }
    std::cout<<"No Node with that order"<<std::endl;
    Node* M=new Node();     //for solving the potential warning and throwing an error
    return *M;     
}

void BinomialHeap::Node::swap(Node *sw)
{
    bool ok_flag = true;    
    for (auto &i : sw->children)
    {
        if ((sw->value) > (i->value))
            ok_flag = false;
        else
            continue;
    }
    if (!ok_flag)
    {
        double minimum = std::numeric_limits<double>::max();
        for (auto &i : sw->children)
        {
            if (i->value < minimum)
                minimum = i->value;
        }
        sw->value = minimum;
        for (auto &i : sw->children)
        {
            swap(i);
        }
    }
}

BinomialHeap::~BinomialHeap()
{
    this->clear();
}