import traceback
from helper.ErrException import ErrException
from model.TicketModel import TicketModel

class TicketService:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def createTicket(self, data):
        try:
            # order = TicketModel().select(7)
            # print(order)
            createOrder = TicketModel().create(data)
            print(createOrder.rowcount)
            if createOrder.rowcount<1:
                result = {'responsecode': 101, 'status': 'failed','message': 'no insert'}
            else:
                result = {'responsecode': 0, 'status': 'success','message': 'Yeah'}
        
        except Exception as error:
            if type(error) == ErrException:
                result = {'responsecode': int(
                    error.code), 'status': 'failed', 'message': error.msg}
            else:
                result = {'responsecode': 100, 'status': 'failed',
                          'message': str(traceback.format_exc())}  # str(error)
        return result
    
    def selectTicket(self, data):
        try:
            print(data)
            order = TicketModel().select(data)
            print(order)
            # for inorder in order:
            #     print(inorder)
            result = {'responsecode': 0, 'status': 'success','result': order}
        
        except Exception as error:
            if type(error) == ErrException:
                result = {'responsecode': int(
                    error.code), 'status': 'failed', 'message': error.msg}
            else:
                result = {'responsecode': 100, 'status': 'failed',
                          'message': str(traceback.format_exc())}  # str(error)
        return result
    
    def updateTicket(self, data):
        try:
            updateOrder = TicketModel().update(data)
            print(updateOrder.rowcount)
            result = {'responsecode': 0, 'status': 'success','message': 'Yeah'}
        
        except Exception as error:
            if type(error) == ErrException:
                result = {'responsecode': int(
                    error.code), 'status': 'failed', 'message': error.msg}
            else:
                result = {'responsecode': 100, 'status': 'failed',
                          'message': str(traceback.format_exc())}  # str(error)
        return result

    