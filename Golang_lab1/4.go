package main 
import "fmt"


func add(n, m int) int {
	return n+m
}
func swap (a,b string)(string,string) {
	return b,a
}
func division (n,m int)(int, int){
	return n/m, n%m
}

func main (){
	var n int 
	fmt.Scan(&n)
	var m int 
	fmt.Scan(&m)

	var a,b string 
	fmt.Scan(&a,&b)

fmt.Println(add(n,m))
fmt.Println(swap(a,b))
fmt.Println(division(n,m))
}