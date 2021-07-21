---
layout: default
title: Variable and Constant
parent: Basics
grand_parent: Go
nav_order: 2
---
# Variable and Constant
## Basic
* Go는 정적 타입 언어이다.
* 일반적으로 변수 또는 상수 선언 시 타입 명시를 꼭 해줘야 한다.
* 그러나 변수에 대해 타입을 명시하지 않아도 컴파일러가 알아서 유추해주는 경우도 있다.
* Go는 **강타입 언어**이다.
    * 암묵적인 type conversion을 허용하지 않는다.
    * Type conversion을 위해서는 `type()` 형태의 함수를 사용해야 한다.
    * e.g. `int()`, `float64()` 
## Variable
### 정의 및 특징
* 실행 중 값이 변할 수 있는 객체.
* *값, 이름, 타입, 메모리 주소* 이렇게 4가지 속성을 가진다.
* Scope에 따라 *local variable*, *global variable*로 분류할 수 있다.
### Local variable 정의 방법
* 가장 정석인 방법은 아래와 같이 변수를 정의하는 것이다.
    ```go
    var n int   // Declare
    n = 7       // Initialize
    ```
* 위의 과정을 아래와 같이 합칠 수도 있다.
    ```go
    var n int = 7
    ```
* 다음과 같이 타입 없이도 선언 및 초기화가 가능하다.
    ```go
    var n = 7
    ```
* ``:=``를 이용하면 다음과 같이 가장 간단하게 선언 및 초기화가 가능하다.
    ```go
    n := 7
    ```
* 타입을 명시하지 않더라도 이미 정해진 변수의 타입은 다시 바꿀 수 없다.
* 다음과 같이 여러 개 동시에 선언도 가능하다.
    ```go
    var a, b int
    a = 1
    b = 2
    ```
* 변수 선언의 여러 가지 형태 예시
    ```go
    package main

    import "fmt"

    func main() {
        var a int = 3
        var b int
        var c = 4
        d := 5

        fmt.Println(a, b, c, d)
    }
    ```
### Global variable 정의 방법
* Function body 외에서 정의되는 variable (global variable)은 다음과 같이 무조건 선언문으로서 작성될 수 있다.
    ```go
    var global_n int = 3

    // or
    var global_n = 3

    // Without init (type must be specified)
    var global_n int
    ```
* 다음과 같이 global context에서 작성되어 있는 경우 컴파일 에러 발생한다.
    ```go
    // syntax error: non-declaration statement outside function body
    var global_n int
    global_n = 3

    // syntax error: unexpected newline, expecting type
    var global_n
    ```

* 다음과 같이 여러 개의 global variable을 선언할 수 있다.
    ```go
    var (
        a = 1
        b = 2
        c = 3
    )
    ```

## Constant
### 정의
* 이름처럼 값이 바뀌지 않는 객체.
* ``var`` 키워드 대신 ``const`` 키워드를 붙여 정의

### 특징
* 정수, 실수, 문자와 같은 **기본 타입 (Primitive type)만 상수로 정의할 수 있다.**
* 구조체, 배열 등 기본 타입이 아닌 경우 (Complex type) 상수로 정의할 수 없다.
* Variable과 달리 메모리 주소값에 접근할 수 없다. 따라서 3가지 속성만 가진다.

### 정의 방법
* Local, global 관계 없이 다음과 같이 정의할 수 있다.
  * 전자는 type 있는 상수, 후자는 type 없는 상수이다.
  * Type 없는 상수의 경우 **변수에 값이 복사될 때 type이 결정**되기 때문에 여러 type으로 상수를 사용하고 싶을 때 유용하다.
    ```go
    const const_n int = 3

    // or
    const const_n = 3
    ```
  * ``const``로 선언된 객체는 반드시 명시적으로 initialize 해야 한다.
  * ``:=``를 사용할 수 없다.

### 사용 방법
* 두 가지 상황에서 주로 사용된다.
  * Runtime에 값이 바뀌지 않는 걸 보장하고 싶을 때
  * 특정 값에 이름을 부여하고 싶을 때 (Enum과 비슷한 느낌)
    ```go
    const (
        apple uint = 1
        orange uint = 2
        banana uint = 3
    )
    ```
  * `iota`를 이용해 더 간단하게 정의할 수 있다.
    ```go
    const (
        apple uint = iota + 1   // 0 + 1
        orange uint = iota + 1  // 1 + 1
        banana uint = iota + 1  // 2 + 1
    )
    // Or
    const (
        apple uint = iota + 1
        orange        
        banana
    )
    ```
    * `iota`는 소괄호를 넘어가면 초기화된다.

### Literal
* *고정된 값* 그 자체로 쓰인 문구
* 상수는 리터럴로 취급됨.
* 컴파일 단계에서 상수는 literal로 치환됨.
* 상수가 포함된 expression은 실제 컴파일 단계에서 계산이 이루어지고 결과값은 리터럴로 저장. -> 상수 표현식 계산에 CPU 자원이 쓰이지 않는 이유.
* Go 언어는 강타입 언어이기 때문에 일반적으론 다른 타입의 변수끼리 연산이 불가능하지만 상수를 이용하면 다음과 같이 가능하다.
    ```go
    const PI = 3.14
    var n int = PI * 100

    // Compile 단계에서 다음과 같이 변환
    var n int = 314
    ```
* 상수는 실행파일에 *값* 형태로 쓰이기 때문에 동적 할당 메모리 영역을 사용하지 않음.
    * 정확히는 literal의 형태로 *코드 영역* 에 올라간다.
    * 우리가 상수의 메모리 주소를 못 참조 하는 이유
