package main

import (
	"fmt"
	"strconv"
	"time"
)

var Ticker int

func getMsg(msgChan chan string) {
	msgId := 0
	for { //循环接收消息 最多10条堵塞
		msgId++
		msg := "cur msg id" + strconv.Itoa(msgId) + " ;time:" + time.Now().String()
		msgChan <- msg
		time.Sleep(10 * time.Microsecond)
	}
}

func handleMsg(taskId int, msgChan chan string) {
	for { //循环处理消息 每秒只能处理一个
		msg := <-msgChan
		fmt.Println("TaskHandle" + strconv.Itoa(taskId) + ":handle Msg" + msg)
		time.Sleep(2 * time.Second)
	}
}
func main() {

	msgChan := make(chan string, 10) //消息池 最多10条
	msgSet := make(chan string, 2)   // 临时消息 每次最多处理两个
	go getMsg(msgChan)               //开始接收消息
	for {                            //开始处理消息
		select {
		case <-time.After(3 * time.Second): //超过三秒
			fmt.Println("Over Time Task Must Do Now")
		}

		Ticker++
		fmt.Println(cap(msgChan))
		go handleMsg(Ticker, msgChan)
		time.Sleep(3 * time.Second) // 每个三秒进行一批次处理
	}

	//msgs := make([]string,10)
	//开启三个处理的协程
	/*for {
		msg := <-msgChan
		fmt.Println(msg)
		time.Sleep(1000 * time.Millisecond)
	}*/
	for { // 挂起主进程 防止退出
		time.Sleep(1 * time.Second)
	}

}
