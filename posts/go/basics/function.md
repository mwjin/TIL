---
layout: default
title: Function
parent: Basics
grand_parent: Go
nav_order: 4
---

# Function

* 함수에 대한 기초적인 경험은 일반적인 프로그래밍 언어와 같다.
* 본 문서에서는 Go만이 가지고 있는 특징을 중심으로 서술한다.

## Grammars

### Basics

* 일반적인 정의는 다음 예시와 같은 형식을 따른다.

    ```go
    func Add(a int, b int) int {
        return a + b
    }
    ```

* 여러 parameter가 같은 type인 경우 다음과 같이 parameter 명시 부분을 줄일 수 있다.

    ```go
    func Add(a, b int) int {
        return a + b
    }
    ```

* 다음과 같이 return type을 명시하는 곳에 변수를 선언할 수도 있다.

    ```go
    func Add (a, b int) (result int) {
        result = a + b
        return
    }
    ```

### Multiple return values

* 다음과 같이 여러 개의 값을 return 할 수 있다.

    ```go
    func Divide(a, b int) (int, int) {
        q := a / b
        r := a % b
        return (q, r)
    }
    ```

* 위와 같은 경우 다음과 같이 return type을 명시하는 자리에 변수명도 같이 명시할 수 있다.

    ```go
    func Divide(a, b int) (q int, r int) {
        q = a / b
        r = a % b
        return
    }
    ```
