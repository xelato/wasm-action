import vcr


def use_cassette(filepath):
    return vcr.use_cassette(
        filepath,
        record_mode="new_episodes",
        filter_headers=[
            "Authorization",
        ],
    )
