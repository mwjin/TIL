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
    * 입력값 간 공백을 삽입하거나 개행 문자를 삽입하지 않는다.
  * `fmt.Println()`
    * `fmt.Print()`와 같이 함수의 입력값들을 표준 서식에 맞추어 출력한다.
    * 그러나 입력값 간 공백 삽입, 호출 시 맨 뒤에 개행 문자를 삽입한다는 차이점이 있다.
  * `fmt.Printf()`
    * 유저가 지정한 format에 맞추어 입력값들을 출력한다.
    * C의 printf와 유사하다.

* 사용법 예시
    ```go
    var a int = 10
    var b string = "Hello"
    var c float64 = 3.141592
    fmt.Print(a, b, c)
    fmt.Println(a, b, c)
    fmt.Printf("a: %d, b: %s, c: %f", a, b, c)
    ```

