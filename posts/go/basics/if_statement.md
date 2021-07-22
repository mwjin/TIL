---
layout: default
title: If statement
parent: Basics
grand_parent: Go
nav_order: 4
---
# If statement
* If 문의 개념 및 용법 자체는 타 언어와 같다.
* 이 문서에서는 Go 만이 가지고 있는 용법 또는 알아두면 좋은 개념을 위주로 서술한다.

## Grammar
### Basics
* 일반적인 용법은 다음과 같다.
    ```go
    if cond1 {
        ...
    } else if cond2 {
        ...
    } else {
        ...
    }
    ```
* Go 언어는 문법을 강제하고 있어 위의 형태를 그대로 유지해야 한다.
* 단 else if, else 문은 필요치 않다면 쓰지 않아도 된다.
* 위의 `cond` 자리에는 일반적인 logical operation이 들어간다.

### if 초기문; 조건문
* Go에서는 특이하게 변수 선언문과 조건문을 동시에 사용할 수 있다.
* 용법은 다음 예시와 같다.
    ```go
    if n := GetNum(); n > 10 {
        ...
    } else if n > 5 {
        ...
    } else {
        ...
    }
    ```
* if 문에서 초기화 한 변수의 scope는 if ... else block 까지이다.

## Conditional statement
* 앞서 언급하였듯이 일반적인 logical operation, 즉 결과값이 boolean 인 경우 사용 가능하다.
  * (Python 처럼 boolean 이 아니더라도 허용해주는 경우가 있는지 잘 모르겠다.)
* C와 같이 AND는 `&&`, OR는 `||`임을 기억하자.
* **Short-circuit**
  * AND의 경우 연산의 특정 expresion이 False인 경우 그 뒤의 expression에 대한 검사는 진행하지 않는다.
  * OR의 경우 연산의 특정 expression이 True인 경우 그 뒤의 expression에 대한 검사는 진행하지 않는다.