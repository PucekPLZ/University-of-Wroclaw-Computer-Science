import static java.lang.Math.*;

public class Triangle {
    
    private Point A;
    private Point B;
    private Point C;

    public Triangle(Point A, Point B, Point C) {
        double AB = sqrt(pow((B.getX() - A.getX()), 2) + pow((B.getY() - A.getY()), 2));
        double AC = sqrt(pow((C.getX() - A.getX()), 2) + pow((C.getY() - A.getY()), 2));
        double BC = sqrt(pow((C.getX() - B.getX()), 2) + pow((C.getY() - B.getY()), 2));

        if (AB + AC == BC || AB + BC == AC || AC + BC == AB) {
            throw new IllegalArgumentException("Punkty są współliniowe!");
        }

        this.A = A;
        this.B = B;
        this.C = C;
    }

    public Point getA() {
        return A;
    }

    public Point getB() {
        return B;
    }

    public Point getC() {
        return C;
    }

    public void moveTriangleByVector(Vector v) {
        A.setX(A.getX() + v.getDX());
        A.setY(A.getY() + v.getDY());

        B.setX(B.getX() + v.getDX());
        B.setY(B.getY() + v.getDY());

        C.setX(C.getX() + v.getDX());
        C.setY(C.getY() + v.getDY());
    }

    public void rotateTriangle(Point p, double angle) {
        double deltaAX = A.getX() - p.getX();
        double deltaAY = A.getY() - p.getY();
        double deltaBX = B.getX() - p.getX();
        double deltaBY = B.getY() - p.getY();
        double deltaCX = C.getX() - p.getX();
        double deltaCY = C.getY() - p.getY();

        double angleInRadians = Math.toRadians(angle);

        double newAX = deltaAX * Math.cos(angleInRadians) - deltaAY * Math.sin(angleInRadians);
        double newAY = deltaAX * Math.sin(angleInRadians) + deltaAY * Math.cos(angleInRadians);
        double newBX = deltaBX * Math.cos(angleInRadians) - deltaBY * Math.sin(angleInRadians);
        double newBY = deltaBX * Math.sin(angleInRadians) + deltaBY * Math.cos(angleInRadians);
        double newCX = deltaCX * Math.cos(angleInRadians) - deltaCY * Math.sin(angleInRadians);
        double newCY = deltaCX * Math.sin(angleInRadians) + deltaCY * Math.cos(angleInRadians);

        A.setX(newAX + p.getX());
        A.setY(newAY + p.getY());
        B.setX(newBX + p.getX());
        B.setY(newBY + p.getY());
        C.setX(newCX + p.getX());
        C.setY(newCY + p.getY());
    }
}
