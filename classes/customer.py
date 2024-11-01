
class customer :
    def __init__(self,customerID, customerName, customerAddress, phoneNumber, customerEmail) :
        self.__customerID = customerID
        self.__customerName = customerName
        self.__customerAddress = customerAddress
        self.__phoneNumber = phoneNumber
        self.__customerEmail = customerEmail

    def getCustomerID(self) :
        return self.__customerID
    def getCustomerName(self):
        return self.__customerName

    def setCustomerName(self, customerName):
        self.__customerName = customerName

    def getCustomerAddress(self):
        return self.__customerAddress

    def setCustomerAddress(self, customerAddress):
        self.__customerAddress = customerAddress

    def getPhoneNumber(self):
        return self.__phoneNumber

    def setPhoneNumber(self, phoneNumber):
        self.__phoneNumber = phoneNumber

    def getCustomerEmail(self):
        return self.__customerEmail

    def setCustomerEmail(self, customerEmail):
        self.__customerEmail = customerEmail

    #need some other methods to get and set the other attributes

    # toString method
    def __str__(self) :# toString method
        return "Customer ID: " + str(self.__customerID) + "\nCustomer Name: " + self.__customerName + "\nCustomer Address: " + self.__customerAddress + "\nPhone Number: " + self.__phoneNumber + "\nCustomer Email: " + self.__customer

