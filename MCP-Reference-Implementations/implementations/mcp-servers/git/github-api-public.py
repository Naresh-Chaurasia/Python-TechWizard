from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("GitHub-API")

@mcp.tool()
def get_github_repos(username: str) -> str:
    """
    Fetch public repositories of a GitHub user.

    Args:
        username: GitHub username (e.g., 'naresh-Chaurasia')
    """
    try:
        url = f"https://api.github.com/users/{username}/repos"
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        repos = response.json()

        if not repos:
            return f"No public repositories found for {username}."

        repo_list = []
        for repo in repos[:2]:  # limit to 10 repos
            name = repo.get("name")
            url = repo.get("html_url")
            repo_list.append(f"{name} - {url}")

        return f"Public repositories of {username}:\n" + "\n".join(repo_list)

    except Exception as e:
        return f"Error fetching repositories for {username}: {e}"


if __name__ == "__main__":
    mcp.run()