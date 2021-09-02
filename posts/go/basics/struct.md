---
layout: default
title: Struct
parent: Basics
grand_parent: Go
nav_order: 3
---
# struct
## Basic
* 다양한 종류의 data type들을 맴버 (또는 필드)로서 포함할 수 있는 data type.
* C의 struct와 거의 동일한 개념이다.
* Go에서는 다음과 같은 방식으로 struct를 정의한다.
    ```go
    type Person struct {
        name        string
        age         int
        languages   []string
    }
    ```
* 위와 같이 정의하고 나면 다음과 같은 방식으로 struct type의 변수를 초기화 할 수 있다.
    ```go
    // Implicit field declaration
    person1 := Person{"Minwoo Jeong", 26, []string{"Python", "C", "Go"}}

    // Explicit field declaration
    var person2 Person
    person2.name = "John"
    person2.age = 15
    person3.languages = []string{"C++", "Python"}

    // Or
    person3:= Person{
		name:      "Anonymous",
		age:       15,
		languages: []string{"Java", "Javascript"}}
    ```
* Go의 private 인지 public 인지 판단하는 규칙은 struct의 필드명에도 적용된다.
    * 필드명이 소문자이면 private, 필드명의 첫번째 글자가 대문자이면 public.
    * 따라서 위의 예시에 이어 다음과 같은 접근 방식은 불가능하다.
    ```go
    // In other package...
    personName := person1.name  // Impossible!
    ```

## 구조체를 포함하는 구조체
* 구조체 정의 시 또 다른 구조체를 포함시킬 수 있다.
* 구조체를 포함할 수 있는 방법은 크게 두 가지가 있다.
    * 내장 타입
        ```go
        type Location struct {
            city        string
            distinct    string
        }
        type Person struct {
            name        string
            age         int
            location    Location
        }
        ```
    * 포함된 필드
        ```go
        // 위와 같은 Location 정의 방식
        type Person struct {
            name    string
            age     int
            Location
        }
        ```
        * 이 경우 Person type의 변수에서 Location의 필드값에 접근할 때 `.`를 한 번만 써도 접근이 가능하다.
        * 마치 `Location`의 필드가 모두 `Person`에 포함되는 것과 유사하다.
        * 단 두 구조체 사이 **중복된 필드**가 있는 경우 `변수.구조체.필드` 와 `변수.필드` 와 같은 방식으로 구분해야 한다.

## 구조체 크기
* C와 같은 방식으로 구조체의 크기가 결정된다.
* 특정 필드의 크기가 n byte인 경우, n의 배수에 해당하는 메모리 주소에 해당 필드의 값이 위치한다. 이는 컴퓨터가 데이터에 효과적으로 접근하기 위한 **메모리 정렬** 방식이다.
* 위 규칙을 유지하기 위해 메모리 상에서 필드값 뒤에 빈 공간이 padding 되는 경우가 존재한다.
* 이러한 규칙 때문에 필드를 어떻게 정렬하는가에 따라 구조체의 크기가 바뀔 수 있으니 유의해야 한다.
    ```go
    type t1 struct {
        n1 int8
        n2 int
        n3 int8
    }  // 24 bytes

    type t2 struct {
        n1 int8
        n2 int8
        n3 int
    }  // 16 bytes
    ```

## Constructor
* 인자값을 바탕으로 struct type 변수를 정의하여 반환하는 함수.
* 다른 객체 지향 언어에서의 class constructor와 유사한 역할이다.
* Go에서 강제하는 형태가 따로 존재하지 않기 떄문에 여러 방식으로 정의가 가능하다.
* Go에서는 struct type의 변수를 만들 때 직접적으로 struct를사용하는 것보다 constructor pattern을 이용해서 정의하는 것을 권장한다.
* Constructor는 다음과 같이 정의한다.
    ``` go
    // Return the local variable address
    func NewPerson(name string, age int, languages []string) *Person {
        p := Person{
            name:       name,
            age:        age,
            languages:  languages
        }
        return &p
    }
    
    // or
    // Allocate memory in the heap memory
    func NewPerson(name string, age int, languages []string) *Person {
        p := new(Person)
        p.name = name
        p.age = age
        p.languages = languages
        return p
    }
    ```
* [Effective Go](https://golang.org/doc/effective_go#composite_literals)에 따르면, Go에서는 C와는 달리 첫번째 constructor처럼 함수 내의 local variable address를 return 하는 형태가 허용된다.

## Methods
* Go의 struct에 대해서도 다른 객체 지향 언어의 class 처럼 method를 정의할 수 있다.
* 일반적인 Go 언어의 함수들과는 달리 정의 단계에서 **Receiver**를 명시한다.
    ```go
    func (p Person) GetName() {
        return p.name;
    }
    ```
    위 정의에서 ``` (p Person) ``` 에 해당하는 부분을 receiver 라고 한다.
    
* 위와 같이 정의한 후 다음과 같이 사용한다.
    ```go
    personName := person1.GetName()
    ```
* Method를 이용해서 private field의 값에 접근(getter)하거나 변경(setter)할 수 있다.
* Go에서는 이와 같은 method pattern을 권장한다.

### Receiver
* Receiver는 크게 두 가지 타입이 있다.
  * Value receiver
  * Pointer receiver
* Pointer receiver는 receiver로 받아 오는 변수의 type이 pointer로 명시되어 있다.
    ```go
    // Value Receiver
    func (p Person) GetName() {...}

    // Pointer Receiver
    func (p *Person) SetName(string name) {...}
    ```
* Value, pointer receiver는 대상이 되는 객체를 각각 call-by-value, call-by-reference로 불러온다.
* 때문에 단순한 객체의 값을 참조하는 method를 정의하고자 할 때는 value receiver를, 객체 내의 값을 변경하는 method를 정의하고자 할 때는 pointer receiver가 적절하다.

## 추가적으로 알아야 할 것
* Go에서는 왜 함수 내 local variable의 주소를 return 해도 괜찮은가?
