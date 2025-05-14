'''
    # 조건문 if

    if(조건식) : 조건식이 참일 경우
    실행할 명령문
    else : 조건식이 거짓일 경우
    실행할 명령문
'''
score = input('insert score ?')
grade = 'F'

if int(score) >= 90 :
    grade = 'A'
else :
    grade = 'F'


msg = f'''
    당신의 학점은 {grade} 입니다.
'''
print(msg)


score = int(input('score 입력해주세요.'))

if ((100 >= score) and (score >= 90)) : 
    print('A 학점입니다.')

if (90 <= score) and (score <= 100) :
    print('A 학점입니다. 2')

if ((90 <= score <= 100)) :
    print('A 학점입니다. 3')

if ((100 >= score >= 90)) :
    print('A 학점입니다. 4')

# number = 2 + 3 * 4
number = 2 + 3 * 4
print(number)
number = number + 2 % (2 + 3 * 4) + 2

print('number = ', number)