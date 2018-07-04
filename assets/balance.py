import datetime




class Balance:

    def __init__(self, username):
        self.balance = []
        self.__username = username
        current_file = open('accounts/balance.txt', 'r')
        file_text = current_file.read()
        current_file.close()
        word = ""
        counter = 0
        row = 0
        self.balance.append([])
        for i in file_text:
            if(i != ':'):
                word += i
            elif(i == ':' and counter < 5):
                self.balance[row].append(word)
                counter += 1
                word = ""
                if(counter == 5):
                    self.balance.append([])
                    counter = 0
                    row += 1
        del self.balance[len(self.balance)-1]

    def addValue(self, value, description):
        now = datetime.datetime.now()
        date = ""
        date += str(now.day) + "." + str(now.month) + "." + str(now.year) + "."
        value = int(value)
        self.balance.append([])
        self.balance[len(self.balance) - 1].append(len(self.balance))
        self.balance[len(self.balance) - 1].append(self.__username)
        self.balance[len(self.balance) - 1].append(value)
        self.balance[len(self.balance) - 1].append(date)
        self.balance[len(self.balance) - 1].append(description)

        to_write = ""
        for i in self.balance:
            for j in i:
                j = str(j)
                to_write += j + ":"
        current_document = open("accounts/balance.txt", 'w')
        current_document.write(to_write)
        current_document.close()
        return True

    def deleteRecord(self, record_id):
        index = 0
        for i in self.balance:
            if(str(i[0]) == record_id):
                del self.balance[index]
                to_write = ""
                for j in self.balance:
                    for g in j:
                        g = str(g)
                        to_write += g + ":"

                current_document = open("accounts/balance.txt", 'w')
                current_document.write(to_write)
                current_document.close()
                return True
            else:
                index +=1
    def getBalance(self):
        total = 0
        for i in self.balance:
            if(i[1] == self.__username):
                total += int(i[2])
        return total


        return False

    def getRecords(self):
        return self.balance



#bal = Balance("jasmin")
#bal.addValue("30", "Some Description")

