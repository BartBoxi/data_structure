def get_top_categories(videos, k):
    category_results = {}
    
    for video in videos:
        category_name = video["category"]
        category_views = video["views"]
        
        
        if category_name not in category_results:
            category_results[category_name] = category_views
        else:
            category_results[category_name] += category_views
            
    
    
    
    return sorted(category_results.keys(), key =  lambda x: category_results[x])[:k]
        
        





videos = [
    {"video_id": "v1", "category": "Gaming", "views": 1500},
    {"video_id": "v2", "category": "Vlog", "views": 500},
    {"video_id": "v3", "category": "Gaming", "views": 3000},
    {"video_id": "v4", "category": "Charity", "views": 10000},
    {"video_id": "v5", "category": "Vlog", "views": 200},
    {"video_id": "v6", "category": "Gaming", "views": 100}
]

print(get_top_categories(videos,k=2))
