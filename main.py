from board_dao import *

board_dao = BoardDAO()

# 커넥션 테스트
board_dao.get_connection()

while True:

    print("="*40)
    print("1.목록 2.등록 3.내용 4.삭제 5.수정 0.종료")
    print("="*40)

    menu = input("선택 > ")

    if menu == "0":
        break
    elif menu =="1": # 게시판 select * from board
        boards = board_dao.select_all()
        print()
        
        for board in boards:
            print(board[0],
                  board[1],
                  board[3])
    
    elif menu == "2":
        title = input("제목:")
        content = input("내용:")
        writer = input("작성자:")

        board_dao.insert_board(
            title,
            content,
            writer
        )

        print("등록 완료")

    elif menu == "3":
        num = input("번호: ")
        board = board_dao.select_one(num)

        if board:
            print()
            print("=== 게시글 내용 ===")
            print("번호 :", board[0])
            print("제목 :", board[1])
            print("내용 :", board[2])
            print("작성자 :", board[3])
            print("작성일 :", board[4])
            print("=" * 40)

            # [추가] 해당 게시글의 댓글 목록 가져와서 출력하기
            replies = board_dao.select_replies_by_board_id(num)
            print(f"댓글 ({len(replies)})")
            for r in replies:
                # r[2]: 작성자, r[1]: 내용, r[3]: 작성일
                print(f"  └─ {r[2]}: {r[1]} ({r[3]})")
            print("=" * 40)

            # [추가] 상세보기 안에서 댓글 작성 여부 묻기
            sub_menu = input("1.댓글작성  2.돌아가기 > ")
            if sub_menu == "1":
                r_writer = input("댓글 작성자: ")
                r_content = input("댓글 내용: ")
                board_dao.insert_reply(num, r_content, r_writer)
                print("댓글이 등록되었습니다.")
        else:
            print("존재하지 않는 게시물입니다.")


    elif menu == "4":

        num = input("삭제 번호 : ")

        board_dao.delete_board(num)

        print("삭제 완료")

    elif menu == "5":
        num = input("수정할 글 번호:")
        board = board_dao.select_one(num)
        if board:
            title = input(f"새 제목({board[1]}):")or board[1] # 입력 안 하면 기존 값 유지
            content = input(f"새 내용({board[2]}):") or board[2]
            board_dao.update_board(num,title,content)
            print("수정 완료")

        else:
            print("존재하지 않는 게시글입니다.")


print("게시판 종료")