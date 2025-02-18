public final class Vector {
    
    public final double dx;
    public final double dy;

    public Vector(double dx, double dy) {
        this.dx = dx;
        this.dy = dy;   
    }

    public double getDX() {
        return dx;
    }

    public double getDY() {
        return dy;
    }

    public static Vector fold(Vector v, Vector w) {
        double dx = v.getDX() + w.getDX();
        double dy = v.getDY() + w.getDY();

        return new Vector(dx, dy);
    }
}
