---
layout: default
title: Switch Statement
parent: Basics
grand_parent: Go
nav_order: 5
---
# Switch statement
## Concept
* C언어와 같이 특정 변수의 값에 따라 다른 로직을 수행하는 구문.
* 문법은 C언어와 비슷하나 Go가 더 간단해보인다.

## Grammar
* 일반적인 문법은 다음과 같다.
    ```go
    switch yourValue {
    case value1:
        ...
    case value2:
        ...
    default:
        ...
    }
    ```
* `default`는 생략 가능하다.
* C와는 달리 `break`를 명시적으로 할 필요가 없다.
  * 일반적인 케이스에서 `break` 없이도 case문 하나만 실행한 후 switch 문을 빠져나온다.
* 하나 이상의 값에 대해 같은 동작을 할 때는 다음과 같이 작성한다.
    ```go
    switch yourValue {
    case value1 , value2:
        ...
    case value3, value4, value5:
        ...
    }
    ```
* 다음과 같이 작성하면 `true` 값을 가지는 case 문에 값 대신 조건문을 넣을 수 있다.
    ```go
    switch true {
    case a > 10 && b < 20:
        ...
    case a <= 10:
        ...
    default:
        ...
    }
    ```
    위 case 문 중 가장 먼저 `true`가 되는 case 문을 실행한뒤 switch 문을 빠져 나온다. 
* `switch true {}`는 `switch {}`와 같이 `true`를 생략해서 작성 가능하다.
* if 문과 유사하게 switch 문법에서도 어떤 변수에 대한 init statement를 삽입할 수 있다.
    ```go
    switch a := b + 10, a {
    case value:
        ...
    }
    ```
    * 위의 `a`와 같이 switch block 내에서 정의된 변수의 scope는 switch 문 한정이다.
* 다음과 같이 const 열거값 (enum)과 switch 문을 함께 사용하면 가독성 좋은 코딩이 가능하다.
    ```go
    type Alphabet int
    const (
        A Alphabet := iota
        B
        C
        D
    )

    ...
    
    func main() {
        score Alphabet = D;
        switch score {
        case A:
            ...
        case B:
            ...
        ...
        }
    }
    ```
* Switch 문 내의 여러 case에 대해 동일한 동작을 수행하고 싶은 경우에는 `fallthrough` 키워드를 사용할 수 있다. 
  * 그러나 코드의 가독성 상 사용을 권하진 않는다.
