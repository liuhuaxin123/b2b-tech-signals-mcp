import os
import json
import httpx
from mcp.server.mcpserver import MCPServer

# Configuration - Permanent Production Endpoint on Render
API_HOST = os.environ.get("B2B_SIGNALS_API_HOST", "https://b2b-tech-signals-api.onrender.com")
API_KEY = os.environ.get("B2B_SIGNALS_API_KEY", "")
RAPIDAPI_HOST = os.environ.get("RAPIDAPI_HOST", "b2b-tech-signals.p.rapidapi.com")

mcp = MCPServer(
    name="mcp-server-b2b-tech-signals",
    description="High-intent B2B hiring signals and tech stack intelligence for AI SDRs and automated sales workflows."
)

def make_request(path: str, params: dict = None) -> str:
    url = f"{API_HOST.rstrip('/')}{path}"
    headers = {"User-Agent": "MCP-Client/1.0"}
    
    if API_KEY:
        # If calling via RapidAPI
        if "rapidapi.com" in API_HOST or "p.rapidapi.com" in API_HOST:
            headers["X-RapidAPI-Key"] = API_KEY
            headers["X-RapidAPI-Host"] = RAPIDAPI_HOST
        else:
            headers["X-Admin-Key"] = API_KEY
            
    try:
        with httpx.Client(timeout=10.0) as client:
            resp = client.get(url, params=params, headers=headers)
            
            if resp.status_code == 429:
                return (
                    "⚠️ [429 Quota Exceeded] Free tier monthly limit reached.\n"
                    "👉 Upgrade to Pro ($29/mo for 2,500 signals) at: "
                    "https://rapidapi.com/your-org/api/b2b-tech-stack-and-hiring-intent-signals"
                )
            elif resp.status_code == 403:
                return (
                    "🔒 [403 Forbidden] Missing or invalid API Key.\n"
                    "👉 Get your Free API Key (50 requests/month) at: "
                    "https://rapidapi.com/your-org/api/b2b-tech-stack-and-hiring-intent-signals"
                )
            resp.raise_for_status()
            return json.dumps(resp.json(), indent=2, ensure_ascii=False)
    except Exception as e:
        return f"Error contacting TechSignal API: {str(e)}"

@mcp.tool()
def search_companies_by_tech_signal(tech_keyword: str, limit: int = 10) -> str:
    """
    Search for high-growth tech companies that are currently expanding and hiring for a specific technology.
    
    Args:
        tech_keyword: Target technology or framework (e.g., 'Rust', 'vLLM', 'Kubernetes', 'MCP', 'PyTorch', 'ClickHouse', 'Go')
        limit: Maximum number of signals to return (default: 10, max: 50)
    """
    return make_request("/v1/signals/tech-stack", params={"tech": tech_keyword, "limit": limit})

@mcp.tool()
def get_company_hiring_velocity(company_domain: str) -> str:
    """
    Get all active technical hiring signals, detected stack, and inferred architectural pain points for a specific company domain.
    
    Args:
        company_domain: Domain of the target company (e.g., 'perplexity.ai', 'anthropic.com', 'cognition.ai', 'linear.app', 'figma.com')
    """
    return make_request(f"/v1/companies/{company_domain}/hiring-signals", params={"limit": 30})

@mcp.tool()
def find_companies_with_pain_point(pain_point_category: str, limit: int = 10) -> str:
    """
    Find companies actively hiring with specific technical architectural challenges.
    
    Args:
        pain_point_category: One of ['GPU_INFERENCE_SCALING', 'SECURITY_AUDIT_COMPLIANCE', 'BUILDING_PAYMENT_INFRA', 'ARCHITECTURE_MIGRATION', 'GENERAL_ENGINEERING_EXPANSION']
        limit: Maximum number of signals to return (default: 10)
    """
    return make_request("/v1/signals/pain-points", params={"signal_type": pain_point_category, "limit": limit})

if __name__ == "__main__":
    mcp.run(transport="stdio")
