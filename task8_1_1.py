from datetime import datetime
class Date:
    da = 0

    def __init__(self, da):
        self.da = input('Enter date ddmmyyyy: ').split(' ')[0]
        print('Time')

    @staticmethod
    def validate_guess(da):
        result = None
        for f in ['%d%m%Y', '%d%m%Y.%H']:
            try:
                result = datetime.strptime(da, f)
            except:
                pass
        if result is None:
            print('There is no such date on Earth')
        else:
            print('Date is fine.')

    @classmethod
    def convert(cls, result):
        return cls(result)


Date.convert('3')
Date.validate_guess('3')
