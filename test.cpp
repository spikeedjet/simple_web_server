#include <stdio.h>

using namespace std;


// class Box 
// {
//     public:
//         double length;
//         double breadth;
//         double height;

//         double get(void);
//         void set(double l, double b, double h);

// };

// double Box::get(void)
// {
//     return length * breadth * height;
// }

// void Box::set(double l, double b, double h)
// {
//     length = l;
//     breadth = b;
//     height = h;
// }

// int main()
// {
//     Box box;
//     box.set(10, 20, 30);
//     printf("Volume of box is %f\n", box.get());
//     return 0;
// }

class Shape 
{
    public:
        void setWidth(int w)
        {
            width = w;
        }
        void setHeight(int h)
        {
            height = h;
        }
    protected:
        int width;
        int height;

};

class PaintCost
{
    public:
        int getCost(int area)
        {
            return area * 70;
        }
};


class Rectangle: public Shape, public PaintCost
{
    public:
        int getArea()
        {
            return (width * height);
        }
};


int main(void)
{
    Rectangle Rect;
    Rect.setWidth(5);
    Rect.setHeight(7);

    // Print the area of the object.
    printf("Total area: %d", Rect.getArea());

    // Calculate the total cost of painting
    printf("\nTotal paint cost: %d", Rect.getCost(Rect.getArea()));
    return 0;
}