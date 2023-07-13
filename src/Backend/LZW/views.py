from django.shortcuts import render
from django.http import HttpResponse
from . import Encoder, Decoder, Utils
from .models import History
from .serializers import HistorySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


ascii_count = 256
ascii_range = range(0, ascii_count)
ascii_list = [chr(i) for i in ascii_range]


@api_view(['POST'])
def index(request):
    enc_res = ""
    dec_res = ""

    if (request.method == 'POST'):
        chars = request.POST['chars']
        oChars = chars
        code = request.POST['code']
        algorithm1 = request.POST['algorithm1']
        algorithm2 = request.POST['algorithm2']
        saveChecked = 'saveCheckbox' in request.POST

        if (chars != ''):
            alg1 = ""
            if (algorithm1 == 'bwt' or algorithm1 == 'rle'):
                alg1 += "BWT+"
                chars = Encoder.bwtEncode(chars)
            if (algorithm1 == 'rle'):
                alg1 += "RLE+"
                chars = Encoder.rleEncode(chars)
            
            enc_res = Encoder.encode(chars, ascii_list)
            if (request.POST['format1'] == 'binary'):
                enc_res = [Utils.Utils.decimalToBinary(x) for x in enc_res]
            enc_res = ' '.join(map(str, enc_res))
            if (saveChecked):
                alg1 += "LZW"
                history1 = History()
                history1.name = "Compression" + " (" + alg1 + ")"
                history1.user_input = oChars
                history1.output = enc_res
                history1.save()

        if (code != ''):
            alg2 = ""
            codeList = code.split()
            if (request.POST['format2'] == 'binary'):
                codeList = [Utils.Utils.binaryToDecimal(x) for x in codeList]
            codeList = [int(i) for i in codeList]
            dec_res = Decoder.decode(codeList, ascii_list)
            if (algorithm2 == 'rle'):
                alg2 += "RLE+"
                dec_res = Decoder.rleDecode(dec_res)
            if (algorithm2 == 'rle' or algorithm2 == 'bwt'):
                alg2 += "BWT+"
                dec_res = Decoder.bwtDecode(dec_res)
            if (saveChecked):
                alg2 += "LZW"
                history2 = History()
                history2.name = "Decompression" + " (" + alg2 + ")"
                history2.user_input = code
                history2.output = dec_res
                history2.save()

    return Response({'enc_result': enc_res, 'dec_result': dec_res})


@api_view(['GET'])
def getHistory(request):
    history = History.objects.all()
    serializer = HistorySerializer(history, many=True)
    return Response(serializer.data)