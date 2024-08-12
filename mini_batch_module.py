import numpy as np

# 미니 배치 생성 함수 정의
def create_mini_batches(X, y, batch_size):
    mini_batches = []
    data = np.array(X)
    labels = np.array(y)
    
    # 데이터와 레이블을 결합한 후 섞기
    combined = np.column_stack((data, labels))
    np.random.shuffle(combined)

    # 미니 배치 생성
    for i in range(0, len(combined), batch_size):
        mini_batch = combined[i:i + batch_size]
        mini_batches.append((mini_batch[:, :-1], mini_batch[:, -1]))  # 특성과 레이블 분리
        
    return mini_batches
