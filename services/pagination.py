class Pagination(object):
    def __init__(self):
        pass

    def do(self, collection_name, query, request):
        startIndex = int(request.args.get('startIndex', default=1))
        requestedCount = int(request.args.get('limit', default=10))
        sortcolumn = str(request.args.get('sortcolumn', default='_id'))
        sortdirection = str(request.args.get('sortdirection', default='asc'))
        if sortdirection == 'asc':
            direction = 1
        else:
            direction = -1

        #result = list(collection_name.find(query).skip(startIndex-1).limit(requestedCount).sort(sortcolumn, direction))
        result = collection_name.paginationQuery(query, {}, startIndex-1, requestedCount, [sortcolumn, direction])
        pagination = {}
        sort = {}
        pagination['total'] = collection_name.getDocumentsCount(query)
        sort['column'] = sortcolumn
        sort['direction'] = sortdirection
        pagination['sort'] = sort
        pagination['limit'] = len(result)
        pagination['startIndex'] = startIndex
        return result, pagination