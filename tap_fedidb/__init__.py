"""Python package for the tap-fedidb CLI."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Any, ClassVar

from singer_sdk import RESTStream, Stream, Tap
from singer_sdk import typing as th

if sys.version_info >= (3, 12):
    from typing import override
else:
    from typing_extensions import override

if TYPE_CHECKING:
    from singer_sdk.helpers.types import Context


class _FediDBStream(RESTStream[Any]):
    """FediDB stream class."""

    url_base = "https://api.fedidb.org"


class Servers(_FediDBStream):
    """Servers stream."""

    name = "servers"
    path = "/v1/servers"
    records_jsonpath = "$.data[*]"
    next_page_token_jsonpath = "$.meta.next_cursor"  # noqa: S105

    _page_size = 40

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("domain", th.StringType),
        th.Property("open_registration", th.BooleanType),
        th.Property("description", th.StringType),
        th.Property("banner_url", th.StringType),
        th.Property(
            "location",
            th.ObjectType(
                th.Property("city", th.StringType),
                th.Property("country", th.StringType),
            ),
        ),
        th.Property(
            "software",
            th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("name", th.StringType),
                th.Property("url", th.StringType),
                th.Property("version", th.StringType),
            ),
        ),
        th.Property(
            "stats",
            th.ObjectType(
                th.Property("status_count", th.IntegerType),
                th.Property("user_count", th.IntegerType),
                th.Property("monthly_active_users", th.IntegerType),
            ),
        ),
        th.Property("first_seen_at", th.DateTimeType),
        th.Property("last_seen_at", th.DateTimeType),
    ).to_dict()

    @override
    def get_url_params(
        self,
        context: Context | None,
        next_page_token: str | None,
    ) -> dict[str, Any] | str:
        params: dict[str, Any] = {"limit": self._page_size}
        if next_page_token:
            params["cursor"] = next_page_token
        return params


class Software(_FediDBStream):
    """Software stream."""

    name = "software"
    path = "/v1/software"
    records_jsonpath = "$[*]"

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("url", th.StringType),
        th.Property("name", th.StringType),
        th.Property("license", th.StringType),
        th.Property("website", th.StringType),
        th.Property("user_count", th.IntegerType),
        th.Property("description", th.StringType),
        th.Property("details_url", th.StringType),
        th.Property("source_repo", th.StringType),
        th.Property("status_count", th.IntegerType),
        th.Property("instance_count", th.IntegerType),
        th.Property(
            "latest_version",
            th.ObjectType(
                th.Property("version", th.StringType),
                th.Property("published_at", th.DateTimeType),
            ),
        ),
        th.Property("monthly_active_users", th.IntegerType),
    ).to_dict()


class PopularAccounts(_FediDBStream):
    """Popular accounts stream."""

    name = "popular_accounts"
    path = "/v1/popular-accounts"
    records_jsonpath = "$.data[*]"

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("rank", th.IntegerType),
        th.Property("username", th.StringType),
        th.Property("name", th.StringType),
        th.Property("domain", th.StringType),
        th.Property("account_url", th.StringType),
        th.Property("avatar_url", th.StringType),
        th.Property("following_count", th.IntegerType),
        th.Property("followers_count", th.IntegerType),
        th.Property("status_count", th.IntegerType),
        th.Property("webfinger", th.StringType),
        th.Property("bio", th.StringType),
        th.Property("account_created_at", th.DateTimeType),
        th.Property("last_fetched_at", th.DateTimeType),
    ).to_dict()


class TapFediDB(Tap):
    """Singer tap for FediDB."""

    name = "tap-fedidb"
    config_jsonschema: ClassVar[dict[str, Any]] = {
        "type": "object",
        "properties": {},
    }

    @override
    def discover_streams(self) -> list[Stream]:
        return [
            Servers(tap=self),
            Software(tap=self),
            PopularAccounts(tap=self),
        ]
