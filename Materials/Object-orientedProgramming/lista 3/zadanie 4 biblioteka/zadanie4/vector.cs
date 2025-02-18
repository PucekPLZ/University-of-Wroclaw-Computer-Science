namespace zadanie4;
public class Wektor
{
    public float[] vec = Array.Empty<float>();

    public Wektor(int n)
    {
        vec = new float[n];
    }

    public void fillVector(float[] elements)
    {
        for (int i = 0; i < vec.Length; i++)
        {
            vec[i] = elements[i];
        }
    }

    public void printVector()
    {
        for (int i = 0; i < vec.Length; i++)
        {
            Console.Write(vec[i] + " ");
        }
    }

    public Wektor addVectors(Wektor other)
    {
        if (vec.Length != other.vec.Length)
        {
            throw new ArgumentException("Vectors have diffrent dimensions");
        }
        else
        {
            Wektor result = new Wektor(vec.Length);

            for (int i = 0; i < vec.Length; i++)
            {
                result.vec[i] = vec[i] + other.vec[i];
            }

            return result;
        }
        
    }

    public Wektor scalarProduct(Wektor other)
    {
        if (vec.Length != other.vec.Length)
        {
            throw new ArgumentException("Vectors have diffrent dimensions");
        }
        else
        {
            Wektor result = new Wektor(vec.Length);

            for (int i = 0; i < vec.Length; i++)
            {
                result.vec[i] = vec[i] * other.vec[i];
            }

            return result;
        }
    }

    public Wektor scalar(float alfa)
    {
        Wektor result = new Wektor(vec.Length);

        for (int i = 0; i < vec.Length; i++)
        {
            result.vec[i] = vec[i] * alfa;
        }

        return result;
    }

    public float norma()
    {
        float len = 0;
        Wektor vec2 = new Wektor(vec.Length);
        vec2.fillVector(vec);
        vec2.scalarProduct(vec2);

        for (int i = 0; i < vec.Length; i++)
        {
            len += vec2.vec[i];
        }

        len = MathF.Sqrt(len);
        return len;
    }
}

