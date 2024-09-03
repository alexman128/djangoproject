from notification.models import BackendUser, Channel, Category
# from watchlist_app.api.serializer import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# GET


@api_view(["GET"])
def movie_list(request):
    movie = Movie.objects.all()
    serializer = MovieSerializer(movie, many=True)
    return Response(serializer.data)


@api_view()
def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
