from mcp.server.fastmcp import FastMCP
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


mcp = FastMCP("GitHub-API-Public-Private")


def get_headers():
    """
    Create headers using GitHub token from environment variable
    """
    token = os.getenv("GITHUB_TOKEN")

    if not token:
        raise ValueError("GITHUB_TOKEN environment variable is not set")

    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }


@mcp.tool()
def get_github_repos(username: str) -> str:
    """
    Fetch public + private repositories of the authenticated user.

    Args:
        username: GitHub username (for display/logging purpose)
    """
    try:
        url = "https://api.github.com/user/repos"

        headers = get_headers()

        params = {
            "visibility": "all",   # public + private
            "per_page": 10         # limit results
        }

        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()

        repos = response.json()

        if not repos:
            return f"No repositories found for {username}."

        repo_list = []
        for repo in repos:
            name = repo.get("name")
            html_url = repo.get("html_url")
            private = repo.get("private")

            repo_list.append(
                f"{name} ({'Private' if private else 'Public'}) - {html_url}"
            )

        return "Repositories:\n" + "\n".join(repo_list)

    except Exception as e:
        return f"Error fetching repositories: {e}"


@mcp.tool()
def get_github_user() -> str:
    """
    Get authenticated GitHub user details
    """
    try:
        url = "https://api.github.com/user"

        headers = get_headers()

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        user = response.json()

        return (
            f"User: {user.get('login')}\n"
            f"Name: {user.get('name')}\n"
            f"Public Repos: {user.get('public_repos')}\n"
            f"Followers: {user.get('followers')}"
        )

    except Exception as e:
        return f"Error fetching user details: {e}"


if __name__ == "__main__":
    mcp.run()