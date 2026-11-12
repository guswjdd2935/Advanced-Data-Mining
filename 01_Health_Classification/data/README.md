# Dataset

원본 CSV는 GitHub ZIP에 포함하지 않았습니다. Kaggle 대회 데이터의 재배포 가능 여부와 개인 식별자(`name`) 포함 가능성을 고려해 공개 저장소에 올리기 전 원 규정을 확인해야 합니다.

공식 대회: <https://www.kaggle.com/competitions/hbnu-adm-24-competition>

대회에서 다음 파일을 받아 이 폴더에 넣으세요.

```text
data/
├── README.md
├── train.csv              # 140,000 rows, 26 columns incl. health_status
├── test.csv               # 19,256 rows, 25 columns
└── sample_submission.csv  # index, health_status
```

**주의:** 이 파일들은 `.gitignore`에 등록되어 기본적으로 Git에 추가되지 않습니다. EDA 노트북의 그래프만 공개하며 `name` 열은 모델링에서 제외합니다.
