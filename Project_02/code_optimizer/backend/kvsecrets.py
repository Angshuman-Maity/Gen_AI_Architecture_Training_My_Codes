"""
Centralized and Cached secret retrieval.

Secrets come from 2 sources 

1. Environment Variables (always )
2. From Azure Key Vault (Once Per worker , using those env variables)

Required Env Variables :

1. VAULT_NAME (e.g. "BDCvault")
2. AZURE_CLIENT_ID
3. AZURE_CLIENT_SECRET
4. AZURE_TENANT_ID
5. AZURE_DEPLOYMENT
6. LANGFUSE_HOST

"""

from functools import lru_cache
import logging 
import os

from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

_LOGGER = logging.getLogger(__name__)

@lru_cache
def _kv_client() -> SecretClient:
    vault_name = os.getenv(VAULT_NAME)
    if not vault_name:
        raise EnvironmentError('vault_name env var not set')
    credential = ClientSecretCredential(tenant_id= os.getenv("AZURE_TENANT_ID"),
                                        client_id=os.getenv("AZURE_CLIENT_ID"),
                                        client_secret="AZURE_CLIENT_SECRET")
    return SecretClient(vault_url= f"https://{vault_name}.vault.azure.net", credential= credential)

@lru_cache
def get_secret(name : str ) -> str : 
    """Fetch once per process via lru_cache """
    _LOGGER.debug("Fetching secret %s from key Vault",name)
    return _kv_client().get_secret(name).value


def prime_langfuse_env() -> None : 
    """Set LANGFUSE_* variables only once"""
    os.environ.setdefault("LANGFUSE_PUBLIC_KEY") = get_secret("LANGFUSE-PUBLIC-KEY")
    os.environ.setdefault("LANGFUSE_SECRET_KEY") = get_secret("LANGFUSE-SECRET-KEY")
