from urllib.parse import parse_qs, urlparse


def extract_video_id(url: str) -> str:
    parsed_url = urlparse(url)
    host = parsed_url.netloc.lower()

    # watch?v=
    if host in ("youtube.com", "www.youtube.com", "m.youtube.com"):
        if parsed_url.path == "/watch":
            video_id = parse_qs(parsed_url.query).get("v")
            if video_id:
                return video_id[0]

        # shorts
        if parsed_url.path.startswith("/shorts/"):
            return parsed_url.path.split("/")[2]

        # live
        if parsed_url.path.startswith("/live/"):
            return parsed_url.path.split("/")[2]

    # youtu.be
    if host == "youtu.be":
        return parsed_url.path.lstrip("/")

    raise ValueError("Invalid YouTube URL.")