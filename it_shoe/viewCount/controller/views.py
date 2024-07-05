from rest_framework import viewsets
from rest_framework.response import Response
from viewCount.service.viewcount_service_impl import ViewCountServiceImpl

view_count_service = ViewCountServiceImpl()

class ViewCountView(viewsets.ViewSet):

    def increment_community(self, request, pk=None):
        new_view_count = view_count_service.increment_community_view_count(pk)
        if new_view_count is not None:
            return Response({'status': 'success', 'viewCount': new_view_count})
        else:
            return Response({'status': 'error', 'message': 'Community not found'}, status=404)

    def increment_review(self, request, pk=None):
        new_view_count = view_count_service.increment_review_view_count(pk)
        if new_view_count is not None:
            return Response({'status': 'success', 'viewCount': new_view_count})
        else:
            return Response({'status': 'error', 'message': 'Community not found'}, status=404)