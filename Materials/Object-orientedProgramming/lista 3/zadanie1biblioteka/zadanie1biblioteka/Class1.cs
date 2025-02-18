namespace zadanie1biblioteka;
public class Lista<T>
{
    class Element
    {
        public T value;
        public Element next;
        public Element previous;

        public Element(T value)
        {
            this.next = null;
            this.previous = null;
            this.value = value;
        }
    }

    Element first;

    public Lista()
    {
        first = null;
    }

    public void push_front(T elem)
    {
        Element newElement = new Element(elem);

        if (first == null)
        {
            first = newElement;
        }
        else if (first.next == null)
        {
            newElement.previous = first;
            newElement.next = first;
            first.previous = newElement;
            first = newElement;
        }
        else
        {
            newElement.next = first;
            newElement.previous = first.previous;
            first.previous = newElement;
            first = newElement;
        }
    }

    public void push_back(T elem)
    {
        Element newElement = new Element(elem);

        if (first == null)
        {
            first = newElement;
        }
        else if (first.next == null)
        {
            first.previous = newElement;
            first.next = newElement;
            newElement.previous = first;
        }
        else
        {
            first.previous.next = newElement;
            newElement.previous = first.previous;
            first.previous = newElement;
        }
    }

    public T pop_front()
    {
        if (first == null)
        {
            throw new NullReferenceException("Lista is empty");
        }
        else if (first.next == null)
        {
            T valueDel = first.value;
            first = null;
            return valueDel;
        }
        else
        {
            T valueDel = first.value;
            first.next.previous = first.previous;
            first = first.next;
            return valueDel;
        }
    }

    public T pop_back()
    {
        if (first == null)
        {
            throw new NullReferenceException("Lista is empty");
        }
        else if (first.next == null)
        {
            T valueDel = first.value;
            first = null;
            return valueDel;
        }
        else
        {
            T valueDel = first.previous.value;
            first.previous.previous.next = null;
            first.previous = first.previous.previous;
            return valueDel;
        }
    }

    public void printLista()
    {
        Element temp = first;
        while (temp != null)
        {
            Console.Write(temp.value + " ");
            temp = temp.next;
        }
    }

    public bool is_empty()
    {
        if (first == null)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}


