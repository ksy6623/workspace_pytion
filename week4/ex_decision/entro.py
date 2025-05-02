import numpy as np

def calculate_entropy(probabilities):
    # 엔트로피 계산
    entropy = -np.sum(probabilities * np.log2(probabilities))
    return entropy

# 예시 확률 분포 (각 사건의 발생 확률)
probabilities = np.array([0.5, 0.5])  # 두 사건이 동일한 확률로 발생할 때
entropy_value = calculate_entropy(probabilities)

print(f"엔트로피 값: {entropy_value:.4f}")
