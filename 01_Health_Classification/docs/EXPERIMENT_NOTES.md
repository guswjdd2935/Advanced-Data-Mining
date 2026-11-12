# 실험 과정 및 재현 시 주의사항

## 2024년 기록에서 확인한 내용

1. **데이터 탐색(EDA)**: Train/Test 상관계수 비교, 변수별 분포/상관관계 탐색.
2. **파생 변수(Feature Engineering)**: 체격, 지질/콜레스테롤, 철분, 효소 변수 조합 등 다양한 파생 변수 실험.
3. **Feature Selection**: LightGBM 기반 중요도/변수 제거 실험.
4. **기초 모델 비교**: Logistic Regression, Decision Tree, Random Forest 등을 포함한 여러 모델 비교.
5. **최종 후보**: XGBoost, LightGBM, CatBoost. 모델별 BayesSearchCV 50회 탐색(`cv=3`, `scoring='roc_auc'` 확인).
6. **앙상블**: Stacking, 규칙 기반 확률 결합, 가중치 기반 soft voting 비교. 발표 슬라이드에 최종 제출 **XGB:LGB:CAT=6:2:2**, 늦은 추가 제출 **8:1:1** 기록.

## 로그에 남아 있는 CV 성능

| 모델 | Best CV ROC-AUC | 근거 |
|---|---:|---|
| XGBoost | 0.868 | `results/metrics/xgb_bayesver2.0.txt` |
| LightGBM | 0.866 | `results/metrics/lgbm_bayesver2.0.txt` |
| CatBoost | 0.866 | `results/metrics/catboost_bayesver2.0.txt` |

값은 실험 로그에 3자리로 반올림되어 있습니다. 이는 **교차검증 결과**이지 Kaggle Public/Private 점수가 아닙니다.

## 점검 사항 — 삭제하거나 임의로 보정하지 않고 기록

- 초기 노트북은 실행 순서, 반복 셀, 하드코딩 경로 및 여러 파일 덮어쓰기 문제 등이 있어 모두 독립적으로 실행되는 최종 파이프라인이라고 보장할 수 없습니다.
- 원본 코드 중 `waist_to_age_ratio = df['midsection_inch'] / 2024-df['birth']`는 연산자 우선순위상 예상과 다른 계산이 될 수 있습니다. 2024 실험을 정확히 재현하려면 먼저 의도를 확인해야 합니다.
- 원본의 `bmi = mass_kg / ((stature_inch + 100) / 100)**2`는 `stature_inch`라는 열 이름에 비춰 단위 및 의미를 재확인할 필요가 있습니다. 이번 정리에서는 원본 코드를 임의로 수정하지 않았습니다.
- 저장된 개별 모델 예측 파일(`xgb_prediction.csv`, `lightgbm_prediction.csv`, `catboost_prediction.csv`)로 8:1:1을 계산하면 저장된 `late_weight_8_1_1_original.csv`에 부동소수 오차 범위로 재현됩니다. **6:2:2와 4:3:3 원본 제출물은 현재 보관된 개별 모델 예측 파일을 단순 가중합한 것과 정확히 일치하지 않습니다.** 다른 모델 버전 또는 제출 시점 차이 가능성이 있으나, 증거 없이 원인을 단정하지 않습니다.
- 노트북 27번 셀에는 2024-12-08의 '대시보드 기준' 메모로 규칙 기반 0.85510, 스태킹 0.85625, 가중치 0.85772가 있습니다. Public/Private 구분 및 어떤 제출과 연결되는지 확실하지 않아 README의 최종 공식 점수로 사용하지 않았습니다.
- **3위**는 프로젝트 작성자가 제공한 결과입니다. 공식 종료 당시 순위 캡처가 있으면 README의 근거 자료로 추가하면 좋습니다.
- 원 데이터에 있는 `name` 열은 개인 식별 가능성이 있으므로 공개 저장소에서 원본 데이터를 기본 제외했습니다.

## 재정리 과정에서 새로 만든 자료

- `notebooks/01_EDA.ipynb`: 2026년 데이터 검토를 통해 구성한 EDA 노트북. 2024년 원본이 아님.
- `results/figures/*.png`: 위 EDA 노트북을 현재 데이터로 다시 실행해 생성한 그래프.
- `src/ensemble.py`: 기존 모델별 예측 CSV를 가중합하는 간단한 재현 도구. **모델 재학습 스크립트가 아님**.

기존 노트북은 **2024년 작성 코드의 소스는 유지하되, 커다란 실행 출력과 불필요한 위젯 메타데이터만 제거**했습니다. `data`가 없는 상태에서는 원본 학습 노트북을 바로 실행할 수 없습니다.
