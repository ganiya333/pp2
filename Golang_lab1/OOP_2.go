package main 
import "fmt"

type Employee struct {
	name string 
	id int
}

type Manager struct{
	Employee
	Department string 
}

func (p Employee) work() {
	fmt.Print("Name: ", p.name, ". Employee's id: ", p.id)

}
func main (){
	manager := Manager{
		Employee: Employee{
			name: "Ganiya",
			id: 12,
		},
		Department: "IT",
	}
	manager.work()
}