public class LineSegment {
    
    private Point A;
    private Point B;

    public LineSegment(Point A, Point B) {
        if (A.getX() == B.getX() && A.getY() == B.getY()) {
            throw new IllegalArgumentException("To te same punkty!");
        }

        this.A = A;
        this.B = B;
    }

    public Point getA() {
        return A;
    }

    public Point getB() {
        return B;
    }

    public void moveLineByVector(Vector v) {
        A.setX(A.getX() + v.getDX());
        A.setY(A.getY() + v.getDY());

        B.setX(B.getX() + v.getDX());
        B.setY(B.getY() + v.getDY());
    }

    public void rotateLine(Point p, double angle) {
        double deltaAX = A.getX() - p.getX();
        double deltaAY = A.getY() - p.getY();
        double deltaBX = B.getX() - p.getX();
        double deltaBY = B.getY() - p.getY();

        double angleInRadians = Math.toRadians(angle);

        double newAX = deltaAX * Math.cos(angleInRadians) - deltaAY * Math.sin(angleInRadians);
        double newAY = deltaAX * Math.sin(angleInRadians) + deltaAY * Math.cos(angleInRadians);
        double newBX = deltaBX * Math.cos(angleInRadians) - deltaBY * Math.sin(angleInRadians);
        double newBY = deltaBX * Math.sin(angleInRadians) + deltaBY * Math.cos(angleInRadians);

        A.setX(newAX + p.getX());
        A.setY(newAY + p.getY());
        B.setX(newBX + p.getX());
        B.setY(newBY + p.getY());
    }
}
