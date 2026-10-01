import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # Filter rows where author viewed their own article
    df = views[views['author_id'] == views['viewer_id']]
    
    # Get unique author IDs, rename column to 'id', and drop duplicates
    df = df[['author_id']].rename(columns={'author_id': 'id'}).drop_duplicates()
    
    # Sort by 'id' in ascending order
    return df.sort_values(by='id')