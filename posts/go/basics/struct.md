---
layout: default
title: struct
parent: Basics
grand_parent: Go
nav_order: 1
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
* 위와 같이 정의하고 나면 다음과 같은 방식으로 struct type의 변수를 정의할 수 있다.
    ```go
    // Implicit field declaration
    person1 := Person{"Minwoo Jeong", 26, []string{"Python", "C", "Go"}}

    // Explicit field declaration
    person2 := Person{
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

## 추가해야 할 목록
* struct의 method와 receiver의 개념

## 추가적으로 알아야 할 것
* Go에서는 왜 함수 내 local variable의 주소를 return 해도 괜찮은가?