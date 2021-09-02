---
layout: default
title: Input and Output
parent: Basics
grand_parent: Go
nav_order: 3
---

# Input and Output

## Introduction

* Go에서 입출력을 위해 주로 사용하는 라이브러리는 `fmt`이다.
* 본 문서에서는 이 라이브러리에서 기본적으로 사용되는 함수들에 대해 설명한다.

## Output

* 크게 세 가지 함수가 있다.
  * `fmt.Print()`
    * 함수의 입력값들을 호출한다.
    * 기본 서식에 맞추어 표준 출력한다.
    * 입력값 사이에 아무것도 삽입하지 않는다.
    * 개행 문자도 삽입하지 않는다.
  * `fmt.Println()`
    * `fmt.Print()`와 같이 함수의 입력값들을 표준 서식에 맞추어 출력한다.
    * 입력값 간 공백을 삽입한다.
    * 결과 맨 뒤에 개행 문자를 삽입한다.
  * `fmt.Printf()`
    * 유저가 지정한 format에 맞추어 입력값들을 출력한다.
    * C의 `printf()`와 유사하다.

* 사용법 예시
 
  ```go
  var a int = 10
  var b string = "Hello"
  var c float64 = 3.141592
  fmt.Print(a, b, c)
  fmt.Println(a, b, c)
  fmt.Printf("a: %d, b: %s, c: %f\n", a, b, c)
  ```

* 결과 예시

  ```bash
  10Hello3.14159210 Hello 3.141592
  a: 10, b: Hello, c: 3.141592
  ```  

## Input

* 크게 세 가지 함수가 있다.
  * `fmt.Scan(a ...interface{}) (n int, err error)`
    * 표준 입력에서 값을 받는다.
    * Output은 성공적으로 입력받은 값 개수, 에러이다.
    * 예시

      ```go
      package main

      func main() {
        var a int
        var b int

        n, err := fmt.Scan(&a, &b)
        if err != nil {
          fmt.Println(n, err)
        } else {
          fmt.Println(n, a, b)
        }
      }
      ```

    * 위 프로그램을 실행하면 integer 두 개가 입력되거나 integer가 될 수 없는 다른 데이터를 입력할 때 까지 종료되지 않는다.
    * Integer가 아닌 값이 입력되는 경우 `expected integer` 에러와 함께 종료된다.
    * 두 integer 간의 구분은 공백, 개행 문자 같은 whitespace이다.
    * 결과 예시

      ```bash
      3 4                 # input 1
      2 3 4               # output 1
      Hello 4             # input 2
      0 expected integer  # output 2
      4 Hello             # input 3
      1 expected integer  # output 3
      ```
  
  * `fmt.Scanf(format String, a ...interface{}) (n int, err error)`
    * 표준 입력에서 서식 형태로 값을 입력받는다.
    * String으로 명시한 format을 맞추지 않으면 에러가 발생한다.
    * 예시

      ```go
      // 위의 예시에서 Scan 호출 statement를 아래의 statement로 교체
      n, err := fmt.Scanf("%d %d\n", &a, &b)
      ```

    * 결과 예시

      ```bash
      # Scan 함수 결과 예시와는 동일한 결과 출력
      1                                         # input 1
      1 newline in input does not match format  # output 2
      1h                                        # input 2
      1 expected space in input to match format # output 2
      ```

      위와 같이 format과 맞지 않는 경우 경우에 맞는 에러가 출력된다.

  * `fmt.Scanln(a ...interface{}) (n int, err error)`
    * 표준 입력에서 한 줄을 읽어 값을 입력받는다.
    * `Enter`키를 누르면 입력이 종료된다.
    * 예시

      ```go
      // 위의 예시에서 Scanf 호출 statement를 아래의 statement로 교체
      n, err := fmt.Scanln(&a, &b)
      ```

    * 결과 예시

      ```bash
      # Scan 함수 결과 예시와는 동일한 결과 출력
      1                     # input 1
      1 unexpected newline  # output 2
                            # input 2
      0 unexpected newline  # output 2
      ```

  * 사용 시 유의 사항
    * 위의 함수 사용 시 갑작스러운 에러 발생으로 인해 모든 입력을 다 읽지 못한 경우 표준 입력 스트림에 아직 입력한 값이 남아 있게 되는 문제가 있다.
    * 이를 방지하기 위해 `bufio.NewReader`, `os.Stdin` 객체를 이용해 다음과 같이 에러 발생 시 표준 입력 스트림을 읽어주는 작업을 진행할 것을 권한다.

      ```go
      package main

      import (
        "bufio"
        "fmt"
        "os"
      )

      func main() {
        stdin := bufio.NewReader(os.Stdin)

        var a int
        var b int

        n, err := fmt.Scanln(&a, &b)
        if err != nil {
          fmt.Println(n, err)
          stdin.ReadString('\n')
        } else {
          fmt.Println(n, a, b)
        }
      }
      ```
