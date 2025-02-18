public class Point {
    
    private double x;
    private double y;

    public Point(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    public void setX(double x) {
        this.x = x;
    }

    public void setY(double y) {
        this.y = y;
    }

    public void movePointByVector(Vector v) {
        x += v.getDX();
        y += v.getDY();
    }

    public void rotatePoint(Point p, double angle) {
        double deltaX = x - p.getX();
        double deltaY = y - p.getY();

        double angleInRadians = Math.toRadians(angle);

        double newX = deltaX * Math.cos(angleInRadians) - deltaY * Math.sin(angleInRadians);
        double newY = deltaX * Math.sin(angleInRadians) + deltaY * Math.cos(angleInRadians);

        x = newX + p.getX();
        y = newY + p.getY();
    }
}