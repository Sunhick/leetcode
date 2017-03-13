from Queue import Queue

def getMovieRecommendations(movie, N):
    # better to do a DFS / BFS traversal
    rating = movie.getRating()
    
    q = Queue()
    q.put(movie)
    
    seen = [movie]
    recommend = []

    while not q.empty():
        m = q.get()
        #print 'm: ', m.getId()
        movies = m.getSimilarMovies()
        
        for mov in movies:
            if mov in seen:
                #print 'seen: ', mov.getId()
                continue
            #print 'add: ', mov.getId()
            q.put(mov)

        # don't recommend already recommended movie
        if m in seen:
            continue
        
        # mark movie as seen.
        seen.append(m)
        
        # check if we can recommend this movie
        if m.getRating() > rating:
            # print 'recommend: ', m.getId()
            recommend.append(m.getId())
    
    recommend = sorted(recommend)
    print ' '.join(str(x) for x in recommend[:N])
