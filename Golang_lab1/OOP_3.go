package main

import (
	"fmt"
	"math"
)

type shape interface {
	area() float64
}

type circle struct {
	radius float64
}

type rect struct {
	length float64
	width  float64
}

func (c circle) area() float64 {
	return math.Pi * c.radius * c.radius
}

func (r rect) area() float64 {
	return r.length * r.width
}

func result(s shape) {
	fmt.Println("Area is equal to -", s.area())
}

func main() {
	circle_area := circle{radius: 10}
	rect_area := rect{length: 5, width: 6}

	result(circle_area)
	result(rect_area)
}
