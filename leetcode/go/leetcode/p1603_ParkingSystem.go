package leetcode

type ParkingSystem struct {
	parkPos [4]int
}

func ConstructorParkingSystem(big int, medium int, small int) ParkingSystem {
	return ParkingSystem{[4]int{0, big, medium, small}}
}

func (this *ParkingSystem) AddCar(carType int) bool {
	if carType > 3 || carType < 1 {
		return false
	}
	if this.parkPos[carType] > 0 {
		this.parkPos[carType] -= 1
		return true
	}
	return false
}
