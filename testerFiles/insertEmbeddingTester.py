import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database import insertEmbedding

insertEmbedding(1, [2, 3, 4])


#test was successful
