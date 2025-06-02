def getTopXMatchesQuery(target, limit) -> str:
    query = f"""
        WITH target_vector AS (
            SELECT ARRAY{target}::DECIMAL[] AS input_embedding
        )
        SELECT 
            stored.id,
            stored.userID,
            stored.username,
            SQRT(SUM(POW(stored_value - input_value, 2))) AS euclidean_distance
        FROM 
            embeddings stored,
            target_vector input,
            UNNEST(stored.embedding, input.input_embedding) AS pair(stored_value, input_value)
        GROUP BY 
            stored.id, stored.userid, stored.username
        ORDER BY 
            euclidean_distance
        LIMIT {limit};
    """
    return query
