N=int(input())
# sanguen_N=list(map(int,input().split()))
sanguen_N = set(map(int, input().split()))
#8개의 카드를 상근이 6개에 하나씩 비교하는거니까
#리스트보다 값 자체를 해시로 갖는 셋 집합이 좋음


M=int(input())
card=list(map(int,input().split()))

result=[]
for i in range(M):
    if(card[i] in sanguen_N):
        result.append(1)
        
    else:
        result.append(0)

print(" ".join(map(str,result)))
        

#         문제 10815번(숫자 카드)은 특정 숫자의 존재 여부를 확인하는 문제로, 집합(Set)을 사용하는 것이 일반적으로 리스트(List)보다 좋은 이유가 있습니다. 다음은 그 이유입니다:

# 중복된 숫자 처리: 문제에서는 숫자 카드를 중복해서 가지고 있을 수 있습니다. 즉, 동일한 숫자가 여러 장일 수 있습니다. 집합(Set)은 중복된 값을 허용하지 않기 때문에 중복된 숫자가 있을 때도 정확한 결과를 반환합니다. 반면, 리스트는 중복된 값이 있을 경우 직접 중복을 처리해야 하므로 코드가 더 복잡해집니다.

# 검색 속도: 집합(Set)은 해시 테이블과 같은 구조를 사용하여 요소의 존재 여부를 빠르게 확인할 수 있습니다. 따라서 Set을 사용하면 검색 속도가 빨라집니다. 리스트는 순차적으로 검색해야 하므로 검색에 걸리는 시간이 리스트의 크기에 비례하여 늘어날 수 있습니다.

# 코드 가독성과 간결성: 집합(Set)을 사용하면 코드가 더 간결하고 읽기 쉬워집니다. 순수하게 중복된 값을 처리하거나 검색하는 로직을 직접 작성할 필요가 없기 때문입니다.

# 요약하면, 집합(Set)을 사용하면 중복된 값 처리 및 검색 속도 면에서 이점이 있고, 코드도 간결해집니다. 따라서 숫자 카드 문제와 같은 존재 여부 확인 작업에는 집합(Set)을 사용하는 것이 일반적으로 더 좋은 선택입니다.