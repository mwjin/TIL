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

## Variable
### Local
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
### Global
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
* 이름처럼 값이 바뀌지 않는 객체.
* ``var`` 키워드 대신 ``const`` 키워드를 붙여 정의
* Character, string, boolean, 또는 숫자들에 대해 사용 가능.
* Local, global 관계 없이 다음과 같이 정의할 수 있다.
    ```go
    const const_n int = 3

    // or
    const const_n = 3
    ```
* ``const``로 선언된 객체는 반드시 명시적으로 initialize 해야 한다.
* ``:=``를 사용할 수 없다.
