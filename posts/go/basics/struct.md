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
    personName := person1.name  // Impossible!
    ```

## 추가해야 할 목록
* struct의 contructor
* struct의 method와 receiver의 개념