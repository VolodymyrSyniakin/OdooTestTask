'''
Необхідно розрахувати кількість “обраних” квитків із заданою сумою цифр,
серед тих, номер яких складається з 2N розрядів. “Обраним” є квиток у 
якого сума перших N цифр рівна сумі останніх N цифр.
Вхідні дані
В єдиній стрічці через пробіл вказано два числа: перше — N (1 ≤ N ≤ 50); 
друге — сума цифр цікавих для нас квитків (позитивне число, не більше 1000).
'''

count = 0


def setInputData():
    inputStr = input('Enter two numbers separated by a space: ') 
    return inputStr.split(' ') 

 
def existForResultNumbers (restRank, restSum):
    if  restSum / restRank >= 10:
        return False
    return True


def countingTickets(restRank, restSum):
    global count

    i = 9
    if restSum < 9: 
        i = restSum
        
    while i >= 0:
        rest = restSum - i
        
        if restRank > 1:
            if not existForResultNumbers(restRank - 1, rest):
                break
            elif rest >= 0:
                countingTickets(restRank - 1, rest)
        elif restRank == 1:
            if rest == 0:
                count += 1
            else:
                break
        else:
            break
        i -= 1 


def specialTickets(rank, sumNumber):
   
    if not 1 <= rank <= 50 or not 0 < sumNumber <= 1000 or sumNumber % 2 == 1:
        return 'Incorrect input data'
        
    halfSum = sumNumber / 2
        
    if  not existForResultNumbers(rank, halfSum):
        return 0
    
    countingTickets(rank, halfSum)
    return count * count


# START:
listData = setInputData()
print('Number of special tickets:', specialTickets(int (listData[0]), int (listData[1])))
