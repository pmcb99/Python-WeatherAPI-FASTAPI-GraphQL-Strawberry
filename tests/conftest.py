import pytest
import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import main

@pytest.fixture
def test_queries():
    schema = strawberry.Schema(Query,mutation=Mutation)
    graphql_app = GraphQLRouter(schema)
    app = FastAPI()
    app.include_router(graphql_app, prefix="/graphql")