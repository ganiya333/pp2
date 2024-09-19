package main 
import "fmt"

type Person struct {
	name string 
	age int 
}
func (p Person ) greet (){
	fmt.Print("Hi! My name is ", p.name, ". I am", p.age)
}
func main (){
	

	person := Person {name:"Ganiya", age: 19}
	person.greet()

}