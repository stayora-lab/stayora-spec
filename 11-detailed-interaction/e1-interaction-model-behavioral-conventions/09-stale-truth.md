# Stale Truth

| Condition | Meaning | Behavior |
|---|---|---|
| STALE BUT SAFE TO VIEW | displayed projection may be old but read remains safe | label as current-known/needs refresh conceptually; allow inspect |
| STALE — ACTION REVALIDATION REQUIRED | action consequence could change | revalidate before commitment |
| STALE — ACTION NO LONGER VALID | precondition no longer holds | do not commit; show current truth/recovery |
| CONFLICTED TRUTH | sources/evidence cannot safely coexist | preserve both, assign responsibility |
| UNKNOWN CURRENT OUTCOME | action may have occurred but result is unconfirmed | no duplicate mutation; reconciliation path |

No freshness duration is invented and stale is not automatically unavailable.
