import numpy as np

cov_params = np.array([ .00539200350502, 
                        .00008301229666, 
                       -.00005403142257, 
                        .00027510415024, 
                       -.00011505567442, 
                       -.00008319502641, 
                       -.00025249970065, 
                        -.0001270546323, 
                       -.01947463654581, 
                       -.00148622043794, 
                        .00008301229666, 
                        .00061494208178, 
                       -.00053530516851, 
                        .00008460286252, 
                       -.00003141014027, 
                       -.00021146981832, 
                       -.00008800491569, 
                       -.00006211127529, 
                       -.00970271476814, 
                        -.0001272128164, 
                       -.00005403142257, 
                       -.00053530516851, 
                        .00069648064051, 
                       -.00093761071164, 
                       -.00005116444609, 
                        .00020382401424, 
                       -.00001703315889, 
                       -.00002542561244, 
                        .00787679245732, 
                         .0002313226118, 
                        .00027510415024, 
                        .00008460286252, 
                       -.00093761071164, 
                        .00594922684993, 
                       -.00050426560925, 
                        .00016943427562, 
                        .00027102568975, 
                       -2.220879079e-06, 
                       -.00557358532415, 
                        .00001081569952, 
                       -.00011505567442, 
                       -.00003141014027, 
                       -.00005116444609, 
                       -.00050426560925, 
                        .00721473696044, 
                       -.00003544762186, 
                       -.00016348523263, 
                        .00013992262115, 
                       -.01296017976727, 
                        -.0008759220358, 
                       -.00008319502641, 
                       -.00021146981832, 
                        .00020382401424, 
                        .00016943427562, 
                       -.00003544762186, 
                         .0014160483513, 
                       -.00099829776806, 
                       -.00025251642734, 
                       -.01107628126994, 
                       -.00009086700905, 
                       -.00025249970065, 
                       -.00008800491569, 
                       -.00001703315889, 
                        .00027102568975, 
                       -.00016348523263, 
                       -.00099829776806, 
                        .00670962104762, 
                       -.00057993093321, 
                       -.00329528394208, 
                        .00033097930374, 
                        -.0001270546323, 
                       -.00006211127529, 
                       -.00002542561244, 
                       -2.220879079e-06, 
                        .00013992262115, 
                       -.00025251642734, 
                       -.00057993093321, 
                        .00307661027405, 
                       -.00407244778684, 
                        .00001822288839, 
                       -.01947463654581, 
                       -.00970271476814, 
                        .00787679245732, 
                       -.00557358532415, 
                       -.01296017976727, 
                       -.01107628126994, 
                       -.00329528394208, 
                       -.00407244778684, 
                        .50904016608196, 
                        .00485143549485, 
                       -.00148622043794, 
                        -.0001272128164, 
                         .0002313226118, 
                        .00001081569952, 
                        -.0008759220358, 
                       -.00009086700905, 
                        .00033097930374, 
                        .00001822288839, 
                        .00485143549485, 
                        .00594507951461]).reshape(10,10)

llf = np.array([-7804.3801852628])

llnull = np.array([ -8155.024019474])

n_lcens = np.array([            4313])

n_rcens = np.array([               0])

n_ucens = np.array([            2053])

chi2 = np.array([ 701.28766842242])

df_model = np.array([               8])

df_resid = np.array([            6358])

params = np.array([-1.5307129528123, 
                   -.10513850576491, 
                    .12829011495541, 
                    -.0277671226359, 
                    -.9434969299566, 
                    -.0859750294499, 
                    .31283874114621, 
                    .01421196799422, 
                    7.8365292766812, 
                    4.4988741366943])

bse = np.array([ .07343026286908, 
                 .02479802576379, 
                 .02639091966011, 
                 .07713123135234, 
                 .08493960772476, 
                 .03763041789957, 
                 .08191227653786, 
                 .05546719998387, 
                 .71347050820756, 
                 .07710434173643])

class Bunch(dict):
    def __init__(self, **kw):
        dict.__init__(self, kw)
        self.__dict__  = self


results = Bunch(cov_params=cov_params, llf=llf, llnull=llnull, n_lcens=n_lcens, n_rcens=n_rcens, n_ucens=n_ucens, chi2=chi2, df_model=df_model, df_resid=df_resid, params=params, bse=bse, )

