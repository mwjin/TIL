---
layout: default
title: Minimum Spanning Tree
parent: Greedy Algorithms
nav_order: 1
---
# Minimum Spanning Tree
### 문제 상황
* 프로그래머스에서 최소한의 다리 건설 비용으로 모든 섬을 연결하는 문제를 풀었다.
* 문제를 풀 때는 어찌저찌 생각해서 풀었으나 실제로 이 문제는 **Minimum Spanning Tree (MST)** 라는 아주 유명한 문제였다.
* MST 문제는 특정 조건 하에 greedy algorithm을 통해 풀 수 있다는 사실이 알려져 있다.
* 이와 관련된 알고리즘을 간략하게 나마 정리하였다.

### Prim Algorithm
* 다음과 같은 과정을 통해 MST를 찾는 알고리즘이다.
*1. 임의의 점 하나를 택한다.
*2. 이 점과 연결된 선들 중 최소의 가중치를 가진 선을 택한다.
*3. 이 선과 연결된 점을 포함시킨다.
*4. 포함된 점들과 연결된 선들 중 최소의 가중치를 가진 선을 택한다.
*5. 3, 4 과정을 반복한다.
*6. 위의 과정을 수행할 때 Cycle이 형성되지 않도록 이미 포함된 점들끼리 연결한 선은 택하지 말아야 한다.
* 점의 개수를 n이라 할 때, 각 점에서 최소의 가중치를 가진 선을 찾는 과정의 time complexity는 *O(n)*.
* 최소 가중치를 가진 선을 찾는 과정을 각 점에 대해서 반복하므로 이 알고리즘의 time complexity는 *O(n^2)*.

### Kruskal Algorithm
* 다음과 같은 과정을 통해 MST를 찾는 알고리즘이다.
*1. 모든 선에 대해 가중치를 기준으로 ascending order로 sorting 한다.
*2. 가중치 순서대로 선을 spanning tree에 포함시킨다.
*3. 단, 2의 과정에서 선을 포함시켰을 때 cycle이 형성되는 경우 이를 제외한다.
*4. Cycle 형성은 포함시키고자 하는 선의 양쪽 점이 현재 같은 집합(이미 연결되어 있는 점을 나타냄)에 포함되어 있는지 여부를 통해 확인할 수 있다.
* 선의 개수를 E라 할 때, 선의 가중치를 기준으로 sorting하고 linear 하게 선들을 scan하므로 time complexity는 *O(ElogE)*.

### 두 알고리즘의 비교
* 위의 time complexity 식을 대략적으로 봤을 때 dense 한 그래프일 경우 Prim, 그렇지 않은 경우 Kruskal이 더 유리할 것임을 예측할 수 있다.
* 실제로 좀 더 solid 한 기준이 있는지 확인이 필요하다.

### 더 확인해봐야 할 것
* Greedy algorithm을 적용할 수 있는 조건 및 이유
* 구체적인 time complexity를 구하는 방법
* Kruskal에서 cycle이 형성되는지 여부를 판단할 수 있는 구체적인 방법
* N개의 item을 sorting 하는 경우 time complexity가 일반적으로 O(NlogN)인 이유
* 두 알고리즘 중 무엇을 사용할 지 결정할 수 있는 구체적인 방법
