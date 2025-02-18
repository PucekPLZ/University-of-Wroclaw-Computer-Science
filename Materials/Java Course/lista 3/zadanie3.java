public class zadanie3 {
    public static void main(String[] args){
        Point x = new Point(5, 5);
        Point y = new Point(5, 7);
        Point z = new Point(5, 8);

        LineSegment xy = new LineSegment(x, y);
        LineSegment yz = new LineSegment(y, z);
        LineSegment xz = new LineSegment(x, z);

        Triangle xyz = new Triangle(x, y, z);
      }
}