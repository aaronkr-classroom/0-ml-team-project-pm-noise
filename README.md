[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/PFDbQZp_)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=16867045)
# 0-ml-team-projects

IPYNB notebooks for ML Team Projects

[팀 프로젝트 설명 PPT](https://docs.google.com/presentation/d/1NO6_B8HVeR5WoJuTJXMgTgmhxURlt-uzPia3qDSeYsU/edit?usp=sharing)

# 팀 프로젝트 GitHub 저장소 사용 안내

이 저장소는 팀 프로젝트를 위한 GitHub Classroom의 공동 작업 공간입니다. 모든 팀원들은 프로젝트 진행에 필요한 파일(보고서, 프로젝트 제안서, Jupyter Notebook 파일 등)을 이 저장소에 저장하고 공유해야 합니다. GitHub Codespaces를 통해 온라인 코딩 환경에서 직접 코드를 작성하고 실행할 수 있으며, 저장소를 통해 최신 버전의 파일을 공유할 수 있습니다.

## 저장소 사용 규칙

1. **프로젝트 파일 저장**:
   - 모든 프로젝트 파일과 작업 내용을 이 저장소에 저장합니다.
   - 폴더 구조와 파일 이름은 일관성 있게 관리하여 팀원들이 쉽게 찾을 수 있도록 합니다.

2. **작업 내용 추가 및 업데이트**:
   - 작업이 끝나면 새 파일을 저장소에 추가하거나 기존 파일을 업데이트합니다.
   - 변경 사항을 저장한 후에는 commit과 push 명령어를 통해 저장소에 반영해야 합니다.

3. **커밋 메시지 작성**:
   - 각 커밋에는 작업 내용을 명확히 설명하는 커밋 메시지를 작성합니다.
   - 예시: `README 파일 업데이트`, `데이터 전처리 코드 추가`, `모델 성능 평가 시각화 추가`

4. **팀원과 파일 공유**:
   - 코드나 파일을 새로 추가하거나 수정한 경우, 반드시 commit하고 push하여 팀원들이 변경 사항을 확인할 수 있도록 합니다.
   - 저장소를 통해 팀원들이 공동 작업을 효율적으로 수행할 수 있습니다.
  
---

## 파일 작업 순서 (VS Code 기준)

1. **변경 사항 저장**:
   - 파일에서 변경 작업을 완료한 후 `파일 → 저장`을 눌러 작업한 내용을 저장합니다.
   - 단순히 "저장"만 하면 로컬에만 반영되고, Git 저장소에 반영되지는 않습니다.

2. **커밋 (Commit)**:
   - 소스 제어 메뉴 상단에 변경 사항 설명을 입력합니다 (예: `EDA 코드 추가`).
   - 메시지를 입력한 후 `✔` 아이콘을 클릭하여 커밋을 완료합니다.

3. **푸시 (Push)**:
   - 커밋 후, 상단의 `…` 메뉴에서 `Push`를 선택하여 GitHub 원격 저장소에 변경 사항을 업로드합니다.
   - 푸시가 완료되면 다른 팀원들이 해당 변경 사항을 볼 수 있습니다.

4. **변경 사항 불러오기 (Pull)**:
   - 다른 팀원이 업로드한 최신 파일을 받아오기 위해, `…` 메뉴에서 `Pull`을 선택합니다.
   - `Pull`을 통해 최신 상태의 파일을 가져온 후, 본인의 로컬에서 최신 파일로 작업을 진행하세요.

---

## Git 터미널 명령어 (참고용)

Visual Studio Code에서 Git 터미널 명령어를 사용할 수도 있습니다. 아래는 해당 단계에 대응하는 Git 명령어입니다.

```bash
# 파일 변경사항 저장, 커밋, 푸시 순서
git add .                         # Stage Changes
git commit -m "변경 사항 설명"      # Commit
git push                          # Push to GitHub

# 최신 파일 받아오기
git pull                          # Pull latest changes
위의 단계를 따라 모든 팀원이 최신 데이터를 반영하여 프로젝트를 진행할 수 있도록 해주세요.
```

---

## 파일 구조 예시

```bash
├── README.md                # 저장소 사용 설명서
├── Proposal.docx|.hwpx      # 프로젝트 제안서 폴더
├── Notebooks/               # Jupyter Notebook 파일 폴더
├── Reports/                 # 최종 보고서 및 중간 보고서 폴더
└── Data/                    # 데이터 파일 폴더
```

## 참고사항

GitHub Codespaces를 사용하여 코드 작성, 실행 및 수정이 가능합니다.
Codespaces는 인터넷 연결만 있으면 어디서든지 사용 가능하므로 팀원들 간의 원활한 협업을 위해 적극 활용하세요.

저장소 사용에 관한 질문이나 문제가 발생하면 지도교수에게 문의하세요.
