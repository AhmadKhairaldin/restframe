from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import models
from . import serializers

# Create your views here.

# crud club
@api_view(['POST'])
def addclub(request):
    seria = serializers.clubSerializers(data=request.data)
    if seria.is_valid():
        seria.save()
        return Response(seria.data)
    else:
        return Response("there are problem", status=404)

@api_view(['GET'])
def getclub(request):
    club = models.club.objects.all()
    serial = serializers.clubSerializers(club,many=True)
    return  Response(serial.data)


# *********************crud member***********************
@api_view(['GET'])
def getmem(request):
    mem = models.member.objects.all()
    ser = serializers.memberSerializers(mem,many=True)
    return Response(ser.data)

@api_view(['POST'])
def addmem(request):
    ser = serializers.memberSerializers(data = request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data,status=201)
    else:
        return Response('there are problem')

@api_view(['PUT'])
def updatemem(request,id):
    mem = models.member.objects.get(id=id)
    ser = serializers.memberSerializers(instance=mem,data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data, status=201)
    else:
        return Response('there are problem')

@api_view(['DELETE'])
def detetemem(request,pk):
    mem=models.member.objects.get(id=pk)
    mem.delete()
    return Response("delete is sucssful")


# ********************crud tournament*********************
@api_view(['GET'])
def getdata(requset):
    tour = models.tournament.objects.all()
    serialzer = serializers.tournamentSerializers(tour,many=True)
    return Response(serialzer.data)

@api_view(['POST'])
def insertdata(request):
    seria = serializers.tournamentSerializers(data =request.data)
    if seria.is_valid():
        seria.save()
        return Response(seria.data)
    else:
        return Response("there are problem",status=404)

@api_view(['PUT'])
def updatedata(request,pk):
    tour = models.tournament.objects.get(id=pk)
    ser= serializers.tournamentSerializers(instance=tour,data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data, status=201)
    else:
        return Response('there are problem')

@api_view(['DELETE'])
def detetedata(request,pk):
    tour=models.tournament.objects.get(id=pk)
    tour.delete()
    return Response("delete is sucssful")

# *****************crud player ***********************
@api_view(['GET'])
def getplay(requset):
    play = models.player.objects.all()
    serialzer = serializers.playerSerializers(play,many=True)
    return Response(serialzer.data)

@api_view(['POST'])
def insertplay(request):
    seria = serializers.playerSerializers(data =request.data)
    if seria.is_valid():
        seria.save()
        return Response(seria.data)
    else:
        return Response("there are problem",status=404)

@api_view(['PUT'])
def updateplay(request,pk):
    play = models.player.objects.get(id=pk)
    ser= serializers.playerSerializers(instance=play,data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data, status=201)
    else:
        return Response('there are problem')

@api_view(['DELETE'])
def deteteplay(request,pk):
    play=models.player.objects.get(id=pk)
    play.delete()
    return Response("delete is sucssful")

# ************ crud match ************************
@api_view(['GET'])
def getmatch(requset):
    mat = models.match.objects.all()
    serialzer = serializers.matchSerializers(mat,many=True)
    return Response(serialzer.data)

@api_view(['POST'])
def insertmatch(request):
    seria = serializers.matchSerializers(data =request.data)
    if seria.is_valid():
        seria.save()
        return Response(seria.data)
    else:
        return Response(seria.error_messages)

@api_view(['PUT'])
def updatematach(request,pk):
    mat = models.match.objects.get(id=pk)
    ser= serializers.matchSerializers(instance=mat,data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data, status=201)
    else:
        return Response('there are problem')

@api_view(['DELETE'])
def detetemacth(request,pk):
    mat=models.match.objects.get(id=pk)
    mat.delete()
    return Response("delete is sucssful")