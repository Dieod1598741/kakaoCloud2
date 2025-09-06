students = []  # 학생 리스트 (프로그램 종료시 초기화)
# 이름으로 학생 찾는 함수
def find_student_name(students, name):
    for i, student in enumerate(students):
        if student["name"] == name:
            return i
    return -1
# 이름이 완성된 이름인지 확인하는 함수
def valid_korean_name(name) -> bool:
    return all('가' <= ch <= '힣' for ch in name)

# 점수입력 함수
def input_score(score):
    while True:
        raw = input(score).strip()
        if raw.isdigit():
            return int(raw)
        print("점수를 입력하세요.")

# 1. 추가
def add_student(students) :
    while True:                                        # 반복문
        print("(q)입력시 메인메뉴로")
        name = input("학생 이름 :").strip()
        if name.lower() == "q":   # q 입력 → 메인메뉴 복귀
            print("메인 메뉴로 돌아갑니다.")
            return
        if not name:
            print("이름은 비워둘 수 없습니다.")
            continue
        if not valid_korean_name(name):
            print("이름은 완성된 한글만 입력할 수 있습니다.")
            continue
        if find_student_name(students, name) != -1:
            print("이미 같은 이름이 존재합니다.")
            continue
        score = input_score("점수(0~100): ")
        if not (0 <= score <= 100):
            print("점수는 0~100 사이여야 합니다.")
            return
        students.append({"name": name, "score": score})
        print(f"{name} 학생이 추가되었습니다.")
        break
# 2. 삭제
def delete_student(students):
    while True:
        print("(q)입력시 메인메뉴로")
        name = input("삭제할 학생 이름: ").strip()
        idx = find_student_name(students, name)
        if name.lower() == "q":   # q 입력 → 메인메뉴 복귀
            print("메인 메뉴로 돌아갑니다.")
            return
        if not valid_korean_name(name):
            print("이름은 완성된 한글만 입력할 수 있습니다.")
            continue
        if idx == -1:
            print("해당 학생을 찾을 수 없습니다.")
            continue
        
        removed =  students.pop(idx)
        print(f"{removed['name']} 학생 정보가 삭제되었습니다.")
# 3. 수정
def update_score(students):
    print("(q)입력시 메인메뉴로")
    name = input("점수 수정할 학생 이름: ").strip()
    idx = find_student_name(students, name)
    if name.lower() == "q":   # q 입력 → 메인메뉴 복귀
            print("메인 메뉴로 돌아갑니다.")
            return
    if idx == -1:
        print("해당 학생을 찾을 수 없습니다.")
        return
    new_score = input_score("새 점수(0~100): ")
    if not (0 <= new_score <= 100):
        print("점수는 0~100 사이여야 합니다.")
        return

    students[idx]["score"] = new_score   # 인덱스로 바로 갱신
    print(f"{name} 학생 점수가 {new_score}점으로 수정되었습니다.")
# 4. 목록
def print_all(students):
    if not students:                      # 빈 리스트면 바로 안내
        print("등록된 학생이 없습니다.")
        return
    print("\n[학생 목록]")
    for s in students:
        print(f"- {s['name']} : {s['score']}점")
# 5. 통계
def print_stats(students):
    if not students:
        print("학생 정보가 없습니다.")
        return

    scores = [s["score"] for s in students]   # 점수만 추출(리스트 내포)
    max_score = max(scores)
    min_score = min(scores)
    avg_score = sum(scores) / len(scores)

    # 동점이 있다면 '첫 번째' 학생 이름을 보여준다.
    max_name = next(s["name"] for s in students if s["score"] == max_score)
    min_name = next(s["name"] for s in students if s["score"] == min_score)

    print("\n[통계]")
    print(f"최고 점수: {max_score}점 ({max_name})")
    print(f"최저 점수: {min_score}점 ({min_name})")
    print(f"평균 점수: {avg_score:.2f}점")
    
# 메인화면
def main():
    while True:
        print("\n ===학생 성적 관리 프로그램===")
        print("1. 추가 2. 삭제 3. 수정 4. 목록 5. 통계 0. 종료")
        choice = input("메뉴 번호를 선택하세요: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            delete_student(students)
        elif choice == "3":
            update_score(students)
        elif choice == "4":
            print_all(students)
        elif choice == "5":
            print_stats(students)
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 번호를 입력하세요.")
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n사용자 종료")