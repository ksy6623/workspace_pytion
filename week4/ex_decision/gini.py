from fractions import Fraction
# Fraction 분수
def gini_index_fraction(probabilities):
    return 1 - sum(p ** 2 for p in probabilities)

# 예제
# 첫 번째 예제: 클래스 확률이 고르게 분포된 경우 (높은 이질성)
probabilities_1 = [Fraction(3, 8), Fraction(3, 8),  Fraction(1, 8), Fraction(1, 8)]
gini_1 = gini_index_fraction(probabilities_1)
print("첫 번째 예제 지니 지수 (분수):", gini_1)
print("첫 번째 예제 지니 지수 (실수):", float(gini_1))

# 두 번째 예제: 한 클래스의 확률이 높은 경우 (낮은 이질성)
probabilities_2 = [Fraction(7, 8), Fraction(1, 8)]
gini_2 = gini_index_fraction(probabilities_2)
print("두 번째 예제 지니 지수 (분수):", gini_2)
print("두 번째 예제 지니 지수 (실수):", float(gini_2))