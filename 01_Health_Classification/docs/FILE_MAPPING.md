# 원본 파일 → 정리 후 파일

원본 압축파일 `ADM project.zip`에서 건강상태 분류 프로젝트와 관련된 대표 노트북만 선별했습니다. 아래 원본 파일은 원래 코드가 보존되도록 셀의 실행 출력만 제거했습니다.

| 원본 위치 | 새로운 위치 | 원본 크기 → 정리 후 크기 |
|---|---|---|
| `hbnu-adm-24-competition/feature_engineering.ipynb` | `notebooks/02_Feature_Engineering_2024.ipynb` | 49,309 KB → 12 KB |
| `hbnu-adm-24-competition/logisicv3.ipynb` | `notebooks/03_Logistic_Regression_2024.ipynb` | 54 KB → 20 KB |
| `hbnu-adm-24-competition/randomforest(0.8465).ipynb` | `notebooks/04_Random_Forest_2024.ipynb` | 39 KB → 7 KB |
| `hbnu-adm-24-competition/boosting(0.85538).ipynb` | `notebooks/05_LightGBM_2024.ipynb` | 2,037 KB → 8 KB |
| `hbnu-adm-24-competition/xgboost.ipynb` | `notebooks/06_XGBoost_2024.ipynb` | 44 KB → 10 KB |
| `보고서용 /boost3_ensemblever2.0.ipynb` | `notebooks/07_Bayesian_Tuning_and_Ensemble_2024.ipynb` | 9,364 KB → 20 KB |
| `보고서용 /xgb&lgb_ensemble.ipynb` | `notebooks/08_Ensemble_Experiments_2024.ipynb` | 6,113 KB → 19 KB |
| `보고서용 /baseline.ipynb` | `notebooks/archive_2024/Original_EDA_and_Baseline.ipynb` | 2,936 KB → 17 KB |
| `hbnu-adm-24-competition/feature_selection.ipynb` | `notebooks/archive_2024/Feature_Selection_Exploration.ipynb` | 56 KB → 5 KB |

## 현재 GitHub용 묶음에서 제외한 파일

- `lec/`, `code/`: 강의자료·일반 수업 실습 파일(대회 결과와 분리).
- `adm-24-hackathon/`, `해커톤/`: 다음에 정리할 다른 프로젝트.
- `__MACOSX`, `.DS_Store`: 운영체제 메타데이터.
- `hbnu-adm-24-competition`의 여러 복사본/시험 버전: 전체를 중복 업로드하지 않고 대표 코드만 선별. 원본 ZIP은 개인 보관 추천.
- `ADM-kaggle_20231052...pptx`: 발표자료에는 개인 식별 정보가 들어 있어 공개 GitHub용 ZIP에서 제외. 발표 핵심 내용은 README와 `EXPERIMENT_NOTES.md`에 반영.
- 원본 `train.csv`, `test.csv`: 재배포 및 개인 식별자 검토 전까지 제외.
