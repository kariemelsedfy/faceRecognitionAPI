def getFaceRecognitionQuery(threshold: int, target) -> str:
    query = f"""
        WITH target_vector AS (
        SELECT ARRAY{target}::DECIMAL[] AS input_embedding
        )

        SELECT 
        stored.userID,
        SQRT(SUM(POW(stored_value - input_value, 2))) AS euclidean_distance

        
        FROM 
        embeddings stored,
        target_vector input,
        UNNEST(stored.embedding, input.input_embedding) AS pair(stored_value, input_value)


        GROUP BY 
        stored.userID


        HAVING 
        SQRT(SUM(POW(stored_value - input_value, 2))) < {threshold}


        ORDER BY 
        euclidean_distance

        LIMIT 1;
    """

    return query
