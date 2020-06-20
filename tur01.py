import turtle as t                          #turtle을 t로 두기

def draw_pos(x, y):                         
    t.clear()                               #turtle 위치를 x,y라 할때 흔적 초기화
    t.setpos(x,y)                           #다시 turtle 위치를 x,y로 변경
    t.stamp()                               #turtle의 흔적을 남김

    hl = - (t.window_height() / 2)          #스크린 하단부분 y축 위치 계산 후 대입
                                            #(hl = -300)

    tm = 0                                  #time을 0으로 초기화 시킴
    while True:                             #if문에 만족시킬 때 반복시킴
        d = (9.8 * tm**2) / 2               #등가속도 운동이라 d(거리) 공식 사용
        ny = y - int(d)                     #ny를 설정하기
        if ny > hl:                         #ny가 hl보다 클 때라는 전제조건
            t.goto(x, ny)                   #
            t.stamp()
            tm = tm + 0.3
        else:
            break
        
t.setup(500, 600)                           #turtle 스크린 크기 결정하기
t.shape("circle")                           #turtle 모양 circle로 결정하기
t.shapesize(0.3, 0.3, 0)                    #turtle 크기와 테두리 설정하기   
t.penup()                                   #turtle 펜을 올림       
s = t.Screen()                              #turtle 스크린 생성하기

s.onscreenclick(draw_pos)                   #마우스 클릭하면 콜백 함수 호출
s.listen()                                  #스크린에서 점의 이동 확인 가능
