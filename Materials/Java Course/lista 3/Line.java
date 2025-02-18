public class Line {

    public double a;
    public double b;
    public double c;

    public Line(double a, double b, double c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    public double getA() {
        return a;
    }

    public double getB() {
        return b;
    }

    public double getC() {
        return c;
    }

    public void setA(double a) {
        this.a = a;
    }

    public void setB(double b) {
        this.b = b;
    }

    public void setC(double c) {
        this.c = c;
    }

    public static Line moveLineByVector(Line line, Vector v) {
        double a = line.getA();
        double b = line.getB();
        double c = line.getC();

        double newc = c + a * v.getDX() + b * v.getDY();

        line.setC(newc);

        return line;
    }

    public static boolean ifParallel(Line line1, Line line2) {
        if (line1.getA() == line2.getA()) {
            return true;
        } else {
            return false;
        }
    }

    public static boolean ifPerpendicular(Line line1, Line line2) {
        if (line1.getA() * line2.getA() == -1) {
            return true;
        } else {
            return false;
        }
    }

    public static Point crossPoint(Line line1, Line line2) {
        double a1 = line1.getA();
        double b1 = line1.getB();
        double c1 = line1.getC();

        double a2 = line2.getA();
        double b2 = line2.getB();
        double c2 = line2.getC();

        if (ifParallel(line1, line2)) {
            return new Point(0, 0);
        } else {
            double x = (c1 * b2 - b1 * c2) / (b1 * a2 - a1 * b2);
            double y = (a1 * c2 - c1 * a1) / (b1 * a2 - a1 * b2);

            return new Point(x, y);
        }
    }
} 
