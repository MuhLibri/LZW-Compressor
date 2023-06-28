from django.shortcuts import render
from django.http import HttpResponse
from . import Encoder, Decoder, Utils
from .models import History


ascii_count = 256
ascii_range = range(0, ascii_count)
ascii_list = [chr(i) for i in ascii_range]


def index(request):
    enc_res = None
    dec_res = None
    choice1 = 'decimal'
    choice2 = 'decimal'
    checked = False

    if (request.method == 'POST'):
        choice1 = request.POST['format1']
        choice2 = request.POST['format2']
        chars = request.POST['chars']
        code = request.POST['code']
        if (chars != ''):
            enc_res = Encoder.encode(chars, ascii_list)
            if (request.POST['format1'] == 'binary'):
                enc_res = [Utils.Utils.decimalToBinary(x) for x in enc_res]
            enc_res = ' '.join(map(str, enc_res))
            if ('saveCheckbox' in request.POST):
                history1 = History()
                history1.name = "Compression"
                history1.user_input = chars
                history1.output = enc_res
                history1.save()
                checked = True

        if (code != ''):
            codeList = code.split()
            if (request.POST['format2'] == 'binary'):
                codeList = [Utils.Utils.binaryToDecimal(x) for x in codeList]
            codeList = [int(i) for i in codeList]
            dec_res = Decoder.decode(codeList, ascii_list)
            if ('saveCheckbox' in request.POST):
                history2 = History()
                history2.name = "Decompression"
                history2.user_input = code
                history2.output = dec_res
                history2.save()
                checked = True

    histories = History.objects.all()

    return render(request, 'index.html', {'enc_result': enc_res, 'dec_result': dec_res, 'prevChoice1':choice1, 'prevChoice2':choice2, 'checked':checked, 'histories': histories})