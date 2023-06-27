from django.shortcuts import render
from django.http import HttpResponse
from . import Encoder, Decoder, Utils

ascii_count = 256
ascii_range = range(0, ascii_count)
ascii_list = [chr(i) for i in ascii_range]


def index(request):
    enc_res = None
    dec_res = None
    choice1 = 'decimal'
    choice2 = 'decimal'

    if (request.method == 'POST'):
        choice1 = request.POST['format1']
        choice2 = request.POST['format2']
        if (request.POST['chars'] != ''):
            enc_res = Encoder.encode(request.POST['chars'], ascii_list)
            if (request.POST['format1'] == 'binary'):
                enc_res = [Utils.Utils.decimalToBinary(x) for x in enc_res]
            enc_res = ' '.join(map(str, enc_res))

        if (request.POST['code'] != ''):
            codeList = request.POST['code'].split()
            if (request.POST['format2'] == 'binary'):
                codeList = [Utils.Utils.binaryToDecimal(x) for x in codeList]
            codeList = [int(i) for i in codeList]
            dec_res = Decoder.decode(codeList, ascii_list)
            
    return render(request, 'index.html', {'enc_result': enc_res, 'dec_result': dec_res, 'prevChoice1':choice1, 'prevChoice2':choice2})