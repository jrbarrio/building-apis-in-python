def is_rate_limited(self, api_key: str) -> bool:
    # Get current time and the timestamp for one minute ago
    now = datetime.now()
    minute_ago = now - timedelta(minutes=1)
    
    # Remove requests older than 1 minute
    self.requests[api_key] = [
        req_time for req_time in self.requests[api_key]
        if req_time > minute_ago]
    
    # Check if no. of requests exceeded the set limit
    if len(self.requests[api_key]) > self.requests_per_minute:
        return True
    self.requests[api_key].append(now)
    return False