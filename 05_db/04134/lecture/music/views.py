from django.shortcuts import render, get_object_or_404
from .models import Music
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import MusicSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def music_list_create(request):
    if request.method == 'GET':
        # 모든 음악 리스트를 json 형식으로 응답
        all_music = Music.objects.all() # 모든 음악 리스트 가져와서 변수에 저장 
        # QuerySet 리턴되는 경우
        # 조회되는 데이터가 0개 이상
        # all(), filter() -> many 옵션 설정 필수

        # QuerySet 리턴 외 객체로 리턴되는 경우
        # get() 사용한 데이터 조회 -> many 옵션 설정 불필요
        serializer = MusicSerializer(all_music, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MusicSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 글 생성 로직

@api_view(['GET'])
def music_detail(request, music_pk):
    # music = Music.objects.get(pk=music_pk)

    # 첫 번째 인자 : 어떤 모델에서 찾을 지
    # 두 번째 인자 : 조건
    # 사용자가 요청 잘못한걸 사용자한테 알려주기 위한 코드
    music = get_object_or_404(Music, pk=music_pk)

    MusicSerializer(music)
    return Response(serializer.data)