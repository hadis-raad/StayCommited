from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Users
from diagrams.onprem.database import PostgreSQL
from diagrams.programming.language import Python
from diagrams.programming.framework import React

# Create the architecture diagram
with Diagram("stayComitted MVP Architecture", show=False) as diag:
    user = Users("User")

    with Cluster("Frontend"):
        react_frontend = React("React Frontend")

    with Cluster("Backend"):
        fastapi_backend = Python("FastAPI Backend")

    with Cluster("Database"):
        database = PostgreSQL("Database")

    with Cluster("Machine Learning"):
        ml_models = Python("ML Models")

    with Cluster("External APIs"):
        external_apis = Python("LLM Integration")

    user >> Edge(label="Interact") >> react_frontend
    react_frontend >> Edge(label="API Requests") >> fastapi_backend
    fastapi_backend >> Edge(label="CRUD Operations") >> database
    fastapi_backend >> Edge(label="API Requests") >> ml_models
    fastapi_backend >> Edge(label="API Requests") >> external_apis

# Save the diagram to a file
diag_path = "stayComitted_MVP_Architecture.png"
diag.render()
