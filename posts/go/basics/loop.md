---
layout: default
title: Loop
parent: Basics
grand_parent: Go
nav_order: 7
---
# Loop
## Introduction
* Loop의 역할은 일반적인 다른 언어들과 같다.
* Go에서의 loop는 `for` 뿐이다.
* `for`로 `while` 과 같은 동작을 하게 할 수 있다.

## Grammar
### Basics
* 일반적인 용법은 다음과 같다.
    ```go
    for 초기문; 조건문; 후처리 {
        ...
    }

    // Example
    for i := 0; i < 5; i++ {
        ...
    }
    ```
### Advanced Usage
* 다음과 같이 초기문에 대한 생략이 가능하다.
    ```go
    for ; 조건문; 후처리 {
        ...
    }

    // Example
    i := 0
    for ; i < 5; i++ {
        ...
    }
    ```
    * 당연하게도 for 에서 사용하는 **변수에 대한 정의가 사전에 되어 있어야** 한다.

* 다음과 같이 후처리에 대한 생략이 가능하다.
    ```go
    for 초기문; 조건문; {
        ...
    }

    // Example
    for i := 0; i < 5; {
        ...
        i++
    }
    ```
    * 무한 루프를 빠져 나오기 위한 `break` 또는 후처리는 필수적이다.
    * 조건문 뒤에 `;`는 필수적이다.

* 다음과 같이 조건문, 후처리 둘 다 생략이 가능하다.
    ```go
    for ; 조건문; {
        ...
    }
    
    // Example
    i := 0
    for ; i < 5; {
        ...
        i++
    }
    ```
* 위의 경우 다음과 같이 간소화 하여 `;` 없이 작성할 수 있다.
    ```go
    for 조건문 {
        ...
    }
    ```
    * 위 용법은 다른 언어의 `while` 과 유사하다.

* 다른 언어와 마찬가지로 `break`, `continue` 사용이 가능하며 기능은 동일하다.

## 중첩 루프
* 다른 언어와 마찬가지로 한 `for` loop 안에 다른 `for` loop를 정의하여 사용할 수 있다.
* **Label**
    * `for` loop 정의 시 해당 loop 또는 중첩 loop에 대한 label을 정의할 수 있다.
        ```go
        MyFor:
            for i < 10 {
                ...
                for j < 20 {
                    ...        
                }
            }
        ```
    * 위와 같이 label을 정의하면 `break` 문을 이용해 그 label에 속한 가장 외곽의 loop 까지 한 번에 빠져 나올 수 있다.
        ```go
        MyFor:
            for i < 10 {
                ...
                for j < 20 {
                    ...
                    if j == 15 {
                        break MyFor
                    }
                }
            }
        ```
    * 코드의 가독성을 위해 남용하지 말 것!
