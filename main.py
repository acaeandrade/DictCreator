class Main:

    def __init__(self):
        self.bol = False
        self.bol2 = False

        while not self.bol:

            self.opt1 = input("Add char or str to a password created ? (Y/N): ")

            if self.opt1 == "Y" or self.opt1 == "y" or self.opt1 == "N" or self.opt1 == "n":
                self.bol = True
            else:
                pass

        self.FILE = open('pass.txt', 'a+')
        #isfile
        self.alphab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.alphaB = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                       'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


        for i in range(10000000, 99999999):


            self.password = i.__str__()


#case opt1 == 'Y'
            if self.opt1 == 'Y' or self.opt1 == 'y':


                while not self.bol2:

                    self.opt1_2 = input("Set first letter of salting to uppercase? (Y/N)")

                    if self.opt1_2 == "Y" or self.opt1_2 == "y" or self.opt1_2 == "N" or self.opt1_2 == "n":
                        self.bol2 = True
                    else:
                        pass
                print(self.bol2)
#bol2 been set to TRUE state
#getting of the looping


#case opt1_1 == 'Y' AND opt1_2 == 'Y'
                if self.opt1_2 == 'Y' or self.opt1_2 == 'y':
                    print(self.password)
                    self.FILE.write(self.password + '\n')
                    print("Adding alphabet to nums..")

                    try:
                        for alpha0 in self.alphaB:
                            for alpha1 in self.alphab:
                                for alpha2 in self.alphab:
                                    self.salted = self.password + alpha0 + alpha1 + alpha2
                                    self.FILE.write(self.salted + '\n')
                                    print("******** \n ", self.salted, "\n")
                    except KeyboardInterrupt:
                        pass

                else:
                    try:
                        for alpha0 in self.alphab:
                            for alpha1 in self.alphab:
                                for alpha2 in self.alphab:
                                    self.salted = self.password + alpha0 + alpha1 + alpha2
                                    self.FILE.write(self.salted + '\n')
                                    print("******** \n ", self.salted, "\n")
                    except KeyboardInterrupt:
                        for alpha0 in self.alphab:
                            for alpha1 in self.alphab:
                                for alpha2 in self.alphab:
                                    self.salted = self.password + alpha0 + alpha1 + alpha2
                                    self.FILE.write(self.salted + '\n')
                                    print("******** \n ", self.salted, "\n")


#Case opt1 == 'N'
            else:
                try:
                    print(self.password)
                except KeyboardInterrupt:
                    print(self.password)

                except:
                    self.FILE.write(self.password + '\n')

        try:
            self.FILE.close()
        except:
            self.FILE.close()


    def _private_verify(self):
        pass


Main()