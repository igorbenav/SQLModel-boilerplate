from fastcrud import FastCRUD

from ..models.rate_limit import RateLimit, RateLimitCreateInternal, RateLimitDelete, RateLimitUpdate, RateLimitUpdateInternal

CRUDRateLimit = FastCRUD[RateLimit, RateLimitCreateInternal, RateLimitUpdate, RateLimitUpdateInternal, RateLimitDelete]
crud_rate_limits = CRUDRateLimit(RateLimit)
