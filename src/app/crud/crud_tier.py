from fastcrud import FastCRUD

from ..models.tier import Tier, TierCreateInternal, TierDelete, TierUpdate, TierUpdateInternal

CRUDTier = FastCRUD[Tier, TierCreateInternal, TierUpdate, TierUpdateInternal, TierDelete]
crud_tiers = CRUDTier(Tier)
