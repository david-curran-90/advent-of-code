package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func chkErr(err error) {
	if err != nil {
		panic(err)
	}
}

func checkNoDupe(buff string) bool {
	var match int
	for _, s := range buff {
		if strings.Count(buff, string(s)) > 1 {
			match++
		} else {
			match = match
		}
	}
	if match != 0 {
		return false
	} else {
		return true
	}
}

func readInput(file string) string {
	input, err := ioutil.ReadFile(file)
	chkErr(err)
	return fmt.Sprintf("%s", input)
}

func trimFirstChar(s string) string {
	for i := range s {
		if i > 0 {
		  return s[i:]
		}
	}
	return s[:0]
}

func addToString(buff, char string, num int) string {
	if len(buff) < num {
		buff = buff + char
	} else {
		buff = trimFirstChar(buff)
		buff = buff + char
	}
	return buff
}

func lookForMarker(num, c int, buff string) int {

	if len(buff) == num {
		if checkNoDupe(buff) {
			count := c + 1
			return count
		}
	}
	return 0
}

func main() {
	// open file and save to string
	var startofmsg int
	var startofpkt int
	var buff string
	input := readInput("input.txt")
	chars := []rune(input)
	for c := 0; c < len(chars); c++ {
		num := 4
		char := string(chars[c])
		buff = addToString(buff, char, num)
		if len(buff) == num {
			startofpkt = lookForMarker(num, c, buff)
			if startofpkt > 0 {
				break
			}
		}
	}
	for c := 0; c < len(chars); c++ {
		num := 14
		char := string(chars[c])
		buff = addToString(buff, char, num)
		if len(buff) == num {
			startofmsg = lookForMarker(num, c, buff)
			if startofmsg > 0 {
				break
			}
		}
	}
	fmt.Printf("Packet starts at: %d\n", startofpkt)
	fmt.Printf("Message starts at: %d\n", startofmsg)
}
